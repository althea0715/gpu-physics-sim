from gpu_physics_sim.input import InputManager

class Scene:
    def update(self, dt: float, input_manager: InputManager):
        pass

    def get_renderable(self) -> int:
        return 0
