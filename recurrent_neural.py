from manim import *

class RecurrentNeuralNetwork(Scene):
    def construct(self):
        # introduction words
        # intro_words = Text("""
        #     Recurrent neural networks address this issue.
        #     They are networks with loops in them,
        #     allowing information to persist.中文
        # """)
        # intro_words.to_edge(UP)
        # self.play(FadeIn(intro_words))
        # self.wait(0.5)
        # self.play(FadeOut(intro_words))
        # self.wait(0.5)




        circle1 = Circle().set_height(1).shift(UP*2)
        circle1.set_fill(PINK, opacity=0.4)
        circle1word = MathTex("h_t").set_height(0.5).shift(UP*2)
        self.play(Create(circle1))
        self.play(Write(circle1word))
        # self.wait(2)
        # self.play()

        rec1word = MathTex("A").set_height(0.75)
        rec1 = Rectangle(color = GREEN,height=1,width=2)
        self.play(Create(rec1),run_time=0.5)
        self.play(Write(rec1word))

        circle2 = Circle().set_height(1).shift(DOWN * 2)
        circle2.set_fill(BLUE, opacity=0.4)
        circle2word = MathTex("X_t").set_height(0.5).shift(DOWN * 2)
        self.play(Create(circle2),run_time=0.5)
        self.play(Write(circle2word))

        arr1 = Arrow(stroke_width = 1,buff=2,start=ORIGIN,end=UP,color = WHITE).shift(UP*0.5)
        arr2 = Arrow(stroke_width = 1,buff=2,start=DOWN,end=ORIGIN,color = WHITE).shift(DOWN*0.5)
        # g = Group(arr1, arr2)
        cur1 = CurvedArrow(stroke_width = 1,start_point=DOWN,end_point=UP,angle=PI,color=WHITE).set_height(1).shift(RIGHT*0.5)
        self.play(Create(arr1), run_time = 0.25)
        self.play(Create(arr2), run_time = 0.25)
        self.play(Create(cur1), run_time = 0.25)
        self.wait(2)
        pic1 = Group(*self.mobjects)
        self.play(ApplyMethod(pic1.to_edge,LEFT,buff=SMALL_BUFF),runtime=0.5)
        self.wait(0.5)

        pic2 = Group(rec1,rec1word,circle1,circle1word,circle2,circle2word,arr1,arr2)
        tex1 = MathTex("=").shift(LEFT*3.5)
        self.play(Write(tex1))
        for i in range(3):
            cop = pic2.copy()
            self.play(ApplyMethod(cop.shift,RIGHT*(4+i*3),buff=SMALL_BUFF),runtime=0.5)
            if i != 2:
                arr0 = Arrow(stroke_width = 1,buff=2,start=LEFT,end=RIGHT,color = WHITE).set_width(1).shift(RIGHT*(3*i))
                self.play(Create(arr0))
            self.wait(0.5)

        all1 = Group(*self.mobjects)
        self.play(FadeOut(all1))
        self.wait(0.5)

        # 展示公式
        mat0 = Text("误差项沿时间反向传播的公式").shift(UP * 2 + LEFT * 2)
        mat1 = MathTex("\delta^{T}_{t}=\delta^{T}_{t}\prod_{i=k}^{t-1} diag[f^{'}(net_i)]W")
        self.play(Write(mat0))
        self.play(Write(mat1))
        self.wait(2)
        self.play(FadeOut(mat0))
        self.play(FadeOut(mat1))
        self.wait(1)
        mat2 = Text("由此可得：").shift(UP * 2 + LEFT * 2)
        mat3 = MathTex("""
                \\begin{split}
        \|\delta^{T}_{t}\|&\leq\|\delta^{T}_{t}\| \prod_{i=k}^{t-1} \|diag[f^{'}(net_i)]\|\|W\|
        \\\\
        &\leq \|\delta^{T}_{t}\| (\\beta_f\\beta_W)^{t-k}
        \end{split}
        """)
        self.play(Write(mat2))
        self.play(Write(mat3))
        self.wait(2)
        self.play(FadeOut(mat2))
        self.play(FadeOut(mat3))
        self.wait(1)
        # # 原始RNN与LSTM对比图
        # cir1 = Circle(color=BLUE).set_height(1).shift(LEFT)
        # mar1 = Text("h").set_height(0.75).shift(LEFT)
        # cir2 = Circle(color=GREEN).set_height(1).shift(RIGHT+UP)
        # mar2 = Text("c").set_height(0.75).shift(RIGHT+UP)
        # cir3 = Circle(color=BLUE).set_height(1).shift(RIGHT + DOWN)
        # mar3 = Text("h").set_height(0.75).shift(RIGHT+DOWN)
        # arr3 = Arrow(start=LEFT,end=RIGHT).set_width(0.5)
        # wor1 = Text("原始RNN").shift(LEFT+DOWN*2)
        # wor2 = Text("LSTM").shift(RIGHT+DOWN*2)
        #
        # self.play(Create(cir1),Create(cir2),Create(cir3),Create(arr3),Create(wor1),Create(wor2),Create(mar1),Create(mar2),Create(mar3))
        # self.wait(2)
        # self.play(FadeOut(cir1),FadeOut(cir2),FadeOut(cir3),FadeOut(arr3),FadeOut(wor1),FadeOut(wor2),FadeOut(mar1),FadeOut(mar2),FadeOut(mar3))
        # self.wait(2)
class compare(Scene):
    def construct(self):
        # 原始RNN与LSTM对比图

        rec1 = Rectangle(height=4, width=2).shift(LEFT * 2)
        rec2 = Rectangle(height=4, width=2).shift(RIGHT*2)

        cir1 = Circle(color=BLUE).set_height(1).shift(LEFT*2)
        mar1 = Text("h").set_height(0.75).shift(LEFT*2)

        cir2 = Circle(color=GREEN).set_height(1).shift(RIGHT*2 + UP)
        mar2 = Text("c").set_height(0.75).shift(RIGHT*2 + UP)

        cir3 = Circle(color=BLUE).set_height(1).shift(RIGHT*2 + DOWN)
        mar3 = Text("h").set_height(0.75).shift(RIGHT*2 + DOWN)

        arr3 = Arrow(start=LEFT, end=RIGHT).set_width(1)
        wor1 = Text("原始RNN").shift(LEFT*2 + DOWN * 3)
        wor2 = Text("LSTM").shift(RIGHT*2 + DOWN * 3)

        self.play(Create(cir1), Create(cir2), Create(cir3), Create(arr3), Create(wor1), Create(wor2), Create(mar1),
                  Create(mar2), Create(mar3),Create(rec1),Create(rec2))
        self.wait(2)
        # self.play(FadeOut(cir1), FadeOut(cir2), FadeOut(cir3), FadeOut(arr3), FadeOut(wor1), FadeOut(wor2), FadeOut(mar1),
        #           FadeOut(mar2), FadeOut(mar3))
        # self.wait(2)

class LSTM(Scene):
    def construct(self):
        frame_width = 15  # 8.0 * 1.777 = 14.222
        frame_height = 20
        xt = Circle(color=BLUE).set_height(1).shift(LEFT*5+DOWN*3.75)
        l1 = Line(ORIGIN,UP).set_height(0.5).shift(LEFT*5+DOWN*3.5)
        word1 = MathTex("X_t").set_height(0.5).shift(LEFT*5+DOWN*3.75)
        self.play(Create(xt),Create(l1),Create(word1))

        rec1 = Rectangle(height=1,width=2,color = YELLOW).shift(RIGHT*1+DOWN*1.5)
        rec2 = Rectangle(height=1, width=2,color = YELLOW).shift(RIGHT * 4 + DOWN * 1.5)
        rec3 = Rectangle(height=1, width=2,color = YELLOW).shift(LEFT * 2 + DOWN * 1.5)
        rec4 = Rectangle(height=1, width=2,color = YELLOW).shift(LEFT * 5 + DOWN * 1.5)

        mat1 = MathTex("\sigma",height=0.5).shift(RIGHT*1+ DOWN*1.5)
        mat2 = MathTex("\sigma", height=0.5).shift(RIGHT * 4 + DOWN * 1.5)
        mat3 = Text("tanh", height=0.5).shift(LEFT * 2 + DOWN * 1.5)
        mat4 = MathTex("\sigma", height=0.5).shift(LEFT * 5 + DOWN * 1.5)

        cir1 = Circle(fill_color=PINK).set_height(1).shift(RIGHT*4+UP*0.5)
        cir2 = Circle(fill_color=PINK).set_height(1).shift(RIGHT*1+UP*0.5)
        cir3 = Circle(fill_color=PINK).set_height(1).shift(RIGHT * 1 + UP *3.5)
        cir4 = Circle(fill_color=PINK).set_height(1).shift(LEFT * 5 + UP * 3.5)

        mat5 = MathTex("X",height=0.5).shift(RIGHT*4+UP*0.5)
        mat6 = MathTex("X",height=0.5).shift(RIGHT*1+UP*0.5)
        mat7 = MathTex("+",height=0.5).shift(RIGHT*1+ UP *3.5)
        mat8 = MathTex("X",height=0.5).shift(LEFT * 5 + UP * 3.5)

        eli1 = Ellipse().shift(RIGHT*4+UP*2)
        mat9 = MathTex("\\tanh",height=0.5).shift(RIGHT*4+UP*2)

        self.play(Create(cir1),Create(cir2),Create(cir3),Create(cir4),
                  Create(mat5),Create(mat6),Create(mat7),Create(mat8),
                  Create(eli1),Create(mat9))
        self.play(Create(rec1),Create(rec2),Create(rec3),Create(rec4),
                  Write(mat1),Write(mat2),Write(mat3),Write(mat4))
        # self.wait(2)

        lin1 = Line(start=LEFT,end=RIGHT).set_width(3).shift(LEFT*6+DOWN*3)
        lin2 = Line(start=LEFT,end=RIGHT).set_width(3).shift(LEFT*3.5+DOWN*3)
        lin3 = Line(start=LEFT,end=RIGHT).set_width(3).shift(LEFT*0.5+DOWN*3)
        lin4 = Line(start=LEFT,end=RIGHT).set_width(3).shift(RIGHT*2.5+DOWN*3)

        lin5 = Line(start=ORIGIN,end=UP).set_height(1).shift(LEFT*5+DOWN*3)
        lin6 = Line(start=ORIGIN, end=UP).set_height(1).shift(LEFT * 2 + DOWN * 3)
        lin7 = Line(start=ORIGIN, end=UP).set_height(1).shift(RIGHT*1 + DOWN * 3)
        lin8 = Line(start=ORIGIN, end=UP).set_height(1).shift(RIGHT * 4 + DOWN * 3)


        lin9 = Line(start=ORIGIN, end=UP).set_height(1).shift(RIGHT+DOWN)

        self.play(Create(lin1),Create(lin2),Create(lin3),Create(lin4),
                  Create(lin5),Create(lin6),Create(lin7),Create(lin8),
                  Create(lin9))

        arr1 = Arrow(start=ORIGIN, end=UP).set_height(4).shift(LEFT*5+UP*0.5)
        tmp1 = Arrow(start=LEFT,end=RIGHT).set_width(1.25).shift(UP*0.5)
        # tmp2 = ArcBetweenPoints(start=UP,end=LEFT,angle=PI/2).shift(LEFT*2/3+DOWN*2/3).set_width(1.5)
        tmp2 = ArcBetweenPoints(start=UP,end=LEFT,angle=PI/2).next_to(rec3,UP).shift(RIGHT*0.75).set_width(1.5)
        # arr2 = Group(tmp1,tmp2)
        # arr3 = CurvedArrow(LEFT,UP,angle=-PI/2).set_height(1.5).shift(RIGHT*(5+1/3)+DOWN*(2/3))
        arr3 = Arrow(ORIGIN,UP).set_height(1).shift(RIGHT*4+DOWN)
        arr4 = Arrow(start=ORIGIN, end=UP,stroke_width=1).set_height(2).shift(RIGHT + UP*1.5)
        lin10 = Line(ORIGIN,UP).set_height(0.5).shift(RIGHT*4+UP*0.75)
        lin11 = Line(ORIGIN,UP).set_height(1).shift(RIGHT*4+UP*2.5)
        self.play(Create(arr1),Create(tmp1),Create(tmp2),Create(arr3),Create(arr4),
                  Create(lin10),Create(lin11))


        lin12 = Line(start=LEFT,end=RIGHT).set_width(2).shift(LEFT*6.5+UP*3.5)
        lin13 = Line(start=LEFT,end=RIGHT).set_width(5).shift(LEFT*2+UP*3.5)
        arr5 = Arrow(start=LEFT,end=RIGHT).set_width(5.5).shift(RIGHT*(2.75+1.5)+UP*3.5)

        self.play(Create(lin12),Create(lin13),Create(arr5))

        lin13 = Line(LEFT,RIGHT).set_width(2).shift(RIGHT*5.5+UP*0.5)
        arr6 = Arrow(ORIGIN,UP).set_height(1.5).shift(RIGHT*6.5)
        # lin15 = Line(ORIGIN,UP).set_height(0.5).shift(RIGHT*6.5+UP*2.5)
        lin14 = Line(ORIGIN,UP).set_height(3.5).shift(RIGHT*6.5+DOWN*1.75)
        arr7 = Arrow(ORIGIN,RIGHT).set_width(0.5).shift(RIGHT*6.25+DOWN*3)
        self.play(Create(lin13),Create(arr6),Create(lin14),Create(arr7))

        ht = Circle(color = PURPLE).set_width(1).shift(RIGHT*6.5+UP*1.75)
        word2 = MathTex("h_t").set_width(0.5).shift(RIGHT*6.5+UP*1.75)
        self.play(Create(ht),Create(word2))

        self.wait(2)
        # ht_1 = Circle().set_width(1).move_to(lin1,LEFT).shift(LEFT)
        word3 = MathTex("h_{t-1}").set_height(0.5).next_to(lin1,LEFT)
        self.play(Write(word3))

        # ct_1 = Circle().set_width(1).move_to(lin12,LEFT).shift(LEFT)
        word4 = MathTex("c_{t-1}").set_height(0.5).next_to(lin12,LEFT)
        self.play(Write(word4))

        word5 = MathTex("c_t").set_height(0.5).next_to(arr5, RIGHT)
        self.play(Create(word5))
        all1 = Group(*self.mobjects)
        # self.play(ApplyMethod(aim_scope.next_to, target_ij, 0))
        self.play(ApplyMethod(all1.scale, 0.4))

        self.play(ApplyMethod(all1.to_edge, LEFT))
        # ct = Circle().set_width(1).next_to(arr5,RIGHT)

        self.play(Write(word5))
        self.wait(2)

        # 全体变灰
        self.play(ApplyMethod(all1.set_color, GREY))

        #遗忘门
        forget_gate = Group(xt,l1,lin1,lin5,rec4,arr1,mat4)
        self.play(ApplyMethod(forget_gate.set_color_by_gradient, YELLOW, BLUE))
        forget_formula = MathTex("f_t=\sigma(W_f\cdot[h_{t-1},x_t]+b_f)").shift(RIGHT*3.75).set_color_by_gradient(YELLOW, BLUE)
        self.play(Write(forget_formula))
        self.wait(2)
        self.play(FadeOut(forget_formula),ApplyMethod(all1.set_color, GREY))
        self.wait(1)

        # 输入门
        input_gate = Group(xt,word1,l1,lin1,lin2,lin3,lin6,lin7,rec3,rec1,mat1,mat3,tmp2,tmp1,lin9)
        self.play(ApplyMethod(input_gate.set_color_by_gradient,GREEN,ORANGE))
        input_formula = MathTex("i_t=\sigma(W_i\cdot [h_{t-1},x_t]+b_i)").shift(RIGHT*3.75).set_color_by_gradient(GREEN,ORANGE)
        self.play(Write(input_formula))
        self.wait(2)
        self.play(FadeOut(input_formula),ApplyMethod(all1.set_color, GREY))
        self.wait(1)

        # 输出门
        output_gate = Group(xt,word1,l1,lin1,lin2,lin3,lin4,rec2,mat2,lin10,lin11,lin13,lin14,ht,word2,arr7,lin8,
                            eli1,mat9,cir1,mat5,arr3,arr6)
        self.play(ApplyMethod(output_gate.set_color_by_gradient, BLUE,GREEN))
        output_formula = MathTex("o_t=\sigma(W_0\cdot[h_{t-1},x_t]+b_0)").shift(RIGHT*3.75).set_color_by_gradient(BLUE,GREEN)
        self.play(Write(output_formula))
        self.wait(2)
        self.play(FadeOut(output_formula),ApplyMethod(all1.set_color, GREY))
        self.wait(1)

        # 最终输出
        res = Group(ht,word2)
        all1.remove(ht)
        all1.remove(word2)
        self.play(FadeOut(all1),ApplyMethod(res.scale,5))
        # self.play(ApplyMethod(res.set_color, BLUE))
        # self.play(ApplyMethod(res.scale,5))
        self.play(ApplyMethod(res.move_to, [-2,0,0]))
        res_formula = MathTex("h_t=o_t\circ \\tanh(c_t)").shift(RIGHT*3.5).set_color_by_gradient(BLUE)
        self.play(Write(res_formula),ApplyMethod(res.set_color, BLUE))
        self.wait(2)
