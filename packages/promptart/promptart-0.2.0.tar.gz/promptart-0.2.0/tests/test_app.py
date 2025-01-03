# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT

from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_minimal():
    at = AppTest.from_file(Path("src", "promptart", "app.py"), default_timeout=30)
    at.run()
    if at.exception:
        raise AssertionError("Ecountered exception: " + repr(at.exception))
