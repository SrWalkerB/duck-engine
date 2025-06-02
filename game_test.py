from duck_engine import DuckEngine
from components.transform import Transform
from components.sprite import Sprite

duck_engine = DuckEngine()

player_id = duck_engine.ecs_manager.create_entity('Player', 'player')
ground_id = duck_engine.ecs_manager.create_entity('ground')
test = duck_engine.ecs_manager.create_entity('Vai Dormir')

duck_engine.ecs_manager.add_component(player_id, "Transform", Transform(
    0.3,
    0.2,
    0.4,
    0.5
))
duck_engine.ecs_manager.add_component(player_id, "Sprite", Sprite("green"))

duck_engine.ecs_manager.add_component(ground_id, "Transform", Transform(
    -0.1,
    -0.2,
    0.4,
    0.5
))

duck_engine.ecs_manager.add_component(ground_id, "Sprite", Sprite("red"))

duck_engine.ecs_manager.add_component(test, "Transform", Transform(
    -0.9,
    -0.4,
    0.2,
    0.2
))

duck_engine.ecs_manager.add_component(test, "Sprite", Sprite("red"))


duck_engine.start_game()
