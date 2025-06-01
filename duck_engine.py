import pygame
import imgui

from OpenGL.GL import *
from core.ecs_manager import EcsManager  
from components.available_components import AvailableComponents
from system.render_system import RenderSystem
from imgui.integrations.pygame import PygameRenderer

class DuckEngine:
    WIDTH_SCREEN = 1280
    HEIGHT_SCREEN = 720
    DELTA_TIME = 0
    running = True
    component_list = []
    screen: pygame.Surface
    clock: pygame.time.Clock
    game_title: str = 'Duck Engine'
    imgui_renderer: PygameRenderer

    def __init__(self):
        self.running = True
        self.ecs_manager = EcsManager()
        self.available_components = AvailableComponents()
        
        self.start_engine()

    def start_engine(self):
        self.screen = pygame.display.set_mode((self.WIDTH_SCREEN, self.HEIGHT_SCREEN), pygame.OPENGL | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        
        imgui.create_context()
        self.imgui_renderer = PygameRenderer()
        pygame.display.set_caption(self.game_title)

        pass

    def start_game(self):
        render_system = RenderSystem(self.ecs_manager, self.screen)
        width, height = pygame.display.get_surface().get_size()

        print(width)
        imgui.get_io().display_size = (width, height)
        background_color = [0.1, 0.1, 0.1, 1.0]

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.imgui_renderer.process_event(event)


            imgui.new_frame()
            imgui.begin("Debug Mode: ")
            imgui.text(f'FPS: {int(self.clock.get_fps())}')

            imgui.text('Background Color')
            _,background_color = imgui.color_edit4("Color", *background_color)


            # imgui.color_button("ColorPreview", *background_color, imgui.COLOR_BUTTON, 50, 50)
            imgui.end()

            if imgui.begin_main_menu_bar():
                if imgui.begin_menu("Scene"):
                    clicked, _ = imgui.menu_item("New")

                    if clicked:
                        glClearColor(0.2, 0.2, 0.3, 1)
                        print("new")

                    imgui.end_menu()
                imgui.end_main_menu_bar()

            render_system.update(self.DELTA_TIME)

            glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])

            imgui.render()
            self.imgui_renderer.render(imgui.get_draw_data())

            pygame.display.flip()

            self.DELTA_TIME = self.clock.tick(75) / 1000

        self.quit()

    def quit(self):
        imgui.end_frame()
        pygame.quit()