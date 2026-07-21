# ruff: noqa: F405

import numpy as np

from ctypes import c_uint32, byref

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
        
        # fmt: off
        vertex = np.array(
            [
                -0.5, -0.5,  0.0,
                 0.5, -0.5,  0.0,
                 0.0,  0.5,  0.0,
            ],
            dtype=np.float32,
        )
        # fmt: on


        vbo = c_uint32(0)
        vao = c_uint32(0)

        glCreateBuffers(1, byref(vbo))
        glCreateVertexArrays(1, byref(vao))

        glNamedBufferStorage(vbo, vertex.nbytes, vertex, GL_DYNAMIC_STORAGE_BIT)
        glVertexArrayVertexBuffer(vao, 0, vbo, 0, 3 * vertex.itemsize)

        glEnableVertexArrayAttrib(vao, 0)
        glVertexArrayAttribFormat(vao, 0, 3, GL_FLOAT, GL_FALSE, 0)
        glVertexArrayAttribBinding(vao, 0, 0)

        glBindVertexArray(vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        
        
        glDeleteVertexArrays(1, vao)
        glDeleteBuffers(1, vbo)
        

    def end_frame(self):
        pass

    def on_resize(self, width: int, height: int):
        glViewport(0, 0, width, height)
