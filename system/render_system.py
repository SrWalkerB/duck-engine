import pygame
from pygame.surface import Surface
from core.ecs_manager import EcsManager
from components.transform import Transform
from components.sprite import Sprite

class RenderSystem:
    def __init__(self, ecs_manager: EcsManager, screen: Surface):
        self.ecs_manager = ecs_manager
        self.screen = screen
        pass

    def update(self, delta_time: float):
        entity_list = self.ecs_manager.get_entity_component('Transform', 'Sprite')

        for entity_id in entity_list:
            transform: Transform = self.ecs_manager.get_component(entity_id, "Transform")
            sprite: Sprite = self.ecs_manager.get_component(entity_id, 'Sprite')

            entity_pos = pygame.Vector2(transform.pos_x, transform.pos_y)

            pygame.draw.circle(self.screen, sprite.color, entity_pos, 40)


        