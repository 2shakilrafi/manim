from manim import *

class summarize(Scene):
    def construct(self):
        headers = ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"]
        data = [
            [5.1, 3.5, 1.4, 0.2, "setosa"],
            [5.0, 3.6, 1.4, 0.3, "virginica"],
            [4.7, 3.2, 1.3, 0.2, "versicolor"],
            [4.9, 3.0, 1.4, 0.1, "setosa"],
            [4.6, 3.1, 1.5, 0.4, "virginica"],
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
        self.wait(1)

        code_text = Text("iris |> group_by(Species) |> summarize(mean(Petal.Width))", font_size=22, font="Iosevka Term")
        code_text.next_to(table, UP)
        self.play(AddTextLetterByLetter(code_text), run_time = 3.0)
        self.wait(1.0)

        box_1 = SurroundingRectangle(table.get_columns()[4], color=YELLOW, buff=0.4)

        self.play(
            Create(box_1)
        )

        self.wait(0.5)

        self.play(
            Uncreate(box_1)
        )

        self.wait(0.5)

        self.play(
            table.get_rows()[4].animate.shift(
                UP * (table.get_rows()[2].get_center() - table.get_rows()[4].get_center())
            ),
            table.get_rows()[2].animate.shift(
                DOWN * (table.get_rows()[2].get_center() - table.get_rows()[4].get_center())
            )
        )

        column_1 = table.get_columns()[0]
        column_2 = table.get_columns()[1]
        column_3 = table.get_columns()[2]
        column_4 = table.get_columns()[3]
        column_5 = table.get_columns()[4]

        row_1 = table.get_rows()[1]
        row_2 = table.get_rows()[2]
        row_3 = table.get_rows()[3]
        row_4 = table.get_rows()[4]
        row_5 = table.get_rows()[5]

        self.play(
            column_1.animate.shift(DOWN * 20),
            column_2.animate.shift(DOWN * 20),
            column_3.animate.shift(DOWN * 20)
        )
        
        self.play(
            column_5.animate.shift(
                LEFT * (
                    column_5.get_width() + ORIGIN + (column_5.get_center() - ORIGIN - 0.5)
                )
            ),
            column_4.animate.shift(
                LEFT * 1
                )
        )

        species_label = table.get_columns()[3][0]
        new_label = MarkupText("<b>mean(Petal.Width)</b>", font_size=26, font="Iosevka Term").move_to(species_label).scale(0.75)

        self.play(
            Transform(species_label, new_label),
            row_2.animate.shift(UP * (row_1.get_center() - row_2.get_center())),
            row_3.animate.shift(UP * (row_3.get_center() - row_2.get_center())),
            row_4.animate.shift(UP * (row_3.get_center() - row_4.get_center())),
            row_5.animate.shift(UP * (row_3.get_center() - row_5.get_center())),      
        )

class groupby_summarize(Scene):
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
        self.wait(1)

        code_text = Text("iris |> groupby(Species) |> mean(Petal.Width)", font_size=22, font="Iosevka Term")
        code_text.next_to(table, UP)
        self.play(AddTextLetterByLetter(code_text), run_time = 3.0)
        self.wait(1.0)

        box_1 = SurroundingRectangle(table.get_columns()[4], color=YELLOW, buff=0.4)

        self.play(
            Create(box_1)
        )

        self.wait(0.5)

        self.play(
            Uncreate(box_1)
        )

        self.wait(0.5)

        self.play(
            table.get_rows()[4].animate.shift(
                UP * (table.get_rows()[2].get_center() - table.get_rows()[4].get_center())
            ),
            table.get_rows()[2].animate.shift(
                DOWN * (table.get_rows()[2].get_center() - table.get_rows()[4].get_center())
            )
        )

        column_1 = table.get_columns()[0]
        column_2 = table.get_columns()[1]
        column_3 = table.get_columns()[2]
        column_4 = table.get_columns()[3]
        column_5 = table.get_columns()[4]

        row_1 = table.get_rows()[1]
        row_2 = table.get_rows()[2]
        row_3 = table.get_rows()[3]
        row_4 = table.get_rows()[4]
        row_5 = table.get_rows()[5]

        self.play(
            column_1.animate.shift(DOWN * 20),
            column_2.animate.shift(DOWN * 20),
            column_3.animate.shift(DOWN * 20)
        )
        
        self.play(
            column_5.animate.shift(
                LEFT * (
                    column_5.get_width() + ORIGIN + (column_5.get_center() - ORIGIN - 0.5)
                )
            ),
            column_4.animate.shift(
                LEFT * 1
                )
        )

        self.play(
            FadeOut(table.get_entries()[0,4])
        )