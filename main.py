from duck_engine import DuckEngine
from core.entity_manager import EntityManager

duckEngine = DuckEngine()
entity_manager = EntityManager()

player_id = entity_manager.create_entity('player')

print(player_id)
# entity_manager.get_entity_list()



# duckEngine.start_engine()