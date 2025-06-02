import pygame
from pygame.surface import Surface
from core.ecs_manager import EcsManager
from components.transform import Transform
from components.sprite import Sprite
from OpenGL.GL import *
from editor.editor_gui import EditorGui

# Basico Opengl,
#            Y (1.0)
#              ↑
#              |
#    (-1.0,1.0)| (1.0,1.0)
# ─────────────┼─────────────→ X (1.0)
#              |
#    (-1.0,-1.0)| (1.0,-1.0)
#              ↓
#            Y (-1.0)


class RenderSystem:
    def __init__(self, ecs_manager: EcsManager, screen: Surface, guiSystem: EditorGui):
        self.ecs_manager = ecs_manager
        self.screen = screen
        self.guiSystem = guiSystem
        pass

    def update(self, delta_time: float):
        glClear(GL_COLOR_BUFFER_BIT)
        entity_list = self.ecs_manager.get_entity_component('Transform', 'Sprite')

        if len(entity_list) == 0:
            print(f'Empty Entity With Transform and Sprite')

        for entity_id in entity_list:
            transform: Transform = self.ecs_manager.get_component(entity_id, "Transform")
            sprite: Sprite = self.ecs_manager.get_component(entity_id, 'Sprite')
            entity_data = self.ecs_manager.get_component_of_entity(entity_id)


            pos_x = transform.pos_x
            pos_y = transform.pos_y

            pos_x_2 = pos_x+transform.scale_x
            pos_y_2 = pos_y

            pos_x_3 = pos_x
            pos_y_3 = pos_y+transform.scale_x

            self.guiSystem.simple_gui('Entity List', [
                f'[{entity_data["name"]}]',
                f'pos_x = {pos_x}', f'pos_y = {pos_y}',
                f'scale_x {transform.scale_x}, scale_y = {transform.scale_x}',
                ''
            ])

            glBegin(GL_TRIANGLES)
            glVertex2f(pos_x, pos_y)
            glVertex2f(pos_x_2, pos_y_2)
            glVertex2f(pos_x_3, pos_y_3)
            glEnd()

            # entity_pos = pygame.Vector2(transform.pos_x, transform.pos_y)

            # if self.screen is not None:
            #     pygame.draw.circle(self.screen, sprite.color, entity_pos, 40)


        