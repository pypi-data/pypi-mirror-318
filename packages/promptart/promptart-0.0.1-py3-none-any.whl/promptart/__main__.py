# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT

import sys
from pathlib import Path

from streamlit.web.cli import main


def entrypoint():
    lib_path = Path(__file__).parent
    main(["run", str(Path(lib_path, "app.py"))] + sys.argv[1:])


if __name__ == "__main__":
    entrypoint()
