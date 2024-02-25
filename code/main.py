import pygame, sys
from settings import *  # Importing settings module for game configurations
from level import Level  # Importing Level class from level module

class Game:
    def __init__(self):
        """Initialize the game."""
        
        # General setup
        pygame.init()  # Initialize Pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the game window/screen
        pygame.display.set_caption('Zelda Souls')  # Set the window caption/title
        self.clock = pygame.time.Clock()  # Create a Pygame Clock object for controlling the frame rate
        
        self.level = Level()  # Create an instance of the Level class for managing game levels

        # Sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')  # Load background music
        main_sound.set_volume(0.5)  # Set the volume level
        main_sound.play(loops=-1)  # Start playing the background music in an infinite loop

    def run(self):
        """Run the game loop."""
        
        while True:  # Main game loop
            for event in pygame.event.get():  # Handle events
                if event.type == pygame.QUIT:  # Check if the user wants to quit the game
                    pygame.quit()  # Quit Pygame
                    sys.exit()  # Exit the program
                if event.type == pygame.KEYDOWN:  # Check if a key is pressed
                    if event.key == pygame.K_m:  # Check if the 'm' key is pressed
                        self.level.toggle_menu()  # Toggle the in-game menu

            self.screen.fill(WATER_COLOR)  # Fill the screen with the background color
            self.level.run()  # Run the game level
            pygame.display.update()  # Update the display
            self.clock.tick(FPS)  # Control the frame rate

if __name__ == '__main__':
    game = Game()  # Create an instance of the Game class
    game.run()  # Run the game loop
