from manim import *

class groupby(Scene):
    def construct(self):
        headers = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"]
        data = [
            [5.1, 3.5, 1.4, 0.2, "setosa"],
            [5.0, 3.6, 1.4, 0.2, "virginica"],
            [4.7, 3.2, 1.3, 0.2, "versicolor"],
            [4.9, 3.0, 1.4, 0.2, "setosa"],
            [4.6, 3.1, 1.5, 0.2, "virginica"],
        ]

        table = Table(
            data,
            col_labels = [MarkupText(f"<b>{h}</b>", font_size=26, font="Iosevka Term") for h in headers],
            element_to_mobject=lambda x: Text(str(x), font_size=22, font = "Iosevka Term")
        ).scale(0.75).move_to(ORIGIN)

        self.play(
            Create(table.get_entries()),
            run_time = 3
        )
        self.wait(2)

        code_text = Text("iris |> groupby(Species)", font_size=22, font="Iosevka Term")
        code_text.next_to(table, UP)
        self.play(AddTextLetterByLetter(code_text), run_time = 3.0)
        self.wait(1.0)

        box_1 = SurroundingRectangle(table.get_columns()[4], color=YELLOW, buff=0.4)

        self.play(
            Create(box_1)
        )

        self.play(
            Uncreate(box_1)
        )

        self.wait(1)

        self.play(
            table.get_rows()[4].animate.shift(
                UP * (table.get_rows()[2].get_center() - table.get_rows()[4].get_center())
            ),
            table.get_rows()[2].animate.shift(
                DOWN * (table.get_rows()[2].get_center() - table.get_rows()[4].get_center())
            )
        )

        