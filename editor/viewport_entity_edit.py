from core.ecs_manager import EcsManager

class ViewPortEntityEditorEditManager:
    def __init__(self, ecs_manager: EcsManager):
        self.ecs_manager = ecs_manager
        pass

    def process(self, mouse_x, mouse_y):
        entity_list = self.ecs_manager.get_entity_component('Transform')

        # for entity in entity_list:
        #     print(entity)
            