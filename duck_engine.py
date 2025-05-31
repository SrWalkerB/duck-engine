import pygame
from core.ecs_manager import EcsManager  
from components.available_components import AvailableComponents

class DuckEngine:
    WIDTH_SCREEN = 1280
    HEIGHT_SCREEN = 720
    DELTA_TIME = 0
    running = True
    component_list = []

    def __init__(self):
        self.running = True
        self.ecs_manager = EcsManager()
        self.available_components = AvailableComponents()

        pass

    def start_engine(self):
        pass
        
    def start_game(self):
        screen = pygame.display.set_mode((self.WIDTH_SCREEN, self.HEIGHT_SCREEN))
        clock = pygame.time.Clock()
        running = True

        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

        self.component_list.append(player_pos)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("purple")

            pygame.draw.circle(screen, "red", player_pos, 40)

            keys = pygame.key.get_pressed()
            mouse_event_pressed = pygame.mouse.get_pressed()

            if keys[pygame.K_w]:
                player_pos.y -= 300 * self.DELTA_TIME
            if keys[pygame.K_s]:
                player_pos.y += 300 * self.DELTA_TIME

            if mouse_event_pressed[0] is True:
                mouse = pygame.mouse.get_pos()
                print(f'clic {mouse_event_pressed} - {mouse}')

            pygame.display.flip()

            self.DELTA_TIME = clock.tick(60) / 1000

        self.quit()

    def quit(self):
        print('Finish Engine')
        pygame.quit()