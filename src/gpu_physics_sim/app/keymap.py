# ruff: noqa: F405

from enum import Enum, auto

from glfw.GLFW import *  # type: ignore # noqa


class Key(Enum):
    ESC = auto()


GLFW_KEY_MAP: dict[int, Key] = {}
GLFW_KEY_MAP[GLFW_KEY_ESCAPE] = Key.ESC


def get_key_map(key: int) -> Key:
    return GLFW_KEY_MAP[key]


def is_pressed(action: int) -> bool:
    if action == GLFW_PRESS:
        return True

    return False
