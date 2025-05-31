class AvailableComponents:
    def __init__(self):
        self.available_components_list = {
            "Transform": {},
            "Sprite": {},
            "Collider2D": {},
            "Rigidbody2D": {}
        }

    def register_components(self, component: str):
        self.available_components_list[component] = {}
    
    def get_component_list(self):
        component_list = []

        for component in self.available_components_list:
            component_list.append(component)

        return component_list