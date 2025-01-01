# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT

import os
import time
import uuid
from datetime import datetime
from pathlib import Path

import requests
import streamlit as st
from openai import OpenAI

from promptart.constants import IMAGE_GEN_BASE_PATH, IMAGE_PROMPT_BASE_PATH


def image_generation():
    model = st.sidebar.selectbox("Model", ["dall-e-3", "dall-e-2"])
    if model == "dall-e-3":
        size = st.sidebar.selectbox("Size", ["1024x1024", "1792x1024", "1024x1792"])
        quality = st.sidebar.selectbox("Quality", ["standard", "hd"])
        style = st.sidebar.selectbox("Style", ["vivid", "natural"])
        optional_params = {"quality": quality, "style": style}
    else:
        size = st.sidebar.selectbox("Size", ["1024x1024", "256x256", "512x512"])
        quality = None
        style = None
        optional_params = {}
    with st.sidebar.form("Input Parameters", border=False):
        prompt_text = st.text_area("Prompt", height=250)
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

    today = str(datetime.today().date())
    generations_today_path = Path(IMAGE_GEN_BASE_PATH, today)
    prompt_today_path = Path(IMAGE_PROMPT_BASE_PATH, today)
    if not generations_today_path.exists():
        os.makedirs(generations_today_path)
    if not prompt_today_path.exists():
        os.makedirs(prompt_today_path)

    if "last_image" not in st.session_state:
        st.session_state["last_image"] = None
        st.session_state["last_image_prompt"] = None

    if run_button and prompt_text:
        with st.spinner("Image generation in progress ..."):
            client = OpenAI(**st.session_state["openai_client_args"])
            response = client.images.generate(
                model=model,
                prompt=prompt_text,
                size=size,
                n=1,
                **optional_params,
            )

            image_url = response.data[0].url
            revised_prompt = response.data[0].revised_prompt
            all_prompts = (
                f"**User Prompt:** {prompt_text}\n\n**Revised Prompt:** {revised_prompt}"
                f"\n\n**Model:** {model}, **Quality:** {quality}, **Style:** {style}"
            )
            base_name = str(time.time()) + "_" + str(uuid.uuid4())
            image_path = Path(generations_today_path, base_name + ".png")
            prompt_path = Path(prompt_today_path, base_name + ".txt")
            img_response = requests.get(image_url, timeout=120)
            with open(image_path, "wb") as outfile:
                outfile.write(img_response.content)
            with open(prompt_path, "w") as outfile:
                outfile.write(all_prompts)
            st.session_state["last_image"] = image_path
            st.session_state["last_image_prompt"] = all_prompts

    if st.session_state["last_image"]:
        with st.container(border=True):
            st.image(st.session_state["last_image"])
            st.write(st.session_state["last_image_prompt"])
            with open(st.session_state["last_image"], "rb") as download_file:
                st.download_button(
                    "Download Image",
                    data=download_file,
                    file_name=st.session_state["last_image"].name,
                )
