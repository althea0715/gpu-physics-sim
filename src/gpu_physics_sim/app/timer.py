# ruff: noqa: F405

from glfw.GLFW import *  # type: ignore # noqa


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
