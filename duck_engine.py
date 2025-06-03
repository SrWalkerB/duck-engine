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
    # background_engine = [0.1, 0.1, 0.1, 1.0]

    screen: pygame.Surface
    clock: pygame.time.Clock

    editor_gui: EditorGui

    def __init__(self):
        self.running = True
        self.ecs_manager = EcsManager()
        self.available_components = AvailableComponents()
        self.editor_gui = EditorGui(self.ecs_manager)
        
        self.start_engine()

    def start_engine(self):
        self.screen = pygame.display.set_mode((self.WIDTH_SCREEN, self.HEIGHT_SCREEN), pygame.OPENGL | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        
        self.editor_gui.renderer = PygameRenderer()
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
                self.editor_gui.renderer.process_event(event)


            self.editor_gui.process_init_frame()
            self.ecs_manager.queue_entity_creation()

            render_system.process(self.DELTA_TIME)
            self.editor_gui.process()

            pygame.display.flip()

            self.DELTA_TIME = self.clock.tick(75) / 1000

        self.quit()

    def start_game(self):
        self.start_main_loop()

    def quit(self):
        self.editor_gui.quit()
        pygame.quit()