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

from promptart.constants import SPEECH_GEN_BASE_PATH, SPEECH_PROMPT_BASE_PATH


def speech_generation():
    with st.sidebar.form("Input Parameters", border=False):
        model = st.selectbox("Model", ["tts-1", "tts-1-hd"])
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
            tooltip = "Click to start image generation."
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
        st.session_state["last_speech"] = None
        st.session_state["last_speech_prompt"] = None

    if run_button:
        with st.spinner("Speech generation in progress ..."):
            client = OpenAI(**st.session_state["openai_client_args"])
            response = client.audio.speech.create(
                model=model,
                voice=voice,
                response_format=response_format,
                speed=speed,
                input=input_text,
            )
            base_name = str(time.time()) + "_" + str(uuid.uuid4())
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
            st.session_state["last_speech"] = speech_path
            st.session_state["last_speech_prompt"] = all_prompts

    if st.session_state["last_speech"]:
        with st.container(border=True):
            st.audio(st.session_state["last_speech"])
            st.write(st.session_state["last_speech_prompt"])
            with open(st.session_state["last_speech"], "rb") as download_file:
                st.download_button(
                    "Download Audio",
                    data=download_file,
                    file_name=st.session_state["last_speech"].name,
                )
