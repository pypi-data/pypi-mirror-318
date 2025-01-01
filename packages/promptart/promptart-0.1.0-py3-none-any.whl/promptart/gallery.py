# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT

import os
from pathlib import Path

import streamlit as st

from promptart.constants import (
    IMAGE_GEN_BASE_PATH,
    IMAGE_PROMPT_BASE_PATH,
    SPEECH_GEN_BASE_PATH,
    SPEECH_PROMPT_BASE_PATH,
)


def gallery(object_base_path, prompt_base_path, download_label, media_function):
    chosen_date = st.sidebar.date_input("Generation Date")
    generations_date_path = Path(object_base_path, str(chosen_date))
    prompt_date_path = Path(prompt_base_path, str(chosen_date))
    if generations_date_path.exists():
        file_list = sorted(os.listdir(generations_date_path), reverse=True)
        for idx, object_name in enumerate(file_list):
            with st.container(border=True):
                speech_path = Path(generations_date_path, object_name)
                prompt_path = Path(
                    prompt_date_path, object_name.rsplit(".", 1)[0] + ".txt"
                )
                prompt = ""
                if prompt_path.exists():
                    with open(prompt_path, "r") as prompt_file:
                        prompt = prompt_file.read()
                if not prompt:
                    prompt = "Description not found."
                media_function(speech_path)
                st.write(prompt)
                with open(speech_path, "rb") as download_file:
                    st.download_button(
                        download_label, data=download_file, file_name=object_name
                    )


def speech_gallery():
    gallery(SPEECH_GEN_BASE_PATH, SPEECH_PROMPT_BASE_PATH, "Download Audio", st.audio)


def image_gallery():
    gallery(IMAGE_GEN_BASE_PATH, IMAGE_PROMPT_BASE_PATH, "Download Image", st.image)
