from duck_engine import DuckEngine
from components.transform import Transform
from system.render_system import RenderSystem

duck_engine = DuckEngine()

player_id = duck_engine.ecs_manager.create_entity('Player', 'player')
# ground_id = duck_engine.ecs_manager.create_entity('Ground')


render_system = RenderSystem(duck_engine.ecs_manager, None)

render_system.update(10)

# duck_engine.ecs_manager.add_component(player_id, "Transform", Transform())

# duck_engine.start_game()
