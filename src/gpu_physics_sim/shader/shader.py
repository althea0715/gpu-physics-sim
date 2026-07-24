# ruff: noqa: F405

from abc import ABC, abstractmethod
from typing import Self
from pathlib import Path
from enum import IntEnum
from ctypes import POINTER, cast, c_char, c_char_p, pointer, create_string_buffer

from OpenGL.GL import *  # type: ignore # noqa

from gpu_physics_sim.logger import get_logger

logger = get_logger(__name__)


class ShaderType(IntEnum):
    Vertex = GL_VERTEX_SHADER
    Fragment = GL_FRAGMENT_SHADER
    Compute = GL_COMPUTE_SHADER


class BaseShader(ABC):
    def __init__(self, code: str, shader_type: ShaderType):

        buffer = create_string_buffer(code.encode())
        buffer = cast(buffer, POINTER(c_char))

        strings = (POINTER(c_char) * 1)()
        strings[0] = buffer

        
        


        vertex_program = glCreateShaderProgramv(shader_type, 1, strings)

        print(vertex_program)

    @classmethod
    @abstractmethod
    def from_file(cls, path: str) -> Self: ...


class VertexShader(BaseShader):
    def __init__(self, code: str):
        super().__init__(code, ShaderType.Vertex)

    @classmethod
    def from_file(cls, path: str) -> Self:
        return cls(Path(path).read_text())


class FragmentShader(BaseShader):
    def __init__(self, code: str):
        super().__init__(code, ShaderType.Fragment)

    @classmethod
    def from_file(cls, path: str) -> Self:
        return cls(Path(path).read_text())


class ComputeShader(BaseShader):
    def __init__(self, code: str):
        super().__init__(code, ShaderType.Compute)

    @classmethod
    def from_file(cls, path: str) -> Self:
        return cls(Path(path).read_text())
