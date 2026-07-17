# ruff: noqa: F405

from typing import Callable

from glfw.GLFW import *  # type: ignore # noqa
from glfw import _GLFWwindow as GLFWwindow

from gpu_physics_sim.logger import get_logger


logger = get_logger(__name__)


class Window:
    def __init__(self, title: str, width: int, height: int):

        self.width = width
        self.height = height

        self.key_listener: list[Callable[[int, int, int, int], None]] = []

        if not glfwInit():
            raise RuntimeError("GLFW Failed")

        glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4)
        glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 5)
        glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE)

        self.window = glfwCreateWindow(width, height, title, None, None)

        if not self.window:
            glfwTerminate()
            raise RuntimeError("Create Window Failed")

        glfwMakeContextCurrent(self.window)

        glfwSetFramebufferSizeCallback(self.window, self._framebuffer_size_callback)
        glfwSetKeyCallback(self.window, self._key_callback)

        self._fn_on_resize: Callable[[int, int], None] | None = None
        self._fn_on_key: Callable[[int, int, int, int], None] | None = None

    def _framebuffer_size_callback(self, _: GLFWwindow, width: int, height: int):
        self.width = width
        self.height = height

        if self._fn_on_resize:
            self._fn_on_resize(width, height)

    def _key_callback(self, _: GLFWwindow, key: int, code: int, action: int, mods: int):
        if self._fn_on_key:
            self._fn_on_key(key, code, action, mods)

    def should_close(self) -> bool:
        return glfwWindowShouldClose(self.window)

    def poll_events(self):
        glfwPollEvents()

    def swap_buffer(self):
        glfwSwapBuffers(self.window)

    def close(self):
        if self.window is not None:
            glfwDestroyWindow(self.window)
            self.window = None

        glfwTerminate()


    def set_resize_callback(self, fn: Callable[[int, int], None]):
        self._fn_on_resize = fn

    def set_key_callback(self, fn: Callable[[int, int, int, int], None]):
        self._fn_on_key = fn


