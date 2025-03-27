class Goomba:
    alive = True
    speed = 1
    animation_state = 0
    # death_animation_counter = 0

    def __init__(self, c, x, y):
        self.hitbox = goomba_animation_list[0].get_rect(topleft = (x, y))

    def __repr__(self):
        return "My value is " + str(self.temp)

    def die(self):
        self.alive = False
        # do animation counter?

    def animation(self):
        self.animation_state += 1
        if self.alive:
            if self.animation_state < 20:
                """goomba0.png animation state"""
                # goomba_animation_list[0]
                pass
            elif self.animation_state < 40:
                """goomba1.png animation state"""
                # goomba_animation_list[1]
                pass
            elif self.animation_state >= 40:
                """Restart animation"""
                self.animation_state = 0
        else:
            if self.animation_state < 30:
                # die
                # goomba_death_ani
            else:
                # disappear
                self.animation_state = 50

class Characters:
    pass
