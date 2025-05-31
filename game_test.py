from duck_engine import DuckEngine
from components.transform import Transform
from components.sprite import Sprite

duck_engine = DuckEngine()

player_id = duck_engine.ecs_manager.create_entity('Player', 'player')
ground_id = duck_engine.ecs_manager.create_entity('ground')

duck_engine.ecs_manager.add_component(player_id, "Transform", Transform(
    duck_engine.WIDTH_SCREEN / 2 +100,
    duck_engine.HEIGHT_SCREEN / 2 + 100
))
duck_engine.ecs_manager.add_component(player_id, "Sprite", Sprite("red"))

duck_engine.ecs_manager.add_component(ground_id, "Transform", Transform(
    100,
    100
))

duck_engine.ecs_manager.add_component(ground_id, "Sprite", Sprite("green"))

duck_engine.start_game()
