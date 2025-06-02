import pygame
import imgui

from OpenGL.GL import *
from core.ecs_manager import EcsManager  
from components.available_components import AvailableComponents
from system.render_system import RenderSystem
from imgui.integrations.pygame import PygameRenderer
from editor.editor_gui import EditorGui

class DuckEngine:
    game_title: str = 'Duck Engine'
    WIDTH_SCREEN = 1280
    HEIGHT_SCREEN = 720

    DELTA_TIME = 0
    running = True
    component_list = []
    background_engine = [0.1, 0.1, 0.1, 1.0]

    screen: pygame.Surface
    clock: pygame.time.Clock

    imgui_renderer: PygameRenderer
    editor_gui: EditorGui

    def __init__(self):
        self.running = True
        self.ecs_manager = EcsManager()
        self.available_components = AvailableComponents()
        self.editor_gui = EditorGui()
        
        self.start_engine()

    def start_engine(self):
        self.screen = pygame.display.set_mode((self.WIDTH_SCREEN, self.HEIGHT_SCREEN), pygame.OPENGL | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        
        imgui.create_context()
        self.imgui_renderer = PygameRenderer()
        pygame.display.set_caption(self.game_title)

        pass

    def start_main_loop(self):
        render_system = RenderSystem(self.ecs_manager, self.screen, self.editor_gui)
        width, height = pygame.display.get_surface().get_size()

        imgui.get_io().display_size = (width, height)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.imgui_renderer.process_event(event)


            self.render_gui(self.background_engine)
            render_system.update(self.DELTA_TIME)


            imgui.render()
            self.imgui_renderer.render(imgui.get_draw_data())

            pygame.display.flip()

            self.DELTA_TIME = self.clock.tick(75) / 1000

        self.quit()

    def render_gui(self, background_color):
        imgui.new_frame()

        imgui.begin("Debug Mode: ")
        imgui.text(f'FPS: {int(self.clock.get_fps())}')

        imgui.text('Background Color')
        _,background_color = imgui.color_edit4("Color", *background_color)

        imgui.end()

        self.editor_gui.menu_bar()
        self.background_engine = background_color
        glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])

    def start_game(self):
        self.start_main_loop()

    def quit(self):
        imgui.end_frame()
        pygame.quit()