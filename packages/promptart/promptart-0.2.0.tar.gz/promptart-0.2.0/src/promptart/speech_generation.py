# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT

import os
import time
import uuid
from datetime import datetime
from pathlib import Path

import streamlit as st
from openai import OpenAI

from promptart.authentication import check_openai_api_key
from promptart.constants import (
    SPEECH_GEN_BASE_PATH,
    SPEECH_PROMPT_BASE_PATH,
    TTS_MODELS,
)


def speech_generation() -> None:
    """
    App page definition for OpenAI speech generation tasks.
    """

    model = st.sidebar.selectbox("Model", TTS_MODELS)
    check_openai_api_key()
    with st.sidebar.form("tts_param_input", border=False):
        voice = st.selectbox(
            "Voice",
            [
                "alloy",
                "ash",
                "coral",
                "echo",
                "fable",
                "onyx",
                "nova",
                "sage",
                "shimmer",
            ],
        )
        response_format = st.selectbox("Format", ["wav", "aac", "mp3"])
        speed = st.slider("Speed", 0.25, 4.0, 1.0, step=0.05)
        input_text = st.text_area("Text", height=250)
        if not os.getenv("OPENAI_API_KEY") and not st.session_state[
            "openai_client_args"
        ].get("api_key"):
            disabled = True
            tooltip = "API key missing."
        else:
            disabled = False
            tooltip = "Click to start speech generation."
        run_button = st.form_submit_button(
            "Run",
            type="secondary",
            use_container_width=True,
            disabled=disabled,
            help=tooltip,
        )

    today = str(datetime.today().date())
    generations_today_path = Path(SPEECH_GEN_BASE_PATH, today)
    prompt_today_path = Path(SPEECH_PROMPT_BASE_PATH, today)
    if not generations_today_path.exists():
        os.makedirs(generations_today_path)
    if not prompt_today_path.exists():
        os.makedirs(prompt_today_path)

    if "last_speech" not in st.session_state:
        st.session_state["last_speech"] = {}
        st.session_state["last_speech_prompt"] = {}

    if run_button:
        with st.spinner("Speech generation in progress ..."):
            client = OpenAI(**st.session_state["openai_client_args"])
            response = client.audio.speech.create(
                model=model,
                voice=voice,  # type: ignore
                response_format=response_format,  # type: ignore
                speed=speed,
                input=input_text,
            )
            base_name = str(time.time()).replace(".", "_") + "_" + str(uuid.uuid4())
            speech_path = Path(
                generations_today_path, base_name + "." + response_format
            )
            prompt_path = Path(prompt_today_path, base_name + ".txt")
            response.stream_to_file(speech_path)
            all_prompts = (
                f"**Text:** {input_text}"
                f"\n\n**Model:** {model}, **Voice:** {voice}, "
                f"**Speed:** {speed}, **Format:** {response_format}"
            )
            with open(prompt_path, "w") as outfile:
                outfile.write(all_prompts)
            st.session_state["last_speech"][model] = speech_path
            st.session_state["last_speech_prompt"][model] = all_prompts

    if st.session_state["last_speech"].get(model):
        with st.container(border=True):
            st.audio(st.session_state["last_speech"].get(model))
            st.write(st.session_state["last_speech_prompt"].get(model))
            with open(
                st.session_state["last_speech"].get(model), "rb"
            ) as download_file:
                st.download_button(
                    "Download Audio",
                    data=download_file,
                    file_name=st.session_state["last_speech"].get(model).name,
                )
