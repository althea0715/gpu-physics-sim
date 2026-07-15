from typing import Self

from glfw.GLFW import *
from OpenGL.GL import *

from gpu_physics_sim.logger import get_logger


logger = get_logger(__name__)


class Window:
    def __init__(self, title: str, width: int, height: int):

        self.width = width
        self.height = height

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
        glViewport(0, 0, width, height)

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

    def on_resize(self):
        pass
    def on_key(self):
        pass
    def on_mouse_move(self):
        pass
    def on_scroll(self):
        pass
    def on_close(self):
        pass


class Renderer:
    def begin_frame(self):
        glClearColor(0.3, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def draw_mesh(self):
        pass

    def draw_particles(self):
        pass

    def end_frame(self):
        pass


class Scene:
    def update(self, dt:float):
        pass

    def render(self, renderer: Renderer):
        pass


class Timer:
    def tick(self) -> float:
        pass

class Application:
    def __init__(self, window: Window, renderer: Renderer, scene: Scene):
        self.window = window
        self.renderer = renderer
        self.scene = scene

        self.timer = Timer()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb):
        self.window.close()

    def run(self):

        while not self.window.should_close():

            dt = self.timer.tick()

            self.window.poll_events()

            self.scene.update(dt)

            self.renderer.begin_frame()

            self.scene.render(self.renderer)

            self.renderer.end_frame()

            self.window.swap_buffer()


def main():

    window = Window("GPU Physics Sim", 400, 300)
    renderer = Renderer()
    scene = Scene()

    with Application(window, renderer, scene) as app:
        app.run()


if __name__ == "__main__":
    main()
