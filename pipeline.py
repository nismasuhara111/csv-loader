from abc import ABC, abstractmethod


class Step(ABC):
    """
    Abstract base class for every pipeline step.
    """

    @abstractmethod
    def run(self, data):
        """
        Process the input data and return the result.
        """
        pass


class Pipeline:
    """
    Pipeline executes a sequence of interchangeable Step objects.
    """

    def __init__(self, steps):
        self.steps = steps

    def run(self, data):
        for step in self.steps:
            data = step.run(data)

        return data