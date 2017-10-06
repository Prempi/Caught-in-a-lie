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

class SecureSprite:
    def __init__(self,secure):
        self.sc = secure
        self.sc_sprite = arcade.Sprite('images/Heart.png')

    def draw(self):
        self.sc_sprite.set_position(self.sc.x,self.sc.y)
        self.sc_sprite.draw()

 
class RoomWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.CHARCOAL)
        self.world = World(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.spy_sprite = SpySprite(self.world.spy)
        
        self.security_sprite1 = SecureSprite(self.world.secure)
        self.security_sprite2 = SecureSprite(self.world.secure2)
        self.security_sprite3 = SecureSprite(self.world.secure3)
        self.security_sprite4 = SecureSprite(self.world.secure4)
        '''
        
        self.security_sprite1 = ModelSprite('images/Heart.png',model = self.world.secure)
        self.security_sprite2 = ModelSprite('images/Heart.png',model = self.world.secure2)
        self.security_sprite3 = ModelSprite('images/Heart.png',model = self.world.secure3)
        self.security_sprite4 = ModelSprite('images/Heart.png',model = self.world.secure4)
        '''
        self.gg = arcade.create_text("Game over", arcade.color.BLACK, 50)
        self.ordi = arcade.create_text("O", arcade.color.BLACK, 20)
        self.clever = arcade.create_text("C", arcade.color.BLACK, 20)

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
        
        if self.world.gg == 0:
            if self.world.mode == 1:
                arcade.set_background_color(arcade.color.AMAZON)
            elif self.world.mode == 2:
                arcade.set_background_color(arcade.color.PURPLE)
            self.spy_sprite.draw()
            if self.security_sprite1.sc.type == self.security_sprite1.sc.ORDINARY:
                arcade.render_text(self.ordi, 280, 160)
            else:
                arcade.render_text(self.clever, 280, 160)
            self.security_sprite1.draw()
            if self.security_sprite2.sc.type == self.security_sprite2.sc.ORDINARY:
                arcade.render_text(self.ordi, 440, 160)
            else:
                arcade.render_text(self.clever, 440, 160)
            self.security_sprite2.draw()
            if self.security_sprite3.sc.type == self.security_sprite3.sc.ORDINARY:
                arcade.render_text(self.ordi, 600, 160)
            else:
                arcade.render_text(self.clever, 600, 160)
            self.security_sprite3.draw()
            if self.security_sprite4.sc.type == self.security_sprite4.sc.ORDINARY:
                arcade.render_text(self.ordi, 760, 160)
            else:
                arcade.render_text(self.clever, 760, 160)
            self.security_sprite4.draw()
            xx = 100
            yy = 370
            text = "Score : {:d}".format(int(self.spy_sprite.sp.score/2))
            self.t8 = arcade.create_text(text, arcade.color.LAVENDER, 18)
            arcade.render_text(self.t8, xx, yy)
        else:
            start_x = 300
            start_y = 200 
            arcade.render_text(self.gg,start_x,start_y)
            arcade.set_background_color(arcade.color.CHARCOAL)
            
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
 
def main():
    window = RoomWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
