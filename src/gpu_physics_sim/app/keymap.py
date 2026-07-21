# ruff: noqa: F405

from enum import IntEnum

from glfw.GLFW import *  # type: ignore # noqa


class Key(IntEnum):
    ESC = GLFW_KEY_ESCAPE
