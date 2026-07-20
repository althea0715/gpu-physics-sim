from typing import Self

from gpu_physics_sim.logger import get_logger

from gpu_physics_sim.input import InputManager
from gpu_physics_sim.app import Window, Timer, Action
from gpu_physics_sim.renderer import Renderer
from gpu_physics_sim.scene import Scene




logger = get_logger(__name__)


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

        self.window.set_resize_callback(self.renderer.on_resize)
        self.window.set_key_callback(self.input_manager.on_key)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc, tb):
        self.window.close()

    def run(self):

        timer = Timer()

        while not self.window.should_close():
            dt = timer.tick()

            self.window.poll_events()

            if self.input_manager.is_action_trigger(Action.Quit):
                self.window.request_close()

            self.scene.update(dt)

            self.renderer.begin_frame()

            self.renderer.render(self.scene.get_renderable())

            self.renderer.end_frame()

            self.window.swap_buffer()

            self.input_manager.clear_action_triggers()
