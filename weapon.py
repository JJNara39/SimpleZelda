import pygame, os

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direction = player.status.split('_')[0]

        #graphic
        
        full_path = f'..\\SimpleZelda\\graphics\\weapons\\{player.weapon}\\{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        
        
        # placement
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16)) # tiny bit too high, so adding a little more y onto it in order to lower it
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16)) # tiny bit too high, so adding a little more y onto it in order to lower it
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0)) # tiny bit too high, so taking away some to center it
        else:
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))