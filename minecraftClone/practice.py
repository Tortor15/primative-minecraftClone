from ursina import *
class Test_cube(Entity):
    def __init__(self) -> None:
        super().__init__(
            model="cube",
            color = color.white,
            texture = "white_cube",
            rotation = Vec3(45,45,45)
        )
class Test_button(Button):
    def __init__(self) -> None:
        super().__init__(
            parent = scene,
            model = "cube",
            texture = "brick",
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.lime

        )
        def input(self,key):
            if self.hovered:
                if key == 's':
                    print("button pressed")
def update():
    if held_keys["a"]:     
        test_square.x -=4 * time.dt
app = Ursina()
test_square = Entity(model="cube", color= color.red, scale = (1,2), position=(5,4))
sans_texture = load_texture('assets\Sans.png')
sans = Entity(model="quad", texture = sans_texture)
test_cube = Test_button()
app.run()
