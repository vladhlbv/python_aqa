from lesson_16.figures_base import Figure
from lesson_16.figures import Triangle, Circle, Diamond


figures: list = [
    Triangle(side_length_1=5, side_length_2=10, side_length_3=7, angle_1= 30),
    Circle(circle_radius=3),
    Diamond(diamond_side_length=10, diamond_angle=30)
]

for figure in figures:
    print(figure)
    print(f"Area of figure: {figure.calculate_area_of_figure()}")
    print(f"Perimeter of figure: {figure.calculate_perimeter_of_figure()}\n")