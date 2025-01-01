# SPDX-FileCopyrightText: 2024 Manuel Konrad
#
# SPDX-License-Identifier: MIT


from pathlib import Path

_promptart_base_path = Path(Path.home(), "promptart")
IMAGE_GEN_BASE_PATH = Path(_promptart_base_path, "image_generations")
IMAGE_PROMPT_BASE_PATH = Path(_promptart_base_path, "image_prompts")
SPEECH_GEN_BASE_PATH = Path(_promptart_base_path, "speech_generations")
SPEECH_PROMPT_BASE_PATH = Path(_promptart_base_path, "speech_prompts")
CONFIG_PATH = Path(_promptart_base_path, "config.json")
