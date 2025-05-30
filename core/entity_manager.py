from components.entity.entity_metadata import EntityMetadata

class EntityManager:
    def __init__(self):
        self.entity_list = {}
        self.entity_metadata_list = {}

    def create_entity(self, name: str = ''):
        entity_id = len(self.entity_list)+1

        self.entity_list[entity_id] = entity_id
        self.entity_metadata_list[entity_id] = EntityMetadata(entity_id, name)

        return entity_id

    def get_entity_list(self):
        for entity_item in self.entity_list:
            print(f'{entity_item} - {self.entity_metadata_list[entity_item].name}')