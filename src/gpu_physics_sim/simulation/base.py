from abc import ABC, abstractmethod
import numpy as np

class ISolver(ABC):
    @abstractmethod
    def step(self):
        """Perform one simulation step."""
        pass

    @abstractmethod
    def get_data_ptr(self):
        """Return pointer/handle to the simulation data for rendering."""
        pass
