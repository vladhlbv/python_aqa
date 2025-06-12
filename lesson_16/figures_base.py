from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def calculate_area_of_figure(self):
        pass

    @abstractmethod
    def calculate_perimeter_of_figure(self):
        pass