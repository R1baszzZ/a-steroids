import pygame
from player import *
from asteroid import *
from asteroidfield import *
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, screen, PLAYER_RADIUS
from logger import log_state





def main():
    pygame.init()
    # initiated the clock
    clock = pygame.time.Clock()
    # delta time
    dt = 0
    # created groups using sprite.Group method so its easier to sort objs by categories
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # initialized static containers
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    # instantiated the objs
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    # this is the loop that the magic of the game happens
    while True:
        # im keeping logs to troubleshoot easier
        log_state()
        # checking if the user pressed the quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # delta time (im still understanding what this does, but im understanding so far that it is the moment in the 60th of a second)
        dt = clock.tick(60) / 1000
        # just the screen (canvas)
        screen.fill("black")
        # iterating the groups so they can do their actions.
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)

        # swaps the off‑screen buffer to the screen.
        pygame.display.flip()


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    


if __name__ == "__main__":
    main()
