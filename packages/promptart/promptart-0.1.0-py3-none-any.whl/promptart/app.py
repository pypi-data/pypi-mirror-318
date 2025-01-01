# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT

import json
import os

import streamlit as st

from promptart.constants import CONFIG_PATH
from promptart.gallery import image_gallery, speech_gallery
from promptart.image_generation import image_generation
from promptart.logo import logo
from promptart.speech_generation import speech_generation

st.logo(logo)

if not st.session_state.get("openai_client_args"):
    st.session_state["openai_client_args"] = {}

if not os.getenv("OPENAI_API_KEY") and not st.session_state["openai_client_args"].get(
    "api_key"
):
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as config_file:
            config = json.load(config_file)
            st.session_state["openai_client_args"]["api_key"] = config.get(
                "openai_api_key"
            )
    else:
        with st.sidebar.popover(
            "API Key",
            use_container_width=True,
        ):
            st.session_state["openai_client_args"]["api_key"] = st.text_input(
                "OPENAI_API_KEY",
                type="password",
            )

pg = st.navigation(
    {
        "Image": [
            st.Page(image_generation, title="Generation"),
            st.Page(image_gallery, title="Gallery"),
        ],
        "Speech": [
            st.Page(speech_generation, title="Generation"),
            st.Page(speech_gallery, title="Gallery"),
        ],
    }
)

pg.run()
