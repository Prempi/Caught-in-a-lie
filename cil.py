import arcade
from models import World 
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 400

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class SpySprite:
    def __init__(self,spy):
        self.sp = spy
        self.sp_sprite = arcade.Sprite('images/block.png')

    def draw(self):
        self.sp_sprite.set_position(self.sp.x,self.sp.y)
        self.sp_sprite.draw()
 
class RoomWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.CHARCOAL)
        self.world = World(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.spy_sprite = SpySprite(self.world.spy)
        self.security_sprite1 = ModelSprite('images/Heart.png',model = self.world.secure)
        self.security_sprite2 = ModelSprite('images/Heart.png',model = self.world.secure2)
        self.security_sprite3 = ModelSprite('images/Heart.png',model = self.world.secure3)
        self.security_sprite4 = ModelSprite('images/Heart.png',model = self.world.secure4)
        

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        #if self.spy_sprite.sp.gg == 0:
        self.spy_sprite.draw()
        self.security_sprite1.draw()
        self.security_sprite2.draw()
        self.security_sprite3.draw()
        self.security_sprite4.draw()
        '''
            xx = 100
            yy = 100
            text = "Score : {:d}".format(self.snake_sprite.snake.length-3)
            self.t8 = arcade.create_text(text, arcade.color.BLACK, 14)
            arcade.render_text(self.t8, xx, yy)
            

        else:
            xx = 240
            yy = SCREEN_HEIGHT//2 - 64
            start_x = 180
            start_y = SCREEN_HEIGHT//2 + 64
            arcade.render_text(self.t1,start_x,start_y)
            arcade.set_background_color(arcade.color.CHARCOAL)
            text = "Score : {:d}".format(self.snake_sprite.snake.length-3)
            self.t8 = arcade.create_text(text, arcade.color.BLACK, 30)
            arcade.render_text(self.t8, xx, yy)
        '''
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
 
def main():
    window = RoomWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
