import arcade
from models import World 
SCREEN_WIDTH = 1000
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
        super().__init__(width, height,'Caught in a lie')
 
        #arcade.set_background_color(arcade.color.CHARCOAL)
        self.world = World(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.spy_sprite = SpySprite(self.world.spy)
        
        self.security_sprite1 = SecureSprite(self.world.secure)
        self.security_sprite2 = SecureSprite(self.world.secure2)
        self.security_sprite3 = SecureSprite(self.world.secure3)
        self.security_sprite4 = SecureSprite(self.world.secure4)
        self.background = arcade.load_texture("images/bg.png")
        self.background2 = arcade.load_texture("images/bg2.png")
        self.background3 = arcade.load_texture("images/bg3.png")
        self.bulldog1 = ModelSprite('images/bulldog.png',model = self.world.brain1)
        self.bulldog2 = ModelSprite('images/bulldog.png',model = self.world.brain2)
        self.bulldog3 = ModelSprite('images/bulldog.png',model = self.world.brain3)
        self.bulldog4 = ModelSprite('images/bulldog.png',model = self.world.brain4)
        self.brain1 = ModelSprite('images/brain.png',model = self.world.brain5)
        self.brain2 = ModelSprite('images/brain.png',model = self.world.brain6)
        self.brain3 = ModelSprite('images/brain.png',model = self.world.brain7)
        self.brain4 = ModelSprite('images/brain.png',model = self.world.brain8)
        self.scoreCheck = False
        '''
        
        self.security_sprite1 = ModelSprite('images/Heart.png',model = self.world.secure)
        self.security_sprite2 = ModelSprite('images/Heart.png',model = self.world.secure2)
        self.security_sprite3 = ModelSprite('images/Heart.png',model = self.world.secure3)
        self.security_sprite4 = ModelSprite('images/Heart.png',model = self.world.secure4)
        '''
        self.gg = arcade.create_text("Game over", arcade.color.BLACK, 50)
        #self.end_score = arcade.create_text("Score"+str(self.spy_sprite.sp.score)), arcade.color.BLACK, 50)
        self.ordi = arcade.create_text("O", arcade.color.AMAZON, 20)
        self.clever = arcade.create_text("C", arcade.color.BLACK, 20)
        self.time_elapsed = 3
        self.t9 = arcade.create_text("Time to Lie: {:d}".format(self.time_elapsed), arcade.color.BLACK, 25)
        #self.time_elapsed = 0

    def update(self, delta):
        self.world.update(delta)
        if self.world.count % 60 == 0:
            self.time_elapsed -= 1
        if self.spy_sprite.sp.state == self.spy_sprite.sp.STATE_RUN:
            self.time_elapsed = 3

    def on_draw(self):
        arcade.start_render()
        
        if self.world.gg == 0:
            if self.world.mode == 1:
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
                #arcade.set_background_color(arcade.color.AMAZON)
            elif self.world.mode == 2:
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background2)
                #arcade.set_background_color(arcade.color.PURPLE)
            self.spy_sprite.draw()
            if self.security_sprite1.sc.type == self.security_sprite1.sc.ORDINARY:
                self.bulldog1.draw()
            else:
                self.brain1.draw()
            self.security_sprite1.draw()
            if self.security_sprite2.sc.type == self.security_sprite2.sc.ORDINARY:
                self.bulldog2.draw()
            else:
                self.brain2.draw()
            self.security_sprite2.draw()
            if self.security_sprite3.sc.type == self.security_sprite3.sc.ORDINARY:
                self.bulldog3.draw()
            else:
                self.brain3.draw()
            self.security_sprite3.draw()
            if self.security_sprite4.sc.type == self.security_sprite4.sc.ORDINARY:
                self.bulldog4.draw()
            else:
                self.brain4.draw()
            self.security_sprite4.draw()
            xx = 100
            yy = 370
            text = "Score : {:d}".format(int(self.spy_sprite.sp.score/2))
            self.t8 = arcade.create_text(text, arcade.color.LAVENDER, 18)
            arcade.render_text(self.t8, xx, yy)
            text = "Time to Lie: {:d}".format(int(self.time_elapsed))
            if text != self.t9.text:
                self.t9 = arcade.create_text(text, arcade.color.BLACK, 25)
            arcade.render_text(self.t9, 384, 250)
        else:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background3)
            f = open('highscore.log', 'r')
            highscore = f.readline()
            if int(self.spy_sprite.sp.score/2) > int(highscore) or self.scoreCheck:
                self.scoreCheck = True
                arcade.draw_text('New Highscore!', 500, 200, arcade.color.BLACK, 30)
                f = open('highscore.log', 'w')
                f.write(str(int(self.spy_sprite.sp.score/2)))

            else:
                arcade.draw_text('Highscore: ' + highscore, 500, 200, arcade.color.BLACK, 30)
            start_x = 500
            start_y = 250 
            arcade.render_text(self.gg,start_x,start_y)
            text = "Score : {:d}".format(int(self.spy_sprite.sp.score/2))
            self.score = arcade.create_text(text, arcade.color.BLACK, 30)
            
            arcade.render_text(self.score, start_x, start_y-100)
            arcade.set_background_color(arcade.color.CHARCOAL)
            
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
 
def main():
    window = RoomWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
