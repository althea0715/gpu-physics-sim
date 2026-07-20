# ruff: noqa: F405


from collections import defaultdict
from typing import Callable
from enum import Enum, auto

from glfw.GLFW import *  # type: ignore # noqa

from gpu_physics_sim.logger import get_logger


logger = get_logger(__name__)




type InputType = tuple[int,int,int,int]


class Action(Enum):
    QUIT = auto()



class InputManager:
    def __init__(self):
        self._keys = defaultdict(bool)
        self.mouse_pos = (0.0, 0.0)

        
        self._on_key_mapper:dict[InputType, Callable[[InputType], None]] = {}
        self._on_key_mapper[(GLFW_KEY_ESCAPE, GLFW_PRESS, GLFW_PRESS, GLFW_RELEASE)]

    def on_key(self, key: int, code: int, action: int, mods: int):

        # if action == GLFW_PRESS:

        print(key, mods)


        # if action == GLFW_PRESS:
        #     self._keys[key] = True
        # elif action == GLFW_RELEASE:
        #     self._keys[key] = False
        # print("ABC")

    def _should_window_close(self):

    def is_key_down(self, key: int) -> bool:
        return self._keys[key]

    def update_mouse(self, x: float, y: float):
        self.mouse_pos = (x, y)
