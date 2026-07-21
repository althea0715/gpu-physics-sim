# ruff: noqa: F405

from collections import defaultdict

from glfw.GLFW import *  # type: ignore # noqa

from gpu_physics_sim.logger import get_logger
from gpu_physics_sim.app import Action, Key

logger = get_logger(__name__)


class InputManager:
    def __init__(self):
        self._keys: dict[int, bool] = defaultdict(bool)
        self._key_binding: dict[int, Action] = {}
        self._key_trigger: set[Action] = set()

    def bind(self, key: Key, action: Action):
        self._key_binding[key] = action

    def on_key(self, key: int, action: bool):

        if action:
            self._keys[key] = True

            if key in self._key_binding.keys():
                self._key_trigger.add(self._key_binding[key])

        else:
            self._keys[key] = False

    def is_action_trigger(self, action: Action) -> bool:
        return action in self._key_trigger

    def clear_action_triggers(self):
        self._key_trigger.clear()
