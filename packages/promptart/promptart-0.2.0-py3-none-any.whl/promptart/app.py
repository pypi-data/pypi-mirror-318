# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT

import os

import streamlit as st

from promptart.gallery import image_gallery, speech_gallery
from promptart.image_generation import image_generation
from promptart.logo import logo
from promptart.speech_generation import speech_generation


def app() -> None:
    st.logo(logo)
    if os.getenv("PROMPTART_PASSWORD") != st.session_state.get("promptart_password"):
        with st.form("password_input"):
            promptart_password = st.text_input("Please enter password", type="password")
            submitted = st.form_submit_button(label="Submit")
        if submitted:
            st.session_state["promptart_password"] = promptart_password
            st.rerun()
        elif st.session_state.get("promptart_password") is not None:
            st.error("The entered password is not valid.")
    else:
        nav = st.navigation(
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
        nav.run()


if __name__ == "__main__":
    app()
