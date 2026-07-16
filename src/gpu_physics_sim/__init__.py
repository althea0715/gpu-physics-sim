# ruff: noqa: F405

from typing import Self, Callable
from collections import defaultdict

from glfw.GLFW import *  # type: ignore # noqa
from glfw import _GLFWwindow as GLFWwindow
from OpenGL.GL import *  # type: ignore # noqa

from gpu_physics_sim.logger import get_logger


logger = get_logger(__name__)


class InputManager:
    def __init__(self):
        self._keys = defaultdict(bool)
        self.mouse_pos = (0.0, 0.0)

    def update_key(self, key: int, scancode: int, action: int, mods: int):
        # if action == GLFW_PRESS:
        #     self._keys[key] = True
        # elif action == GLFW_RELEASE:
        #     self._keys[key] = False
        print("ABC")

    def is_key_down(self, key: int) -> bool:
        return self._keys[key]

    def update_mouse(self, x: float, y: float):
        self.mouse_pos = (x, y)


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
        logger.info(glGetString(GL_VERSION))

        glfwSetFramebufferSizeCallback(self.window, self._framebuffer_size_callback)
        glfwSetKeyCallback(self.window, self._key_callback)

    def _framebuffer_size_callback(self, _: GLFWwindow, width: int, height: int):
        self.width = width
        self.height = height

        glViewport(0, 0, width, height)
        self.on_resize(width, height)

    def _key_callback(
        self, window: GLFWwindow, key: int, scancode: int, action: int, mods: int
    ):
        if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
            glfwSetWindowShouldClose(window, True)

        for func in self.key_listener:
            func(key, scancode, action, mods)

        self.on_key(key, scancode, action, mods)

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

    def add_key_listener(self, func: Callable[[int, int, int, int], None]):
        self.key_listener.append(func)

    def on_key(self, key: int, scancode: int, action: int, mods: int):
        pass

    def on_resize(self, width: int, height: int):
        pass

    def on_mouse_move(self):
        pass

    def on_scroll(self):
        pass

    def on_close(self):
        pass


class Scene:
    def update(self, dt: float, input_manager: InputManager):
        pass

    def get_renderable(self) -> int:
        return 0


class Renderer:
    def begin_frame(self):
        glClearColor(0.3, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def render(self, renderable: int):
        pass

    def end_frame(self):
        pass


class Timer:
    def __init__(self):
        self.previous: float = 0.0
        self.elapsed: float = 0.0
        self.frames: int = 0
        self.fps: int = 0

        self.reset()

    def reset(self):
        self.previous = glfwGetTime()

    def tick(self) -> float:
        current_time = glfwGetTime()
        dt = current_time - self.previous
        self.previous = current_time

        self.elapsed += dt
        self.frames += 1
        if self.elapsed >= 1:
            self.fps = self.frames
            self.frames = 0
            self.elapsed = 0

        return dt


class Application:
    def __init__(
        self,
        window: Window,
        renderer: Renderer,
        scene: Scene,
        input_manager: InputManager,
    ):
        self.window = window
        self.scene = scene
        self.renderer = renderer
        self.input_manager = input_manager

        self.window.add_key_listener(self.input_manager.update_key)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb):
        self.window.close()

    def run(self):

        timer = Timer()

        while not self.window.should_close():
            dt = timer.tick()

            self.window.poll_events()

            self.scene.update(dt, self.input_manager)

            self.renderer.begin_frame()

            self.renderer.render(self.scene.get_renderable())

            self.renderer.end_frame()

            self.window.swap_buffer()


def main():

    window = Window("GPU Physics Sim", 400, 300)
    renderer = Renderer()
    scene = Scene()

    input_manager = InputManager()

    with Application(window, renderer, scene, input_manager) as app:
        app.run()


if __name__ == "__main__":
    main()
