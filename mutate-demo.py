from manim import *

class mutate(Scene):
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
            col_labels = [MarkupText(f"<b>{h}</b>", font_size=26, font="JetBrains Mono") for h in headers],
            element_to_mobject=lambda x: Text(str(x), font_size=22, font = "JetBrains Mono")
        ).scale(0.75).move_to(ORIGIN)

        self.play(
            Write(table.get_entries()),
            run_time = 5
        )
        self.wait(2)

        code_text = Text("iris |> mutate(Petal.Area = Petal.Length * Petal.Width)", font_size=22, font="JetBrains Mono")
        code_text.next_to(table, UP)
        self.play(AddTextLetterByLetter(code_text), run_time = 5.0)
        self.wait(1.0)
        
        self.wait(1.0)

        box_1 = SurroundingRectangle(table.get_columns()[2], color=YELLOW, buff=0.4)
        box_2 = SurroundingRectangle(table.get_columns()[3], color=YELLOW, buff=0.4)


        self.play(
            ShowPassingFlash(
                box_1.copy().set_stroke(width=4),
                time_width=1,
                run_time=2.0
            ),
            ShowPassingFlash(
                box_2.copy().set_stroke(width=4),
                time_width=1,
                run_time=2.0
            )
        )
        dx = ORIGIN - table.get_columns()[4].get_center()
        self.play(
            table.get_entries().animate.shift(RIGHT * dx),
            run_time = 1.5
        )

        old = table.get_entries()
        rows = [
            ["0.28"],
            ["0.28"],
            ["0.26"],
            ["0.30"],
            ["0.28"],
        ]
        new_table = Table(
            rows,
            # Render the header separately as bold
            col_labels=[
                MarkupText("<b>Petal.Area</b>", font="JetBrains Mono", font_size=22)
            ],
            element_to_mobject=lambda x: Text(str(x), font="JetBrains Mono", font_size=22),
        ).scale(0.77).next_to(old, RIGHT, buff=0.5)


        # 1. Grab the 3rd column (0-indexed, so index 2)
        source_col_1 = table.get_columns()[2]
        source_col_2 = table.get_columns()[3]

# 2. Make a copy and shove it over next to `table`
        col_clone_1 = source_col_1.copy()
        col_clone_2 = source_col_2.copy()
        self.add(col_clone_1)  # immediately add it to the scene
        self.add(col_clone_2)

# 3. Grab the only column in your new table (index 0)
        target_col = new_table.get_columns()[0]

        self.play(
                col_clone_1.animate.shift(RIGHT * (target_col.get_center() - source_col_1.get_center())).set_rate_func(smooth),
                col_clone_2.animate.shift(RIGHT * (target_col.get_center() - source_col_2.get_center())).set_rate_func(smooth),
                ReplacementTransform(col_clone_1, target_col),
                ReplacementTransform(col_clone_2, target_col),
        )

class mutate_ratio(Scene):
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
            col_labels = [MarkupText(f"<b>{h}</b>", font_size=26, font="JetBrains Mono") for h in headers],
            element_to_mobject=lambda x: Text(str(x), font_size=22, font = "JetBrains Mono")
        ).scale(0.75).move_to(ORIGIN)

        self.play(
            Write(table.get_entries()),
            run_time = 5
        )
        self.wait(2)

        code_text_2 = Text("iris |> mutate(Petal.Ratio = Petal.Length / Petal.Width)", font_size=22, font="JetBrains Mono")
        code_text.next_to(table, UP)
        self.play(RemoveTextLetterByLetter(code_text), run_time = 5.0)
        self.play(AddTextLetterByLetter(code_text_2), run_time = 5.0)
        self.wait(1.0)
        
        self.wait(1.0)

        box_1 = SurroundingRectangle(table.get_columns()[2], color=YELLOW, buff=0.4)
        box_2 = SurroundingRectangle(table.get_columns()[3], color=YELLOW, buff=0.4)


        self.play(
            ShowPassingFlash(
                box_1.copy().set_stroke(width=4),
                time_width=0.3,
                run_time=2.0
            ),
            ShowPassingFlash(
                box_2.copy().set_stroke(width=4),
                time_width=0.3,
                run_time=2.0
            )
        )
        dx = ORIGIN - table.get_columns()[4].get_center()
        self.play(
            table.get_entries().animate.shift(RIGHT * dx),
            run_time = 1.5
        )

        old = table.get_entries()
        rows = [
            ["0.28"],
            ["0.28"],
            ["0.26"],
            ["0.30"],
            ["0.28"],
        ]
        new_table = Table(
            rows,
            # Render the header separately as bold
            col_labels=[
                MarkupText("<b>Petal.Ratio</b>", font="JetBrains Mono", font_size=22)
            ],
            element_to_mobject=lambda x: Text(str(x), font="JetBrains Mono", font_size=22),
        ).scale(0.77).next_to(old, RIGHT, buff=0.5)


        # 1. Grab the 3rd column (0-indexed, so index 2)
        source_col_1 = table.get_columns()[2]
        source_col_2 = table.get_columns()[3]

# 2. Make a copy and shove it over next to `table`
        col_clone_1 = source_col_1.copy()
        col_clone_2 = source_col_2.copy()
        self.add(col_clone_1)  # immediately add it to the scene
        self.add(col_clone_2)

# 3. Grab the only column in your new table (index 0)
        target_col = new_table.get_columns()[0]

        self.play(
                col_clone_1.animate.shift(RIGHT * (target_col.get_center() - source_col_1.get_center())).set_rate_func(smooth),
                col_clone_2.animate.shift(RIGHT * (target_col.get_center() - source_col_2.get_center())).set_rate_func(smooth),
                ReplacementTransform(col_clone_1, target_col),
                ReplacementTransform(col_clone_2, target_col),
        )



        
