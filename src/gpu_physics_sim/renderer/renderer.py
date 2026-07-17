# ruff: noqa: F405

from OpenGL.GL import *  # type: ignore # noqa

from gpu_physics_sim.logger import get_logger

logger = get_logger(__name__)

class Renderer:

    def __init__(self):
        logger.info(glGetString(GL_VERSION))

    def begin_frame(self):
        glClearColor(0.3, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def render(self, renderable: int):
        pass

    def end_frame(self):
        pass

    def on_resize(self, width: int, height: int):
        glViewport(0, 0, width, height)
