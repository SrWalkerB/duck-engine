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

    def simple_gui(self, title: str, value: str):
        imgui.begin(title)
        imgui.text(value)
        imgui.end()