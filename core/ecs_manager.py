from game.entity_metadata import EntityMetadata
from components.transform import Transform

class EcsManager:
    def __init__(self):
        self.entity_list = {}
        self.entity_metadata_list = {}
        self.component_list = {
            "Transform"
        }
        
    def create_entity(self, name: str = '', tag: str = ''):
        entity_id = len(self.entity_list)+1

        self.entity_list[entity_id] = entity_id
        self.entity_metadata_list[entity_id] = EntityMetadata(entity_id, name, tag)
        self.component_list["Transform"][entity_id] = Transform()

        return entity_id

    def get_entity_list(self):
        for entity_item in self.entity_list:
            print(f'{entity_item} - {self.entity_metadata_list[entity_item].name}')