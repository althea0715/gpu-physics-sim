# ruff: noqa: F405


from collections import defaultdict

from glfw.GLFW import *  # type: ignore # noqa

from gpu_physics_sim.logger import get_logger


logger = get_logger(__name__)


class InputManager:
    def __init__(self):
        self._keys = defaultdict(bool)
        self.mouse_pos = (0.0, 0.0)

    def on_key(self, key: int, scancode: int, action: int, mods: int):
        # if action == GLFW_PRESS:
        #     self._keys[key] = True
        # elif action == GLFW_RELEASE:
        #     self._keys[key] = False
        print("ABC")

    def is_key_down(self, key: int) -> bool:
        return self._keys[key]

    def update_mouse(self, x: float, y: float):
        self.mouse_pos = (x, y)
