class AvailableComponents:
    def __init__(self):
        self.available_components_list = {
            "Transform": {}
        }

    def register_components(self, component: str):
        self.available_components_list[component] = {}
    
    def get_component_list(self):
        for component in self.available_components_list:
            print(f'component init = {component}')