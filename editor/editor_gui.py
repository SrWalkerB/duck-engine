import imgui
from imgui.integrations.pygame import PygameRenderer

class EditorGui:
    imgui_renderer: PygameRenderer
    imgui: imgui

    def __init__(self):
        pass

    def menu_bar(self):
        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("Scene"):
                clicked, _ = imgui.menu_item("New")

                if clicked:
                    glClearColor(0.2, 0.2, 0.3, 1)
                    print("new")

                imgui.end_menu()
            imgui.end_main_menu_bar()

    def simple_gui(self, title: str, value_list: str):
        imgui.begin(title)

        for value in value_list:
            imgui.text(value)

        imgui.end()

    def slide_gui(self, current_value):
        imgui.begin('Slider')

        _, value = imgui.slider_float('Slider', current_value, 0.0, 1.0)

        imgui.end()
        return value
