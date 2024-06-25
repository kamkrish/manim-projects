from manim import *

#INTRODUCTION
class rungekutta(ThreeDScene):
    def construct(self):
        Introline = Line([-6,0,0], [6,0,0])
        IntroTitle = Text("Solving Differential Equations using Runge Kutta", font_size = 30).next_to(Introline,UP)
        self.add(Introline, IntroTitle)
        self.wait(2)
        self.play(FadeOut(Introline,IntroTitle))
        self.wait (2)

        ODEtext1 = Text("Differential Equations")
        ODEtext2 = Text("Rate of change").next_to(ODEtext1,DOWN)
        height = 3
        radius = 1
        resolution = (10,50)
        cylinder = Surface(
                lambda u, v: np.array([
                    radius * np.cos(u),
                    radius * np.sin(u),
                    v * height
                ]),
                u_range = (0, 2*PI),
                v_range = (0, 1),
                resolution = resolution
            )
        ODEtext3 = MathTex(
                "\\frac{du}{dx} = \\alpha\\frac{d^2u}{dx^2}").next_to(cylinder,DOWN)
        framebox1 = SurroundingRectangle(ODEtext3[0], buff = .1)
        ODEtext4 = MathTex("u(x,t) = X(x)T(t)")
        ODEtext5 = MathTex("T(t) = Ce^{-\\alpha\\lambda t}").next_to(ODEtext4,DOWN)
        ODEtext6 = MathTex("X(x) = Asin(\\sqrt{\\lambda}x) + Bcos(\\sqrt{\\lambda}x)").next_to(ODEtext5,DOWN)
        ODEarrow = Arrow(3*UP, ORIGIN)
        ODEtext7 = Text("or solve it numerically")
        
        self.add(ODEtext1)
        self.wait(5)
        self.add(ODEtext2)
        self.wait(5)
        self.play(FadeOut(ODEtext1, ODEtext2))
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(cylinder))
        self.wait(2)
        self.play(ApplyMethod(cylinder.set_color, RED),
                  run_time = 10
            )
        self.move_camera(phi = 0, theta = -90 * DEGREES)
        self.play(Write(ODEtext3))
        self.wait()
        self.play(Create(framebox1))
        self.wait(5)
        self.play(FadeOut(cylinder,ODEtext3,framebox1))
        self.wait(5)
        self.play(Write(ODEtext4))
        self.play(ODEtext4.animate.shift(3*UP))
        self.wait(5)
        self.play(Create(ODEarrow))
        self.play(Write(ODEtext5))
        self.wait(5)
        self.play(Write(ODEtext6))
        self.wait(5)
        self.play(FadeOut(ODEtext4,ODEtext5,ODEtext6,ODEarrow))
        self.wait(2)
        self.play(Write(ODEtext7))
        self.play(FadeOut(ODEtext7))
        
#Analytic Solution of Differential Equation 1st order
        RKtext1 = Text("Why Runge-Kutta ?")
        RKtext2 = MathTex("\\frac{dy}{dx} = -2x; y(0) = 1; y(1) = ?") 
        RKtext3 = Text("Let's solve anaytically first").next_to(RKtext2, DOWN)
        RKtext4 = MathTex("\\int_{}^{}dy = \\int_{}^{} -2x dx")
        RKtext5 = MathTex("y = \\frac{-2x^{2}}{2} + C")
        RKtext6 = MathTex("y = -x^2 + C")
        RKtext7 = MathTex("1 = -(0)^2 + C")
        RKtext8 = MathTex("C = 1")
        RKtext9 = MathTex("y = -x^2 + 1")
        RKtext10 = MathTex("y = -(1)^2 + 1")
        RKtext11 = MathTex("y(1) = 0 ")

        self.add(RKtext1)
        self.wait(2)
        self.play(FadeOut(RKtext1))
        self.play(Write(RKtext2))
        self.wait(2)
        self.play(Write(RKtext3))
        self.wait(2)
        self.play(FadeOut(RKtext3))
        self.play(TransformMatchingShapes(RKtext2, RKtext4))
        self.wait(1)
        self.play(TransformMatchingShapes(RKtext4, RKtext5))
        self.wait(1)
        self.play(TransformMatchingShapes(RKtext5, RKtext6))
        self.wait(1)
        self.play(TransformMatchingShapes(RKtext6, RKtext7))
        self.wait(1)
        self.play(TransformMatchingShapes(RKtext7, RKtext8))
        self.wait(1)
        self.play(TransformMatchingShapes(RKtext8, RKtext9))
        self.wait(1)
        self.play(TransformMatchingShapes(RKtext9, RKtext10))
        self.wait(1)
        self.play(TransformMatchingShapes(RKtext10, RKtext11))
        self.wait(5)

#RK4 of the Differential Equation 1st order
        def f(x, y):
         return -2 * x
        #initial Values
        x0 = 0
        y0 = 1
        x_values = [x0]
        y_values = [y0]
        h = 0.2
        #RKvar1 = Variable()
        #self.play(Write(RKvar1))
        #calculation
        x = x0
        y = y0
        while x <= 1:
         k1 = h * f(x, y)
         k2 = h * f(x + h/2, y + k1/2)
         k3 = h * f(x + h/2, y + k2/2)
         k4 = h * f(x + h, y + k3)
         y += (k1 + 2*k2 + 2*k3 + k4) / 6
         x += h
         x_values.append(x)
         y_values.append(y)

        
