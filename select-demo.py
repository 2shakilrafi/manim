from manim import *

class select_basic(Scene):
    def construct(self):
        headers = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"]
        data = [
            [5.1, 3.5, 1.4, 0.2, "setosa"],
            [4.9, 3.0, 1.4, 0.2, "setosa"],
            [4.7, 3.2, 1.3, 0.2, "versicolor"],
            [4.6, 3.1, 1.5, 0.2, "virginica"],
            [5.0, 3.6, 1.4, 0.2, "virginica"]
        ]

        table = Table(
            data,
            col_labels = [MarkupText(f"<b>{h}</b>", font_size=24, font="Iosevka Etoile") for h in headers],
            element_to_mobject=lambda x: Text(str(x), font_size=22, font = "Iosevka Etoile")
        ).scale(0.75).move_to(ORIGIN)

        self.play(
            Write(table.get_entries()),
            run_time = 3
        )
        self.wait(1)

        species_column = table.get_columns()[4]
        sepal_length_column = table.get_columns()[0]

        code_text = Text("iris |> select(Sepal.Length, Species)", font_size=22, font="Iosevka Etoile")
        code_text.next_to(table, UP)
        self.play(AddTextLetterByLetter(code_text), run_time = 5.0)
        self.wait(1.0)

        box_1 = SurroundingRectangle(sepal_length_column, color=YELLOW, buff=0.4)
        box_2 = SurroundingRectangle(species_column, color=YELLOW, buff=0.4)

        # Show a flash around it
        self.play(
            ShowPassingFlash(
                box_1.copy().set_stroke(width=4),
                time_width=0.3,
                run_time=1.5
            ),
            ShowPassingFlash(
                box_2.copy().set_stroke(width=4),
                time_width=0.3,
                run_time=1.5
            )
        
        )

        self.wait(1.0)

        self.play(
            FadeOut(table.get_columns()[1]),
            FadeOut(table.get_columns()[2]),
            FadeOut(table.get_columns()[3]),
            species_column.animate.shift(LEFT * 4.05),
            sepal_length_column.animate.shift(RIGHT * 4.05),
            run_time = 1.5
        )



class select_minus(Scene):
    def construct(self):
        headers = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"]
        data = [
            [5.1, 3.5, 1.4, 0.2, "setosa"],
            [4.9, 3.0, 1.4, 0.2, "setosa"],
            [4.7, 3.2, 1.3, 0.2, "versicolor"],
            [4.6, 3.1, 1.5, 0.2, "virginica"],
            [5.0, 3.6, 1.4, 0.2, "virginica"]
        ]

        table = Table(
            data,
            col_labels = [MarkupText(f"<b>{h}</b>", font_size=24, font="Iosevka Etoile") for h in headers],
            element_to_mobject=lambda x: Text(str(x), font_size=22, font = "Iosevka Etoile")
        ).scale(0.75).move_to(ORIGIN)

        self.play(
            Write(table.get_entries()),
            run_time = 3
        )
        self.wait(2)

        code_text = Text("iris |> select(-Sepal.Width)", font_size=22, font="Iosevka Etoile")
        code_text.next_to(table, UP)
        self.play(AddTextLetterByLetter(code_text), run_time = 4.0)
        self.wait(1.0)
        sepal_width_column = table.get_columns()[1]

        box_1 = SurroundingRectangle(sepal_width_column, color=RED, buff=0.4)
        self.play(
            FadeToColor(sepal_width_column, color = GRAY)
        )

        self.play(
            ShowPassingFlash(
                box_1.copy().set_stroke(width=4),
                time_width=0.3,
                run_time=1.5
            )
        
        )
    
        dx = table.get_columns()[1].get_center() - table.get_columns()[0].get_center()
        self.play(
            FadeOut(sepal_width_column),
            table.get_columns()[0].animate.shift(RIGHT * dx/2),
            table.get_columns()[2].animate.shift(LEFT * dx/2),
            table.get_columns()[3].animate.shift(LEFT * dx/2),
            table.get_columns()[4].animate.shift(LEFT * dx/2),
            run_time = 1.5
        )


