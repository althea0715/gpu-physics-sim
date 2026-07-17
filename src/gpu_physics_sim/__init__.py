from gpu_physics_sim.logger import setup_logger

from gpu_physics_sim.input import InputManager
from gpu_physics_sim.renderer import Renderer
from gpu_physics_sim.scene import Scene
from gpu_physics_sim.app import Application, Window


def main():

    setup_logger()

    window = Window("GPU Physics Sim", 400, 300)
    renderer = Renderer()
    scene = Scene()

    input_manager = InputManager()

    with Application(window, renderer, scene, input_manager) as app:
        app.run()


if __name__ == "__main__":
    main()
