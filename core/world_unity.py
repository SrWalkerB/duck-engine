from editor.screen_constant import ScreenConstant

class WorldUnityManager:
    def __init__(self):
        screen_constant = ScreenConstant()

        self.world_width = screen_constant.WIDTH_SCREEN
        self.world_height = screen_constant.HEIGHT_SCREEN
    
    def world_to_opengl(self, world_x, world_y):
        gl_x = (world_x / self.world_width) * 2 -1
        gl_y = (world_y/ self.world_height) * 2 -1

        return {
            "gl_x": gl_x,
            "gl_y": gl_y
        }