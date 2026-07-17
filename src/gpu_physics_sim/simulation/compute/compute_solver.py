from ..base import ISolver

class ComputeSolver(ISolver):
    def __init__(self, buffer_handle):
        self.buffer_handle = buffer_handle
        # Load and compile GLSL Compute Shader
        pass

    def step(self):
        # Dispatch compute shader
        pass

    def get_data_ptr(self):
        return self.buffer_handle
