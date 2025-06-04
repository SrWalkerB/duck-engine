import imgui
from imgui.integrations.pygame import PygameRenderer
from OpenGL.GL import *
from core.ecs_manager import EcsManager
from components.transform import Transform
from components.available_components import AvailableComponents

class EditorGui:
    renderer: PygameRenderer
    imgui: imgui

    entity_id_inspect = ''

    # Input Modal
    input_text = ''

    def __init__(self, ecs_manager: EcsManager):
        imgui.create_context()
        self.on_active_modal = {
            "menu": "",
            "sub_item": "",
            "onClick": False
        }

        self.ecs_manager = ecs_manager
        
    def process_init_frame(self):
        imgui.new_frame()

    def process(self):
        self.menu_bar()
        self.inspector()

        if self.on_active_modal["onClick"] == True:
            imgui.open_popup("Modal")
            self.on_active_modal["onClick"] = False
            self.input_text = ''

        if imgui.begin_popup_modal("Modal", flags=imgui.WINDOW_ALWAYS_AUTO_RESIZE)[0]:
            imgui.text("Entity Name: ")

            _, self.input_text = imgui.input_text('', self.input_text, 266)

            imgui.spacing()
            if imgui.button("Cancelar"):
                imgui.close_current_popup()

            imgui.same_line()
            
            if imgui.button("OK"):
                self.ecs_manager.add_entity_creation(self.input_text)
                imgui.close_current_popup()

            imgui.end_popup()

        imgui.render()
        self.renderer.render(imgui.get_draw_data())

    def menu_bar(self):
        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File"):
                clicked, _ = imgui.menu_item("New Scene")
                imgui.menu_item("Load Scene")
                imgui.menu_item("Save")

                if clicked:
                    glClearColor(0.2, 0.2, 0.3, 1)

                imgui.end_menu()

            if imgui.begin_menu("GameObject"):
                clicked, _ = imgui.menu_item("New Entity")

                if clicked:
                    self.on_active_modal["onClick"] = True

                imgui.end_menu()

            if imgui.begin_menu("Components"):
                available_components = AvailableComponents()
        
                available_components_list = available_components.get_component_list()

                for component in available_components_list:
                    imgui.menu_item(component)

                imgui.end_menu()


            imgui.end_main_menu_bar()


        return self.on_active_modal

    def simple_gui(self, title: str, value_list: str):
        imgui.begin(title)

        for value in value_list:
            imgui.text(value)

        imgui.end()

    def entity_list(self):
        imgui.begin('Entity List', flags=(imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_RESIZE))
        
        entity_list = self.ecs_manager.get_entity_list()

        for entity_id in entity_list:
            entity_data = self.ecs_manager.get_component_of_entity(entity_id)
            imgui.text(f'{entity_data["name"]} ({entity_data["entity_id"]})')
            
            if imgui.is_item_clicked():
                self.entity_id_inspect = entity_id
                
        imgui.end()

    def inspector(self):
        if self.entity_id_inspect == '':
            return

        entity_data = self.ecs_manager.get_component_of_entity(self.entity_id_inspect)

        _, visible = imgui.begin('Inspector', closable=True)
        
        imgui.text(f'{entity_data["name"]} ({entity_data["entity_id"]})')
        imgui.separator()

        if visible is False:
            self.entity_id_inspect = ''

        for component in entity_data['components']:
            imgui.text(f'{component}')

            if entity_data['components'][component] is not None:
                if component == 'Transform':
                    transform: Transform = entity_data['components'][component]
                    imgui.text(f'Pos X = {transform.pos_x}')
                    imgui.text(f'Pos Y = {transform.pos_y}')
                    imgui.text(f'Scale X = {transform.scale_x}')
                    imgui.text(f'Scale Y = {transform.scale_y}')
            else:
                imgui.text(f'Empty')
            
            
            imgui.separator()

        imgui.end()

    def background_color_gui(self, background_color):
        imgui.text('Background Color')
        _,background_color = imgui.color_edit4("Color", *background_color)

        return background_color
    
    def quit(self):
        imgui.end_frame()
    

