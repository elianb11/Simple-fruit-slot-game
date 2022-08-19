import pygame
import game

pygame.init()

class Location(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/pomme_dore.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def set_image(self,image):
        self.image = image


width = 800
height = 460
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Bobby Fruity Party")
icon = pygame.image.load('images/pomme_dore.png')
pygame.display.set_icon(icon)

white = [255,255,255]

fruits_images = {
    "orange": pygame.image.load('images/orange.png'),
    "cherry": pygame.image.load('images/cerise.png'),
    "pineapple": pygame.image.load('images/ananas.png'),
    "watermelon": pygame.image.load('images/pasteque.png'),
    "golden_apple": pygame.image.load('images/pomme_dore.png'),
}

locations = pygame.sprite.Group()
left_location = Location(227, height/1.8)
mid_location = Location(327, height/1.8)
right_location = Location(428, height/1.8)

locations.add(left_location)
locations.add(mid_location)
locations.add(right_location)

background = pygame.image.load('images/slot.png')

bonus_background = {
    "orange": pygame.image.load('images/slot_orange.png'),
    "cherry": pygame.image.load('images/slot_cerise.png'),
    "pineapple": pygame.image.load('images/slot_ananas.png'),
    "watermelon": pygame.image.load('images/slot_pasteque.png'),
    "golden_apple": pygame.image.load('images/slot_pomme_dore.png'),
}

def launch_new_round(game):
    random_fruits = game.play()
    print(random_fruits)
    left_location.set_image(fruits_images[random_fruits[0]])
    mid_location.set_image(fruits_images[random_fruits[1]])
    right_location.set_image(fruits_images[random_fruits[2]])

game = game.Game(balance = 1000)
is_bonus = False

font = pygame.font.SysFont('gillsanscondensed', 40)

running = True
while running:

    screen.fill(white)
    locations.draw(screen)
    if game.is_bonus:
        screen.blit(bonus_background[game.bonus_fruit], (0,0))
    else:
        screen.blit(background, (0,0))
    text = font.render("Balance: "+str(game.balance)+" €", True, (0,0,0))
    screen.blit(text, (10,405))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Balance total: {}".format(game.balance))
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                launch_new_round(game)