from manim import *
class avatarGrupo(Scene):
    def construct(self):
        # Inicio de animacion
        self.camera.background_color ="#94b43b"
        titulo = Text("UNAL", color = WHITE, font = "Ancizar Sans Black", font_size = 200)
        self.play(Write(titulo), run_time = 2.5)

        # Descripcion
        titulo = Text("Grupo de Estudio FEM+CC", color = WHITE, font = "Ancizar Sans", font_size=40).move_to(DOWN * 2)
        self.play(Write(titulo), run_time = 1.7)

        self.wait(2.4)