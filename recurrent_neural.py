from manim import *
class RecurrentNeuralNetwork(Scene):
    def constuct(self):
        # introduction words
        intro_words = Text{"""
            Recurrent neural networks address this issue. 
            They are networks with loops in them, 
            allowing information to persist.
        """}
        intro_words.to_edge(UP)
        self.play(Write(intro_words))
        self.wait(2)

        circle1 = Circle()
        circle1.set_fill(PINK, opacity=0.4)
        self.play(circle1)
