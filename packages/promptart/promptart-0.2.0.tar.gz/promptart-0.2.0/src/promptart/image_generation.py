# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT

import base64
import os
import time
import uuid
from collections import OrderedDict
from datetime import datetime
from io import BytesIO
from pathlib import Path

import plotly.express as px
import requests
import streamlit as st
from openai import OpenAI
from PIL import Image, ImageDraw

from promptart.authentication import check_bfl_api_key, check_openai_api_key
from promptart.constants import (
    DALLE_MODELS,
    FLUX_MODELS,
    IMAGE_GEN_BASE_PATH,
    IMAGE_PROMPT_BASE_PATH,
)


def add_entry_from_url(
    image_url: str,
    description: str,
    model: str,
    file_format: str = "png",
) -> None:
    """
    Save a generated image and its description to a default location in the
    user home directory. This storage is used by the image gallery.
    """

    sortable_base_name = str(time.time()).replace(".", "_") + "_" + str(uuid.uuid4())
    today_date = str(datetime.today().date())
    generations_today_path = Path(IMAGE_GEN_BASE_PATH, today_date)
    prompt_today_path = Path(IMAGE_PROMPT_BASE_PATH, today_date)
    if not generations_today_path.exists():
        os.makedirs(generations_today_path)
    if not prompt_today_path.exists():
        os.makedirs(prompt_today_path)

    image_path = Path(generations_today_path, sortable_base_name + "." + file_format)
    prompt_path = Path(prompt_today_path, sortable_base_name + ".txt")
    img_response = requests.get(image_url, timeout=600)
    with open(image_path, "wb") as outfile:
        outfile.write(img_response.content)
    with open(prompt_path, "w") as outfile:
        outfile.write(description)
    st.session_state["last_image"][model] = image_path
    st.session_state["last_image_prompt"][model] = description


def flux_generation(model: str) -> None:
    """
    Sidebar configuration for image generation tasks with Flux models. The available
    API parameters for the models are in part fetched from the openapi specification.
    """

    check_bfl_api_key()
    with st.sidebar.form("flux_prompt_input", border=False):
        prompt_text = st.text_area("Prompt", key="flux_prompt", height=200)
        if not st.session_state.get("bfl_api_key"):
            disabled = True
            tooltip = "API key missing."
        else:
            disabled = False
            tooltip = "Click to start image generation."
        run_button = st.form_submit_button(
            "Run",
            type="secondary",
            use_container_width=True,
            disabled=disabled,
            help=tooltip,
        )
    st.sidebar.divider()
    model_params: OrderedDict[str, int | bool | float | str] = OrderedDict()
    input_images = {}
    if not st.session_state.get("flux_api_spec"):
        api_spec_response = requests.get("https://api.bfl.ml/openapi.json", timeout=60)
        if api_spec_response.status_code == 200:
            st.session_state["flux_api_spec"] = api_spec_response.json()
        else:
            st.error("Fetching API Spec failed.")
            st.error(api_spec_response.text)
    api_model_name = st.session_state["flux_api_spec"]["paths"][f"/v1/{model}"]["post"][
        "requestBody"
    ]["content"]["application/json"]["schema"]["$ref"].split("/")[-1]
    api_model = dict(
        st.session_state["flux_api_spec"]["components"]["schemas"][api_model_name]
    )
    for name, prop in api_model["properties"].items():
        if prop.get("anyOf") and prop.get("default") is not None:
            prop.update(prop["anyOf"][0])
        if name in ["prompt", "mask"]:
            continue
        elif name == "image":
            image_file = st.sidebar.file_uploader(
                prop["title"],
                help=prop["description"],
                key=name + "_" + model,
            )
            if image_file:
                image = Image.open(image_file).convert("RGB")
                mask = Image.new("L", image.size, 255)
                fig = px.imshow(image)
                fig.update_layout(
                    height=600,
                    margin=dict(t=0, b=0, r=0, l=0),
                    xaxis={"visible": False},
                    yaxis={"visible": False},
                )
                with st.container(border=True):
                    selection = st.plotly_chart(
                        fig,
                        on_select="rerun",
                        selection_mode="lasso",
                        use_container_width=True,
                    )
                if len(selection["selection"]["lasso"]) > 0:
                    polygon_coords = list(
                        zip(
                            selection["selection"]["lasso"][0]["x"],
                            selection["selection"]["lasso"][0]["y"],
                        )
                    )
                    ImageDraw.Draw(mask).polygon(polygon_coords, fill=0)
                    image.putalpha(mask)
                    with st.container(border=True):
                        st.image(image, use_container_width=True)
                    buffer = BytesIO()
                    image.save(buffer, format="PNG")
                    input_images[name] = base64.b64encode(buffer.getvalue()).decode(
                        "UTF-8"
                    )

        elif name in ["image_prompt", "control_image"]:
            image_file = st.sidebar.file_uploader(
                prop["title"],
                help=prop["description"],
                key=name + "_" + model,
            )
            if image_file is not None:
                input_images[name] = base64.b64encode(image_file.getvalue()).decode(
                    "UTF-8"
                )
        elif prop.get("type") == "integer":
            model_params[name] = st.sidebar.slider(
                prop["title"],
                min_value=int(prop["minimum"]),
                max_value=int(prop["maximum"]),
                value=int(prop["default"]),
                step=int(prop.get("multipleOf", 1)),
                help=prop["description"],
                key=name + "_" + model,
            )
        elif prop.get("type") == "number":
            model_params[name] = st.sidebar.slider(
                prop["title"],
                min_value=float(prop["minimum"]),
                max_value=float(prop["maximum"]),
                value=float(prop["default"]),
                step=float(prop.get("multipleOf", 0.1)),
                help=prop["description"],
                key=name + "_" + model,
            )
        elif prop.get("type") == "boolean":
            model_params[name] = st.sidebar.toggle(
                prop["title"],
                value=bool(prop["default"]),
                help=prop["description"],
                key=name + "_" + model,
            )
        elif name == "seed":
            seed = st.sidebar.number_input(
                prop["title"],
                value=None,
                min_value=0,
                help=prop["description"],
                key=name + "_" + model,
            )
            if seed:
                model_params[name] = seed
        elif name == "output_format":
            model_params[name] = st.sidebar.selectbox(
                "Output Format",
                ["png", "jpeg"],
                key=name + "_" + model,
            )
        elif name == "aspect_ratio":
            c1, c2 = st.sidebar.columns(2)
            r1 = c1.slider(
                "Aspect Ratio",
                9,
                21,
                16,
                key=name + "_1_" + model,
            )
            r2 = c2.slider(
                "Aspect Ratio 2",
                9,
                21,
                9,
                key=name + "_2_" + model,
                label_visibility="hidden",
            )
            model_params[name] = f"{r1}:{r2}"
        else:
            pass

    if run_button:
        with st.spinner("Image generation in progress ..."):
            url = "https://api.bfl.ml/v1/" + model
            headers = {
                "Content-Type": "application/json",
                "X-Key": st.session_state.get("bfl_api_key"),
            }
            task_response = requests.post(
                url,
                json=dict(prompt=prompt_text, **model_params, **input_images),
                headers=headers,
                timeout=600,
            )
            if "id" in task_response.json():
                task_id = task_response.json()["id"]
                status = "Pending"
                while status == "Pending":
                    time.sleep(0.5)
                    url = "https://api.bfl.ml/v1/get_result?id=" + task_id
                    headers = {"X-Key": st.session_state.get("bfl_api_key")}
                    result_response = requests.get(
                        url,
                        headers=headers,
                        timeout=600,
                    )
                    status = result_response.json()["status"]
                if status == "Ready":
                    image_url = result_response.json()["result"]["sample"]
                    revised_prompt = None
                    if model_params.get("prompt_upsampling"):
                        revised_prompt = result_response.json()["result"]["prompt"]
                    description = (
                        f"**User Prompt:** {prompt_text}\n\n**Revised Prompt:** {revised_prompt}"
                        f"\n\n**Model:** {model}"
                    )
                    for param_name, param in model_params.items():
                        param_name_title = param_name.replace("_", " ").title()
                        description += f", **{param_name_title}:** {param}"
                    description += (
                        f", **Used Input Image:** {bool(len(input_images) > 0)}"
                    )
                    add_entry_from_url(
                        image_url,
                        description,
                        model,
                        str(model_params["output_format"]),
                    )
                else:
                    st.error("An error occured")
                    st.error("Task reponse: " + repr(task_response.json()))
                    st.error("Result response: " + repr(result_response.json()))
            else:
                st.error("An error occured")
                st.error("Task reponse: " + repr(task_response.json()))


def dalle_generation(model) -> None:
    """
    Sidebar configuration for image generation tasks with Dall-E models.
    """

    check_openai_api_key()
    with st.sidebar.form("dalle_prompt_input", border=False):
        prompt_text = st.text_area("Prompt", key="dalle_prompt", height=200)
        if not os.getenv("OPENAI_API_KEY") and not st.session_state[
            "openai_client_args"
        ].get("api_key"):
            disabled = True
            tooltip = "API key missing."
        else:
            disabled = False
            tooltip = "Click to start image generation."
        run_button = st.form_submit_button(
            "Run",
            type="secondary",
            use_container_width=True,
            disabled=disabled,
            help=tooltip,
        )
    st.sidebar.divider()
    model_params = OrderedDict()
    if model == "dall-e-3":
        model_params["size"] = st.sidebar.selectbox(
            "Size", ["1024x1024", "1792x1024", "1024x1792"]
        )
        model_params["quality"] = st.sidebar.selectbox("Quality", ["standard", "hd"])
        model_params["style"] = st.sidebar.selectbox("Style", ["vivid", "natural"])
    else:
        model_params["size"] = st.sidebar.selectbox(
            "Size", ["1024x1024", "256x256", "512x512"]
        )

    if run_button and prompt_text:
        with st.spinner("Image generation in progress ..."):
            client = OpenAI(**st.session_state["openai_client_args"])
            response = client.images.generate(
                model=model,
                prompt=prompt_text,
                n=1,
                **model_params,  # type: ignore
            )
            image_url = str(response.data[0].url)
            if image_url:
                revised_prompt = response.data[0].revised_prompt
                description = (
                    f"**User Prompt:** {prompt_text}\n\n**Revised Prompt:** {revised_prompt}"
                    f"\n\n**Model:** {model}"
                )
                for param_name, param in model_params.items():
                    description += f", **{param_name.title()}:** {param}"
                add_entry_from_url(image_url, description, model)
            else:
                st.error("Url is missing in model response.")


def image_generation() -> None:
    """
    App page definition for all image generation tasks. Depending on model choice,
    the corresponding sidebar configuration is loaded.
    """

    if "last_image" not in st.session_state:
        st.session_state["last_image"] = {}
        st.session_state["last_image_prompt"] = {}

    model = st.sidebar.selectbox("Model", FLUX_MODELS + DALLE_MODELS)

    if model in FLUX_MODELS:
        flux_generation(model)
    elif model in DALLE_MODELS:
        dalle_generation(model)
    else:
        st.error("Unknown model name.")

    if st.session_state["last_image"].get(model):
        with st.container(border=True):
            st.image(st.session_state["last_image"].get(model))
            st.write(st.session_state["last_image_prompt"].get(model))
            with open(st.session_state["last_image"].get(model), "rb") as download_file:
                st.download_button(
                    "Download Image",
                    data=download_file,
                    file_name=st.session_state["last_image"].get(model).name,
                )
