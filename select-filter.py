from manim import *

class select_filter(Scene):
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
            col_labels=[MarkupText(f"<b>{h}</b>", font_size=26, font="Iosevka Term") for h in headers],
            element_to_mobject=lambda x: Text(str(x), font_size=22, font="Iosevka Term")
        ).scale(0.75).move_to(ORIGIN)

        self.play(Create(table.get_entries()), run_time=2)
        self.wait(1)

        sepal_width_col = table.get_columns()[1]
        species_col = table.get_columns()[4]

        code_text = Text("iris |> select(Sepal.Width, Species) |> filter(Sepal.Width > 3.1)", font_size=22, font="Iosevka Term")
        code_text.next_to(table, UP)
        self.play(AddTextLetterByLetter(code_text), run_time=5.0)
        self.wait(1.0)

        box_1 = SurroundingRectangle(sepal_width_col, color=YELLOW, buff=0.4)
        box_2 = SurroundingRectangle(species_col, color=YELLOW, buff=0.4)

        underline_1 = Line(start=code_text.get_left() + RIGHT * 1.6, end=code_text.get_left() + RIGHT * 7.1, color=RED).shift(DOWN * 0.2)
        underline_2 = Line(start=code_text.get_left() + RIGHT * 8.0, end=code_text.get_left() + RIGHT * 12.9, color=RED).shift(DOWN * 0.2)

        self.wait(1.0)

        # Store rows before fading out any
        row_2 = table.get_rows()[2]
        row_3 = table.get_rows()[3]
        row_4 = table.get_rows()[4]  # for animation into empty spots

        self.play(
            Create(underline_1),
            table.get_columns()[0].animate.shift(DOWN * 20),
            table.get_columns()[2].animate.shift(DOWN * 20),
            table.get_columns()[3].animate.shift(DOWN * 20),
            sepal_width_col.animate.shift(RIGHT * 1.3),
            species_col.animate.shift(LEFT * 4.1),
            run_time=1.5
        )

        # Filter condition: Sepal.Width > 3.1 → keep only rows 1 and 4 (indexes 0-based: rows[1] and rows[4])
        row_1 = table.get_rows()[1]
        row_2 = table.get_rows()[2]
        row_3 = table.get_rows()[3]
        row_4 = table.get_rows()[4]
        row_5 = table.get_rows()[5]

        self.wait(1)
        # Filter condition: Sepal.Width > 3.1 → keep only rows 1 and 3
        self.play(
            Create(underline_2),
            FadeOut(row_2),
            FadeOut(row_4),
            row_3.animate.shift(UP * (table.get_rows()[2].get_center() - table.get_rows()[3].get_center())),
            row_5.animate.shift(UP * (table.get_rows()[3].get_center() - table.get_rows()[5].get_center())),
            run_time = 1.5
        )
        self.wait()

class filter_select(Scene):
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
            col_labels=[MarkupText(f"<b>{h}</b>", font_size=26, font="Iosevka Term") for h in headers],
            element_to_mobject=lambda x: Text(str(x), font_size=22, font="Iosevka Term")
        ).scale(0.75).move_to(ORIGIN)

        self.play(Create(table.get_entries()), run_time=2)
        self.wait(1)

        sepal_width_col = table.get_columns()[1]
        species_col = table.get_columns()[4]

        code_text = Text("iris |> filter(Sepal.Width > 3.1) |> select(Sepal.Width, Species)", font_size=22, font="Iosevka Term")
        code_text.next_to(table, UP)
        self.play(AddTextLetterByLetter(code_text), run_time=5.0)
        self.wait(1.0)


        underline_1 = Line(start=code_text.get_left() + RIGHT * 1.6, end=code_text.get_left() + RIGHT * 6.5, color=RED).shift(DOWN * 0.2)
        underline_2 = Line(start=code_text.get_left() + RIGHT * 7.4, end=code_text.get_left() + RIGHT * 12.9, color=RED).shift(DOWN * 0.2)

        row_1 = table.get_rows()[1]
        row_2 = table.get_rows()[2]
        row_3 = table.get_rows()[3]
        row_4 = table.get_rows()[4]
        row_5 = table.get_rows()[5]

        self.wait(1)
        # Filter condition: Sepal.Width > 3.1 → keep only rows 1 and 3
        self.play(
            Create(underline_1),
            FadeOut(row_2),
            FadeOut(row_4),
            row_3.animate.shift(UP * (table.get_rows()[2].get_center() - table.get_rows()[3].get_center())),
            row_5.animate.shift(UP * (table.get_rows()[3].get_center() - table.get_rows()[5].get_center())),
            run_time = 1.5
        )
        self.wait()
        
        
        
        
        
        
        
        self.wait(1.0)

        self.play(
            Create(underline_2),
            table.get_columns()[0].animate.shift(DOWN * 20),
            table.get_columns()[2].animate.shift(DOWN * 20),
            table.get_columns()[3].animate.shift(DOWN * 20),
            sepal_width_col.animate.shift(RIGHT * 1.3),
            species_col.animate.shift(LEFT * 4.1),
            run_time=1.5
        )

        # Filter condition: Sepal.Width > 3.1 → keep only rows 1 and 4 (indexes 0-based: rows[1] and rows[4])
        