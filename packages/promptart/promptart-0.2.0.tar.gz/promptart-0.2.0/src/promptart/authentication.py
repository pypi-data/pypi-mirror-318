# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT

import json
import os

import streamlit as st

from promptart.constants import CONFIG_PATH


def get_api_key(api_key_name: str) -> str:
    """
    Checks if API key is configured in default config file.
    Otherwise, ask user via popover password input in sidebar.
    """

    api_key = ""

    # check config file
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as config_file:
            config = json.load(config_file)
            api_key = config.get(api_key_name, "")

    # if not configured, ask from user
    if not api_key:
        with st.sidebar.popover(
            api_key_name.upper(),
            use_container_width=True,
        ):
            api_key = st.text_input(
                api_key_name.upper(),
                type="password",
            )

    return api_key


def check_openai_api_key() -> None:
    """
    Checks for OpenAI API key in multiple locations. If corresponding
    environment variable is set, no further setting is configured in
    session state. Otherwise, `get_api_key` is run, to check config
    file or to ask user for API key in the frontend.
    """

    api_key_name = "openai_api_key"

    if not st.session_state.get("openai_client_args"):
        st.session_state["openai_client_args"] = {}

    if not os.getenv(api_key_name.upper()) and not st.session_state[
        "openai_client_args"
    ].get("api_key"):
        st.session_state["openai_client_args"]["api_key"] = get_api_key(api_key_name)


def check_bfl_api_key() -> None:
    """
    Checks for BLF API key in multiple locations. If corresponding
    environment variable is set, the value is stored in session state.
    Otherwise, `get_api_key` is run, to check config file or to ask
    user for API key in the frontend.
    """

    api_key_name = "bfl_api_key"
    if not st.session_state.get(api_key_name):
        if os.getenv(api_key_name.upper()):
            st.session_state[api_key_name] = os.getenv(api_key_name.upper())
        else:
            st.session_state[api_key_name] = get_api_key(api_key_name)
