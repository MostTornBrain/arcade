import arcade

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Example"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player_sprite = None
        self.wall_list = None

    def setup(self):
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64

        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.center_x = 300
        wall.center_y = 300
        self.wall_list.append(wall)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

        self.wall_list.draw()
        print("Before player draw")
        self.player_sprite.draw()
        print("After player draw")


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()