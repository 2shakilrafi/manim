from manim import *

class ggplot(Scene):
    def construct(self):
        english_text = Text("She sells seashells by the seashore", font_size=22, font="Iosevka Term")
        self.play(
            AddTextLetterByLetter(english_text)
        )
        self.wait(0.5)

        underline_1 = Line(start=english_text.get_left(), end=english_text.get_left() + RIGHT * 0.52, color=RED).shift(DOWN * 0.2)
        underline_2 = Line(start=english_text.get_left() + RIGHT * 0.8, end=english_text.get_left() + RIGHT * 1.75, color=BLUE).shift(DOWN * 0.2)
        underline_3 = Line(start=english_text.get_left() + RIGHT * 2.0, end=english_text.get_left() + RIGHT * 3.75, color=GREEN).shift(DOWN * 0.2)
        underline_4 = Line(start=english_text.get_left() + RIGHT * 4.0, end=english_text.get_left() + RIGHT * 4.35, color=ORANGE).shift(DOWN * 0.2)
        underline_5 = Line(start=english_text.get_left() + RIGHT * 4.6, end=english_text.get_left() + RIGHT * 5.15, color=PURPLE).shift(DOWN * 0.2)
        underline_6 = Line(start=english_text.get_left() + RIGHT * 5.4, end=english_text.get_left() + RIGHT * 7.0, color=PINK).shift(DOWN * 0.2)

        self.play(
            Write(underline_1),
            Write(underline_2),
            Write(underline_3),
            Write(underline_4),
            Write(underline_5),
            Write(underline_6),
            run_time = 1.0
        )

        subject_label = Text("Subject", font_size=12, font="Iosevka Term", color = RED).next_to(underline_1, DOWN)
        verb_label = Text("Verb", font_size=12, font="Iosevka Term", color = BLUE).next_to(underline_2, DOWN)
        object_label = Text("Object", font_size=12, font="Iosevka Term", color = GREEN).next_to(underline_3, DOWN)
        preposition_label = Text("Preposition", font_size=12, font="Iosevka Term", color = ORANGE).next_to(underline_4, DOWN)
        location_label = Text("Location", font_size=12, font="Iosevka Term", color = PURPLE).next_to(underline_5, UP* 2.1)
        noun_label = Text("Noun", font_size=12, font="Iosevka Term", color = PINK).next_to(underline_6, DOWN)

        self.play(
            Create(subject_label),
            Create(verb_label),
            Create(object_label),
            Create(preposition_label),
            Create(location_label),
            Create(noun_label),
            run_time = 1.0
        )
        self.wait(0.5)

        self.play(
            Uncreate(subject_label),
            Uncreate(verb_label),
            Uncreate(object_label),
            Uncreate(preposition_label),
            Uncreate(location_label),
            Uncreate(noun_label),
            run_time = 0.5
        )

        self.play(
            FadeOut(underline_1),
            FadeOut(underline_2),
            FadeOut(underline_3),
            FadeOut(underline_4),
            FadeOut(underline_5),
            FadeOut(underline_6),
            Uncreate(english_text)
        )
        self.wait(0.25)

        ggplot_text_1 = Text("From the iris dataset",font_size=18, font="Iosevka Term").move_to(ORIGIN + UP * 2)
        ggplot_text_2 = Text("plot Sepal Length vs Sepal width", font_size=18, font="Iosevka Term").next_to(ggplot_text_1, DOWN)
        ggplot_text_3 = Text("using points", font_size=18, font="Iosevka Term").next_to(ggplot_text_2, DOWN)
        ggplot_text_4 = Text("with Minimal Theme", font_size=18, font="Iosevka Term").next_to(ggplot_text_3, DOWN)
        # ggplot_text_5 = Text("with title 'Iris Data', x-label 'Sepal Length' and y-label 'Sepal Width'", font_size=18, font="Iosevka Term").next_to(ggplot_text_4, DOWN)

        self.play(
            AddTextLetterByLetter(ggplot_text_1),
            AddTextLetterByLetter(ggplot_text_2),
            AddTextLetterByLetter(ggplot_text_3),
            AddTextLetterByLetter(ggplot_text_4),
            # AddTextLetterByLetter(ggplot_text_5),
            run_time = 1.5
        )

        self.wait(1.0)

        self.play(
            ggplot_text_1.animate.align_to(LEFT * config.frame_width / 2 + 0.25, LEFT),
            ggplot_text_2.animate.align_to(LEFT * config.frame_width / 2 + 0.25, LEFT),
            ggplot_text_3.animate.align_to(LEFT * config.frame_width / 2 + 0.25, LEFT),
            ggplot_text_4.animate.align_to(LEFT * config.frame_width / 2 + 0.25, LEFT)
        )

        gg_underline_1 = Line(start=ggplot_text_1.get_left(), end=ggplot_text_1.get_right(), color=RED).shift(DOWN * 0.2)
        gg_underline_2 = Line(start=ggplot_text_2.get_left(), end=ggplot_text_2.get_right(), color=BLUE).shift(DOWN * 0.2)
        gg_underline_3 = Line(start=ggplot_text_3.get_left(), end=ggplot_text_3.get_right(), color=GREEN).shift(DOWN * 0.2)
        gg_underline_4 = Line(start=ggplot_text_4.get_left(), end=ggplot_text_4.get_right(), color=ORANGE).shift(DOWN * 0.2)

        self.play(
            Create(gg_underline_1),
            Create(gg_underline_2),
            Create(gg_underline_3),
            Create(gg_underline_4)
        )

        data_label = Text("Data", font_size=12, font="Iosevka Term", color = RED).next_to(gg_underline_1, RIGHT)
        aesthetics_label = Text("Aesthetics", font_size=12, font="Iosevka Term", color = BLUE).next_to(gg_underline_2, RIGHT)
        geometry_label = Text("Geometry", font_size=12, font="Iosevka Term", color = GREEN).next_to(gg_underline_3, RIGHT)
        theme_label = Text("Theme", font_size=12, font="Iosevka Term", color = ORANGE).next_to(gg_underline_4, RIGHT)

        self.play(
            Create(data_label),
            Create(aesthetics_label),
            Create(geometry_label),
            Create(theme_label)
        )
        self.wait(1.0)

        r_code_1 = Text("iris |>",font_size=18, font="Iosevka Term", color = RED).move_to(ORIGIN + UP * 2 + RIGHT * 0.5)
        r_code_2 = Text("ggplot(aes(Sepal.Length, Sepal.Width)) + ",font_size=18, font="Iosevka Term", color = BLUE).next_to(r_code_1, DOWN).align_to(r_code_1, LEFT)
        r_code_3 = Text("geom_point() + ",font_size=18, font="Iosevka Term", color = GREEN).next_to(r_code_2, DOWN).align_to(r_code_2, LEFT)
        r_code_4 = Text("theme_minimal()",font_size=18, font="Iosevka Term", color = ORANGE).next_to(r_code_3, DOWN).align_to(r_code_3, LEFT)

        self.play(
            AddTextLetterByLetter(r_code_1)
        )
        self.play(
            AddTextLetterByLetter(r_code_2)
        )
        self.play(
            AddTextLetterByLetter(r_code_3)
        )
        self.play(
            AddTextLetterByLetter(r_code_4)
        )

        self.wait(0.25)