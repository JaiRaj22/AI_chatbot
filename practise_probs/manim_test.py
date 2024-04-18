from manim import *

class Test(Scene):
    def construct(self):
        c = Circle(2, color = RED, fill_opacity = 0.1)
        self.play(DrawBorderThenFill(c), run_time = 0.5)
        self.wait(3)
    