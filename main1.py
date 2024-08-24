import pygame
import time
import ctypes
import sys
from pygame.locals import *

# Function to display settings
def show_settings():
    ctypes.windll.user32.MessageBoxW(0, "No Settings Available", "Settings", 0x40 | 0x1)

# Function to start full screen screensaver
def start_full_screen():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    run_screensaver(screen, screen.get_width(), screen.get_height())

# Function to start preview mode
def start_preview(window_id):
    # Handle window_id here if necessary. For now, it's a placeholder.
    screen = pygame.display.set_mode((800, 600))  # Adjust size if needed
    run_screensaver(screen, 800, 600)

# Function to run the screensaver
def run_screensaver(screen, screenwidth, screenheight):
    logoSpeed = [1, 1]  # Movement speed for the logo
    backgroundColor = (0, 0, 0)  # RGB values for background color

    # Load and scale the image
    image = pygame.image.load("logo.png")
    image = pygame.transform.scale(image, (100, 100))
    logoRect = image.get_rect()

    exitgame = True
    while exitgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = False
        
        screen.fill(backgroundColor)
        screen.blit(image, logoRect)
        logoRect = logoRect.move(logoSpeed)

        if logoRect.left < 0 or logoRect.right > screenwidth:
            logoSpeed[0] = -logoSpeed[0]
        if logoRect.top < 0 or logoRect.bottom > screenheight:
            logoSpeed[1] = -logoSpeed[1]

        pygame.display.flip()
        time.sleep(10 / 1000)  # 0.01 seconds
    pygame.quit()

# Main entry point
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '/c':
            show_settings()
        elif sys.argv[1] == '/s':
            start_full_screen()
        elif sys.argv[1].startswith('/p'):
            try:
                window_id = int(sys.argv[1].split()[1])
                start_preview(window_id)
            except IndexError:
                show_settings()
            except ValueError:
                show_settings()
        else:
            show_settings()
    else:
        # Default behavior is to start full screen
        start_full_screen()
