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
FLUX_MODELS = (
    "flux-pro-1.1",
    "flux-pro",
    "flux-dev",
    "flux-pro-1.1-ultra",
    "flux-pro-1.0-fill",
    "flux-pro-1.0-canny",
    "flux-pro-1.0-depth",
)
DALLE_MODELS = ("dall-e-3", "dall-e-2")
TTS_MODELS = ("tts-1", "tts-1-hd")
