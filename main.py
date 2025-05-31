from duck_engine import DuckEngine
from core.ecs_manager import EcsManager
from components.transform import Transform

duck_engine = DuckEngine()

player_id = duck_engine.ecs_manager.create_entity('Player', 'player')
ground_id = duck_engine.ecs_manager.create_entity('Ground', '')

duck_engine.ecs_manager.get_entity_list()