class EntityMetadata:
    def __init__(self, entity_id: int, name: str = '', tag: str = ''):
        self.entity_id = entity_id
        self.name = name
        self.tag = tag

    def get_data(self):
        metadata: dict = {}

        metadata["entity_id"] = self.entity_id
        metadata["name"] = self.name
        metadata["tag"] = self.tag

        return metadata