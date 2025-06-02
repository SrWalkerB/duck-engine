from game.entity_metadata import EntityMetadata
from components.transform import Transform
from components.available_components import AvailableComponents

class EcsManager:
    def __init__(self):
        self.entity_list: dict[int, int] = {}
        self.entity_metadata_list: dict[int, EntityMetadata] = {}
        self.component_list = {}
        available_components = AvailableComponents()
        
        available_components_list = available_components.get_component_list()

        for component in available_components_list:
            self.component_list[component] = {}

    def create_entity(self, name: str = '', tag: str = ''):
        entity_id = len(self.entity_list)+1

        self.entity_list[entity_id] = entity_id
        self.entity_metadata_list[entity_id] = EntityMetadata(entity_id, name, tag)
        self.component_list["Transform"][entity_id] = Transform()

        return entity_id

    def get_entity_list(self):
        for entity_item in self.entity_list:
            print(f'{entity_item} - {self.entity_metadata_list[entity_item].name}')

    def count_entity_list(self):
        return len(self.entity_list)
    
    def get_component_of_entity(self, entity_id: int):
        entity_data = self.entity_metadata_list.get(entity_id)

        if entity_data is None:
            return None
        
        response: EntityMetadata = {}

        response.update(entity_data.get_data())

        return response
    
    def add_component(self, entity_id: int, component: str, component_instance):
        if self.component_list.get(component) is None:
            raise Exception('Invalid Component')
        
        if self.entity_list.get(entity_id) is None:
            raise Exception('Invalid Entity Id')

        self.component_list[component][entity_id] = component_instance

    def get_component(self, entity_id, component_type):
        return self.component_list[component_type][entity_id]

    def get_entity_component(self, *component_types):
        entity_list = {}

        for entity_id in self.entity_list:
            component_types_match_list = {}

            for component_type in component_types:
                component_types_match_list[component_type] = {}
                component_types_match_list[component_type][entity_id] = False

            for component in self.component_list:
                check_if_exist_component = len(self.component_list[component].values())

                if check_if_exist_component != 0:
                    if self.component_list[component].get(entity_id) is not None and self.component_list[component][entity_id] is not None:
                        component_types_match_list[component][entity_id] = True
                        

            result_match = []

            for company_type_match in component_types_match_list:
                result_match.append(component_types_match_list[company_type_match][entity_id])

            if all(result_match):
                entity_list[entity_id] = entity_id

        return entity_list