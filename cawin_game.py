from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.clock import Clock
from kivy.core.text import Label as Corelabel
from kivy.config import Config
import random


class gamewidget(Widget):

    def __init__(self):
        super().__init__()
        #Keyboard controls
        self._keyboard = Window.request_keyboard(self.on_keyboard, self)
        self._keyboard.bind(on_key_down=self.on_keyboard_down)
        self._keyboard.bind(on_key_up=self.on_keyboard_up)
        #Frame tracker
        self.register_event_type("on_frame")
        Clock.schedule_interval(self._on_frame, 0)
        #spawn rates
        self.spawn_white_count = 0
        self.spawn_fast_count = 0
        self.spawn_thick_count = 0
        self.spawn_total_count = 0
        self.spawn_white_total = 9
        self.spawn_fast_total = 2
        self.spawn_thick_total = 2

        Clock.schedule_interval(self.spawn_normal_enemies, 5)
        Clock.schedule_interval(self.spawn_fast_enemies, 20)
        Clock.schedule_interval(self.spawn_thick_enemies, 15)

        self.keysPressed = set()
        self._entities = set()

        #Decoration for score and health tracking
        self._score_board = Corelabel(text='Reward: $0',font_size=30)
        self._score_board.refresh()
        self._score = 0

        self._health_board = Corelabel(text='Health =>',font_size=30)
        self._health_board.refresh()

        with self.canvas:
            self._score_instruction = Rectangle(texture=self._score_board.texture,pos=(0,Window.height - 50),size=self._score_board.size)
            self._health_instruction = Rectangle(texture=self._health_board.texture, pos=(Window.width-185, Window.height - 55),
                                                size=self._health_board.size)
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        self._score = value
        self._score_board.text = 'Reward: $' + str(value)
        self._score_board.refresh()
        self._score_instruction.texture = self._score_board.texture
        self._score_instruction.size = self._score_board.size


    def _on_frame(self,dt):
        self.dispatch("on_frame",dt)

    def on_frame(self,dt):
        pass

    def add_entity(self, entity):
        self._entities.add(entity)
        self.canvas.add(entity._instruction)

    def remove_entity(self, entity):
        if entity in self._entities:
            self._entities.remove(entity)
            self.canvas.remove(entity._instruction)

    def spawn_normal_enemies(self, dt):
        if self.spawn_white_count <= self.spawn_white_total:
            random_x = random.randint(0, Window.width)
            y = Window.height - 50
            random_speed = random.randint(125, 175)
            random_left_or_right = random.randint(0, 1)
            size = (((Window.width-150) * (Window.height-150)))**(1/3)*2.5
            self.add_entity(Enemy((random_x, y), random_speed,(size,size),left_or_right=random_left_or_right))
            self.spawn_white_count += 1

    def spawn_fast_enemies(self, dt):
        if self.spawn_fast_count <= self.spawn_fast_total:
            random_x = random.randint(0, Window.width)
            y = Window.height - 50
            random_speed = random.randint(600, 800)
            random_left_or_right = random.randint(0, 1)
            size = (((Window.width-150) * (Window.height-150)))**(1/3)
            self.add_entity(Enemy((random_x, y), random_speed,(size,size),left_or_right=random_left_or_right,type=1))
            self.spawn_fast_count += 1


    def spawn_thick_enemies(self, dt):
        if self.spawn_thick_count <= self.spawn_thick_total:
            random_x = random.randint(0, Window.width)
            y = Window.height - 50
            random_speed = random.randint(25, 50)
            random_left_or_right = random.randint(0, 1)
            size = (((Window.width-150) * (Window.height-150)))**(1/3)*5
            self.add_entity(Enemy((random_x, y), random_speed,(size,size),left_or_right=random_left_or_right,type=2))
            self.spawn_thick_count += 1

    def collides(self, entitiy1, entitiy2):
        #Finds the middle of each box
        entitiy1_x = entitiy1.pos[0]
        entitiy1_y = entitiy1.pos[1]
        entitiy2_x = entitiy2.pos[0]
        entitiy2_y = entitiy2.pos[1]
        #finds the dimensions of each box
        entitiy1_width = entitiy1.size[0]
        entitiy1_height = entitiy1.size[1]
        entitiy2_width = entitiy2.size[0]
        entitiy2_height = entitiy2.size[1]

        if (entitiy1_x < entitiy2_x + entitiy2_width and entitiy1_x + entitiy1_width > entitiy2_x
                and entitiy1_y < entitiy2_y + entitiy2_height and entitiy1_y + entitiy1_height > entitiy2_y):
            return True
        else:
            return False

    def colliding_entities(self, entity):
        result = set()
        for e in self._entities:
            if self.collides(e, entity) and e != entity:
                result.add(e)
        return result

    def on_keyboard(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard = None

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(keycode[1])

    def on_keyboard_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)


class Entity(object):
    def __init__(self):
        #Placeholders
        self._pos = (0,0)
        self._size = (50,50)
        self._source = 'tools/theming/defaulttheme/checkbox_radio_on.png'
        self._instruction = Rectangle(source=self._source,pos=self._pos,size=self._size)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self,value):
        self._pos = value
        self._instruction.pos = self._pos

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self._instruction.size = self._size

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
        self._instruction.source = self._source

class Healthicon(Entity):
    def __init__(self,source="tools/theming/defaulttheme/audio-volume-high.png"):
        super().__init__()
        self.pos = (Window.width - 60, Window.height-60)
        self.source = source
        self.size = (50, 50)
        game.bind(on_frame=self.health_total)

    def stop_callbacks(self):
        game.unbind(on_frame=self.health_total)

    def health_total(self,sender,dt):
        if game.player.health == 2:
            self.stop_callbacks()
            game.remove_entity(self)
            game.add_entity(Healthicon(source="tools/theming/defaulttheme/audio-volume-medium.png"))
        if game.player.health == 1:
            self.stop_callbacks()
            game.remove_entity(self)
            game.add_entity(Healthicon(source="tools/theming/defaulttheme/audio-volume-low.png"))
        if game.player.health <=  0:
            self.stop_callbacks()
            game.remove_entity(self)
            game.add_entity(Healthicon(source="tools/theming/defaulttheme/audio-volume-muted.png"))

class Dashicon(Entity):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.source = 'tools/theming/defaulttheme/tab_btn_disabled.png'
        self.size = (15,25)
        game.bind(on_frame=self.move)

    def stop_callbacks(self):
        game.unbind(on_frame=self.move)

    def move(self, sender, dt):
        # Keeps track of state of dash for user
        if game.player.dash_num <= 0 or game.player.health <= 0 or game.player.time_up == True:
            self.stop_callbacks()
            game.remove_entity(self)

        #movement of dash icon
        dashicon_y_position = self.pos[1]
        dashicon_x_position = game.player.pos[0] - 30
        self.pos = (dashicon_x_position, dashicon_y_position)

class Bulleticon(Entity):
    def __init__(self,pos,number):
        super().__init__()
        self.pos = pos
        self.number = number
        self.source = "tools/theming/defaulttheme/splitter.png"
        self.size = (5, 25)
        game.bind(on_frame=self.move)

    def stop_callbacks(self):
        game.unbind(on_frame=self.move)

    def move(self, sender, dt):
        #Keeps track of state of bullets for user
        if game.player.bullet_num == 1 and self.number == 1:
            self.stop_callbacks()
            game.remove_entity(self)
        if game.player.bullet_num == 0 and self.number == 0:
            self.stop_callbacks()
            game.remove_entity(self)
        # Remove icon when player is dead or game over
        if game.player.health <= 0 or game.player.time_up == True:
            self.stop_callbacks()
            game.remove_entity(self)
        # move
        bullet_x_position = self.pos[0]
        bullet_y_position = self.pos[1]

        if self.number == 1:
            bullet_x_position = game.player.pos[0] + 70
        if self.number == 0:
            bullet_x_position = game.player.pos[0] + 60
        self.pos = (bullet_x_position, bullet_y_position)


class Bullet(Entity):
    def __init__(self, pos, speed=500):
        super().__init__()
        self._speed = speed
        self.pos = pos
        self.source = "tools/theming/defaulttheme/splitter.png"
        self.size = (10,150)
        game.bind(on_frame=self.move)
        game.player.bullet_num -= 1

    def stop_callbacks(self):
        game.unbind(on_frame=self.move)


    def move(self,sender,dt):
        # Bullet out of screen?
        if self.pos[1] > Window.height:
            game.unbind(on_frame=self.move)
            self.stop_callbacks()
            game.remove_entity(self)
            # limit to two bullet in the screen only
            if game.player.bullet_num == 1:
                game.player.bullet_num = 2
                game.add_entity(Bulleticon((game.player.pos[0]+70,game.player.pos[1]+30),1))
            if game.player.bullet_num == 0:
                game.player.bullet_num = 1
                game.add_entity(Bulleticon((game.player.pos[0]+60, game.player.pos[1]+30), 0))
            return
        # Collided?
        for e in game.colliding_entities(self):
            #Enemy to be added
            if isinstance(e,Enemy):
                game.unbind(on_frame=self.move)
                game.remove_entity(self)
                self.stop_callbacks()
                game.add_entity(Explosion(e.pos, (e.size[0]/2.5,e.size[1]/2.5)))
                e.stop_callbacks()
                game.remove_entity(e)
                #enemy spilts into two
                if e.size[0] == e.bubble_size and e.type == 0:
                    game.score += 2
                if e.size[0] == e.bubble_size/2 and e.type == 0:
                    game.score += 5
                if e.size[0] == e.bubble_size/4 and e.type == 0:
                    game.score += 10

                if e.size[0] == e.bubble_size_small and e.type == 1:
                    game.score += 25
                if e.size[0] == e.bubble_size_small/2 and e.type == 1:
                    game.score += 50

                if e.size[0] == e.bubble_size_big and e.type == 2:
                    game.score += 5
                if e.size[0] == e.bubble_size_big/2 and e.type == 2:
                    game.score += 10
                if e.size[0] == e.bubble_size_big/4 and e.type == 2:
                    game.score += 15
                if e.size[0] == e.bubble_size_big/8 and e.type == 2:
                    game.score += 20

                if e.size[0] > e.bubble_size/4:
                    game.add_entity(Enemy((e.pos[0] + 75,e.pos[1]), e._speed+50,(e.size[0]/2,e.size[1]/2),left_or_right=1,type=e.type))
                    game.add_entity(Enemy((e.pos[0] - 75,e.pos[1]), e._speed+50, (e.size[0]/2, e.size[1]/2),left_or_right=0,type=e.type))
                #limit to two bullet in the screen only
                if game.player.bullet_num == 1:
                    game.player.bullet_num = 2
                    game.add_entity(Bulleticon((game.player.pos[0]+70, game.player.pos[1]+30), 1))
                if game.player.bullet_num == 0:
                    game.player.bullet_num = 1
                    game.add_entity(Bulleticon((game.player.pos[0]+60, game.player.pos[1]+30), 0))

        #else Move when fired
        frame_rate = self._speed * dt
        weapon_x_position = self.pos[0]
        weapon_y_position = self.pos[1] + frame_rate
        self.pos = (weapon_x_position,weapon_y_position)

class Explosion(Entity):
    def __init__(self, pos, size):
        super().__init__()
        self.source = "tools/theming/defaulttheme/image-missing.png"
        self.size = size
        self.pos = (pos[0]+(self.size[0]/6),pos[1] - (self.size[0]/2))
        Clock.schedule_once(self._remove_me, 0.1)

    def _remove_me(self, dt):
        game.remove_entity(self)

class Enemy(Entity):
    bubble_size = (((Window.width-150) * (Window.height-150)))**(1/3)*2.5
    bubble_size_small = (((Window.width-150) * (Window.height-150)))**(1/3)
    bubble_size_big = (((Window.width-150) * (Window.height-150)))**(1/3)*5
    speed = 100

    def __init__(self,pos,speed=speed,size=(bubble_size, bubble_size),left_or_right=random.randint(0,1),direction=0,type=0):
        super().__init__()
        self._speed = speed
        self.pos = pos
        self.size = size
        self.left_or_right = left_or_right
        self.direction = direction
        self.type = type
        if self.type == 0:
            self.source = 'tools/theming/defaulttheme/textinput_disabled.png'
        if self.type == 1:
            self.source = 'tools/theming/defaulttheme/spinner_pressed.png'
        if self.type == 2:
            self.source = 'tools/theming/defaulttheme/tab_btn_pressed.png'
        game.bind(on_frame=self.move)
        self.lst = []

    def stop_callbacks(self):
        game.unbind(on_frame=self.move)

    def move(self, sender, dt):
        if game.player.health <= 0:
            game.unbind(on_frame=self.move)
            self.stop_callbacks()
            return
        if game.player.time_up == True:
            self.stop_callbacks()
            game.unbind(on_frame=self.move)
            game.remove_entity(self)
        self.lst.append(self.pos[0])
        # bounce if hit the bottom
        if self.pos[1] < 0 and self.pos[0] != game.player.pos[0] and self.pos[1] != game.player.pos[1]:
           self.stop_callbacks()
           game.unbind(on_frame=self.move)
           game.remove_entity(self)
           if self.left_or_right == 0:
               game.add_entity(Enemy((self.pos[0],abs(self.pos[1])), self._speed,self.size,left_or_right=0,direction=1,type=self.type))
           if self.left_or_right == 1:
               game.add_entity(Enemy((self.pos[0],abs(self.pos[1])), self._speed, self.size,left_or_right=1,direction=1,type=self.type))
        # Bounce if hit top
        if self.pos[1] > Window.height-self.size[0]:
           self.stop_callbacks()
           game.unbind(on_frame=self.move)
           game.remove_entity(self)
           if self.left_or_right == 0:
               game.add_entity(Enemy((self.pos[0],Window.height-self.size[0]), self._speed,self.size,left_or_right=0,direction=0,type=self.type))
           if self.left_or_right == 1:
               game.add_entity(Enemy((self.pos[0],Window.height-self.size[0]), self._speed, self.size,left_or_right=1,direction=0,type=self.type))
        # Bounce if hit left
        if self.pos[0] < 0:
            self.stop_callbacks()
            game.unbind(on_frame=self.move)
            game.remove_entity(self)
            if self.left_or_right == 0:
               game.add_entity(Enemy((abs(self.pos[0]),self.pos[1]), self._speed,self.size,left_or_right=1,direction=self.direction,type=self.type))
            if self.left_or_right == 1:
               game.add_entity(Enemy((abs(self.pos[0]),self.pos[1]), self._speed, self.size,left_or_right=0,direction=self.direction,type=self.type))
        # Bounce if hit right
        if self.pos[0] > Window.width-self.size[0]:
            self.stop_callbacks()
            game.unbind(on_frame=self.move)
            game.remove_entity(self)
            if self.left_or_right == 0:
               game.add_entity(Enemy((Window.width-self.size[0],self.pos[1]), self._speed,self.size,left_or_right=1,direction=self.direction,type=self.type))
            if self.left_or_right == 1:
               game.add_entity(Enemy((Window.width-self.size[0],self.pos[1]), self._speed, self.size,left_or_right=0,direction=self.direction,type=self.type    ))
        for e in game.colliding_entities(self):
            if e == game.player and game.player.invincible_frames != True:
                #Explosion near the player e.pos is a fixed position and self.pos is
                game.add_entity(Explosion(((e.pos[0]+self.pos[0])/2,self.pos[1]), (e.size[0] * 2, e.size[1] * 2)))
                game.unbind(on_frame=self.move)
                self.stop_callbacks()
                game.remove_entity(self)
                game.player.health -= 1
                return

            # move
        # Enemy movement
        frame_rate = self._speed * dt
        enemy_x_position = self.pos[1] - frame_rate
        enemy_y_position = self.pos[1] - frame_rate
        if self.left_or_right == 0:
            enemy_x_position = self.pos[0] - (frame_rate/2)
        if self.left_or_right == 1:
            enemy_x_position = self.pos[0] + (frame_rate/2)
        if self.direction == 1:
            enemy_y_position = self.pos[1] + frame_rate
        self.pos = (enemy_x_position, enemy_y_position)



class Player(Entity):
    def __init__(self):
        super().__init__()
        self.source = "tools/theming/defaulttheme/textinput_active.png"
        game.bind(on_frame=self.move)
        self._shoot_event = Clock.schedule_interval(self.shoot_step, 0.10)
        self.shot = False
        self.pos = (400, 0)
        self.size = (50,50)
        game.add_entity(Bulleticon((self.pos[0]+60,self.pos[1]+30),0))
        game.add_entity(Bulleticon((self.pos[0]+70,self.pos[1]+30),1))
        game.add_entity(Dashicon(((self.pos[0]-30,self.pos[1]+30))))
        game.add_entity(Healthicon())
        self.health = 3
        # limit to two bullet in the screen only
        self.bullet_num = 2
        self.dash_num = 1
        self.invincible_frames = False
        self.max_enemy = 10
        self.time_up = False


    def stop_callbacks(self):
        game.unbind(on_frame=self.move)
        self._shoot_event.cancel()

    def shoot_step(self, dt):
        # shoot
        #Attempt to prevent people from holding the spacebar
        self.shot = True
        if "spacebar" in game.keysPressed and self.bullet_num > 0 and self.health > 0 and self.shot == True and self.time_up == False:
            x = self.pos[0] + 20
            y = self.pos[1] + 40
            self.shot = False
            game.add_entity(Bullet((x, y)))

    def invincible(self,dt):
        self.invincible_frames = False
        self.source = "tools/theming/defaulttheme/textinput_active.png"
        return
    def reset_dash(self,dt):
        self.dash_num += 1
        game.add_entity(Dashicon(((self.pos[0] - 30, self.pos[1] + 30))))
        return

    def time_over(self,dt):
        self.time_up = True

    def move(self, sender, dt):
        # move
        frame_rate = 200 * dt
        player_x_position = self.pos[0]
        player_y_position = self.pos[1]
        if "left" in game.keysPressed and game.player.health > 0 and self.time_up == False:
            if player_x_position > 0:
                player_x_position -= frame_rate + 2
        if "right" in game.keysPressed and game.player.health > 0 and self.time_up == False:
            if player_x_position < Window.width - 50:
                player_x_position += frame_rate + 2
        #Dash mechanic
        if "v" in game.keysPressed and "left" in game.keysPressed and self.dash_num >= 1 and self.health > 0 and self.time_up == False:
            if player_x_position > 0:
                self.invincible_frames = True
                self.dash_num -= 1
                self.source = 'tools/theming/defaulttheme/tab_btn_disabled.png'
                Clock.schedule_once(self.invincible, 0.3)
                Clock.schedule_once(self.reset_dash, 1)
                player_x_position -= frame_rate * 35

        if "v" in game.keysPressed and "right" in game.keysPressed and self.dash_num >= 1 and self.health > 0 and self.time_up == False:
            if player_x_position < Window.width - 50:
                self.invincible_frames = True
                self.dash_num -= 1
                self.source = 'tools/theming/defaulttheme/tab_btn_disabled.png'
                Clock.schedule_once(self.invincible, 0.3)
                Clock.schedule_once(self.reset_dash, 1)
                player_x_position += frame_rate * 35

        self.pos = (player_x_position, player_y_position)

        if self.health <= 0:
            self._game_over_board = Corelabel(text='GAME OVER', font_size=125)
            self._game_over_board_2 = Corelabel(text='Press esc to exit', font_size=100)
            self._game_over_board_3 = Corelabel(text='Turning off in 20 seconds...', font_size=80)
            self._game_over_board.refresh()
            self._game_over_board_2.refresh()
            self._game_over_board_3.refresh()
            Clock.unschedule(game.spawn_normal_enemies)
            Clock.unschedule(game.spawn_fast_enemies)
            Clock.unschedule(game.spawn_thick_enemies)
            Clock.schedule_once(self.stop_game, 20)

            with game.canvas:
                self._game_over_instruction = Rectangle(texture=self._game_over_board.texture, pos=((Window.width-self._game_over_board.size[0])/2, (Window.height-self._game_over_board.size[1])/2),
                                                    size=self._game_over_board.size)
                self._game_over_2_instruction = Rectangle(texture=self._game_over_board_2.texture, pos=(
                (Window.width - self._game_over_board_2.size[0]) / 2,
                (Window.height - self._game_over_board_2.size[1]) / 2 - 100),
                                                        size=self._game_over_board_2.size)
                self._game_over_3_instruction = Rectangle(texture=self._game_over_board_3.texture, pos=(
                    (Window.width - self._game_over_board_3.size[0]) / 2,
                (Window.height - self._game_over_board_3.size[1]) / 2 - 200),
                                                          size=self._game_over_board_3.size)

        Clock.schedule_once(self.time_over, 65)
        if self.time_up == True:
            self._you_win_board = Corelabel(text='You won $' + str(game._score) + '!!', font_size=125)
            self._game_over_board_2 = Corelabel(text='Press esc to exit', font_size=100)
            self._game_over_board_3 = Corelabel(text='Turning off in 20 seconds...', font_size=80)
            self._you_win_board.refresh()
            self._game_over_board_2.refresh()
            self._game_over_board_3.refresh()
            Clock.unschedule(game.spawn_normal_enemies)
            Clock.unschedule(game.spawn_fast_enemies)
            Clock.unschedule(game.spawn_thick_enemies)
            Clock.schedule_once(self.stop_game, 20)

            with game.canvas:
                self._you_win_instruction = Rectangle(texture=self._you_win_board.texture, pos=(
                (Window.width - self._you_win_board.size[0]) / 2, (Window.height - self._you_win_board.size[1]) / 2),
                                                      size=self._you_win_board.size)
                self._game_over_2_instruction = Rectangle(texture=self._game_over_board_2.texture, pos=(
                    (Window.width - self._game_over_board_2.size[0]) / 2,
                    (Window.height - self._game_over_board_2.size[1]) / 2 - 100),
                                                          size=self._game_over_board_2.size)
                self._game_over_3_instruction = Rectangle(texture=self._game_over_board_3.texture, pos=(
                    (Window.width - self._game_over_board_3.size[0]) / 2,
                    (Window.height - self._game_over_board_3.size[1]) / 2 - 200),
                                                          size=self._game_over_board_3.size)

    def stop_game(self, dt):
         gameApp().stop()

class gameApp(App):
    def build(self):
        return game

if __name__ == '__main__':
    game = gamewidget()
    game.player = Player()
    game.add_entity(game.player)
    Config.write()
    Config.set('graphics','width','1000')
    Config.set('graphics', 'height', '1000')
    gameApp().run()