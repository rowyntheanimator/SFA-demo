import pygame
import pygame.mixer
import numpy as np

font_map = {
    "A": [
        (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (4, 4),
        (1, 2), (2, 2), (3, 2),
    ],
    "B": [
        (0, 0), (1, 0), (2, 0),
        (0, 1), (3, 1),
        (0, 2), (3, 2),
        (0, 3), (3, 3),
        (0, 4), (2, 4),
        (1, 2), (2, 2), (3, 2),
        (1, 4),
    ],
    "C": [
        (1, 0), (2, 0), (3, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 4), (2, 4), (3, 4),
    ],
    "H": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (4, 4),
        (1, 2), (2, 2),
        (3, 2),
    ],
    "E": [
        (0, 0), (1, 0), (2, 0),
        (0, 1),
        (0, 2), (1, 2), (2, 2),
        (0, 3),
        (0, 4), (1, 4), (2, 4),
    ],
    "L": [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4), (1, 4), (2, 4),
    ],
    "O": [
        (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (1, 4), (2, 4), (3, 4),
    ],
    "W": [ 
        (0, 0), (2, 0), (4, 0),
        (0, 1), (2, 1), (4, 1),
        (0, 2), (2, 2), (4, 2),
        (0, 3), (2, 3), (4, 3),
        (1, 4), (3, 4),
    ],
    "R": [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3),
        (0, 4), (2, 4),
    ],
    "D": [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 0), (1, 0), (2, 4), (3, 4),
        (0, 4), (1, 4),
    ],
    "S": [
        (1, 0), (2, 0), (3, 0),
        (0, 1),
        (0, 2), (3, 2),
        (3, 3),
        (1, 4), (2, 4), (3, 4),
    ],
    "F": [
        (0, 0), (1, 0), (2, 0),
        (0, 1),
        (0, 2), (1, 2), (2, 2),
        (0, 3),
        (0, 4),
    ],
    "G": [
        (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1),
        (0, 2), (2, 2), (3, 2),
        (0, 3), (4, 3),
        (1, 4), (2, 4), (3, 4),
        (4, 4),
        (4, 2),
    ],
    "I": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "J": [
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3), (0, 3),
        (3, 4), (2, 4), (2, 4), (1, 4)
    ],
    "K": [
        (0, 0), (3, 0),
        (0, 1), (2, 1),
        (0, 2), (1, 2),
        (0, 3), (2, 3),
        (0, 4), (3, 4),
    ],
    "M": [
        (1, 0), (3, 0),
        (0, 1), (2, 1), (4, 1),
        (0, 2), (2, 2), (4, 2),
        (0, 3), (2, 3), (4, 3),
        (0, 4), (2, 4), (4, 4),
    ],
    "N": [
        (4, 0), (1, 1), (0, 0),
        (4, 1), (2, 2), (0, 1),
        (4, 2), (3, 3), (0, 2),
        (4, 3), (0, 3),
        (4, 4), (0, 4),
    ],
    "P": [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3),
        (0, 4),
    ],
    "Q": [
        (1, 0), (2, 0), (3, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (1, 4), (2, 4), (3, 4),
        (3, 3),
        (4, 4),
        (2, 2),
    ],
    "S": [
        (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1),
        (1, 2), (2, 2), (3, 2),
        (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4),
    ],
    "T": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
    ],
    "U": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (1, 4), (2, 4), (3, 4),
    ],
    "V": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (1, 3), (3, 3),
        (2, 4),
    ],
    "W": [
        (0, 0), (2, 0), (4, 0),
        (0, 1), (2, 1), (4, 1),
        (0, 2), (2, 2), (4, 2),
        (0, 3), (2, 3), (4, 3),
        (1, 4), (3, 4),
    ],
    "X": [
        (0, 0), (4, 0),
        (1, 1), (3, 1),
        (2, 2),
        (1, 3), (3, 3),
        (0, 4), (4, 4)
    ],
    "Y": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (1, 2), (3, 2),
        (2, 3),
        (2, 4),
    ],
    "Z": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (3, 1),
        (2, 2),
        (1, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "1": [
        (0, 0), (1, 0), (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "2": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "3": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "4": [
        (0, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (4, 3),
        (4, 4),
    ],
    "5": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "6": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "7": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (4, 1),
        (4, 2),
        (3, 3),
        (3, 4),
    ],
    "8": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "9": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (4, 3),
        (4, 4),
    ],
    "0": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (4, 1),
        (0, 2), (4, 2),
        (0, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "+": [
        (2, 0),
        (2, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (2, 3),
        (2, 4),
    ],
    "-": [
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    ],
    "=": [
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    ],
    "*": [
        (2, 0),
        (2, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (2, 3),
        (2, 4),
        (1, 1),
        (0, 0),
        (4, 0),
        (3, 1),
        (4, 4),
        (0, 4),
        (3, 3),
        (1, 3),
    ],
    "d": [
        (3, 0),
        (3, 1),
        (2, 2),
        (1, 3),
        (1, 4),
    ],
    ".": [
        (0, 4),
    ],
    "?": [
        (0, 0), (1, 0), (2, 0),
        (2, 1),
        (1, 2), (2, 2),
        (1, 4)
    ],
    "!": [
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 4)
    ],
    ":": [
        (2, 1),
        (2, 3),
    ],
    ";": [
        (2, 1),
        (2, 3),
        (2, 4),
    ],
    ",": [
        (2, 3),
        (1, 4),
    ],
    "l": [
        (1, 0), (2, 0),
        (1, 1),
        (1, 2), (0, 2),
        (1, 3),
        (1, 4), (2, 4),
    ],
    "r": [
        (3, 0), (2, 0),
        (3, 1),
        (3, 2), (4, 2),
        (3, 3),
        (3, 4), (2, 4),
    ],
    "[": [
        (1, 0), (2, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4), (2, 4),
    ],
    "]": [
        (3, 0), (2, 0),
        (3, 1),
        (3, 2),
        (3, 3),
        (3, 4), (2, 4),
    ],
    "q": [
        (1, 1), (3, 1),
        (1, 2), (3, 2)
    ],
    "w": [
        (2, 1),
        (2, 2),
    ],
    "g": [
        (2, 0), (3, 0), (4, 0),
        (1, 1),
        (0, 2),
        (1, 3),
        (2, 4), (3, 4), (4, 4),
    ],
    "h": [
        (0, 0), (1, 0), (2, 0),
        (3, 1),
        (4, 2),
        (3, 3),
        (0, 4), (1, 4), (2, 4),
    ],
    "j": [
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
    ],
    "k": [
        (1, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (3, 4),
    ],
    "s": [
        (3, 0),
        (3, 1),
        (2, 2),
        (1, 3),
        (1, 4),
    ],
    "░": [
        (0, 0), (2, 0), (4, 0),
        (0, 2), (2, 2), (4, 2),
        (0, 4), (2, 4), (4, 4),
    ],
    "▒": [
        (0, 0), (2, 0), (4, 0),
        (1, 1), (3, 1),
        (0, 2), (2, 2), (4, 2),
        (1, 3), (3, 3),
        (0, 4), (2, 4), (4, 4),
    ],
    "▓": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (1, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (1, 3), (3, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "█": [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
        (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    ],
    "─": [
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "│": [
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
    ],
    "┌": [
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┐": [
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (2, 2), (1, 2), (0, 2), (-1, 2),
    ],
    "└": [
        (2, 2), (2, 1), (2, 0), (2, -1), (2, -2), (2, -3),
        (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┘": [
        (2, 2), (2, 1), (2, 0), (2, -1), (2, -2), (2, -3),
        (2, 2), (1, 2), (0, 2), (-1, 2),
    ],
    "├": [
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┤": [
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (2, 2), (1, 2), (0, 2), (-1, 2),
    ],
    "┬": [
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┴": [
        (2, -2), (2, -1), (2, 0), (2, 1), (2, 2),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
    ],
    "┼": [
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
    ],
    " ": [],
}






def display_character(x, y, char, color, scale=2):
    """Display a character on the screen by drawing its corresponding pixels."""
    if char in font_map:
        for (dx, dy) in font_map[char]:
            for ix in range(scale):
                for iy in range(scale):
                    graphics(x + dx * scale + ix, y + dy * scale + iy, color)

def display_text(x, y, text, color, scale=2):
    """Display a string of text at the given position."""
    posE = x
    position = x
    positiony = y
    for char in text:
        if char == "/":
            positiony = positiony + (8 * scale)
            position = posE
        display_character(position, positiony, char, color, scale)
        if not char == "/":
            position += (6 * scale)

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chatter Display")

PALETTE = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (128, 128, 128),
    "red": (255, 0, 0),
    "dark_red": (139, 0, 0),
    "light_red": (255, 102, 102),
    "green": (0, 255, 0),
    "dark_green": (0, 100, 0),
    "light_green": (144, 238, 144),
    "blue": (0, 0, 255),
    "dark_blue": (0, 0, 139),
    "light_blue": (173, 216, 230),
    "cyan": (0, 255, 255),
    "dark_cyan": (0, 139, 139),
    "light_cyan": (224, 255, 255),
    "yellow": (255, 255, 0),
    "dark_yellow": (204, 204, 0),
    "light_yellow": (255, 255, 153),
}


for color_name, rgb in PALETTE.items():
    globals()[color_name] = rgb
def graphics(x, y, color):
    """
    Set a pixel at (x, y) to a specific color (RGB).
    Args:
    - x (int): X coordinate on the screen.
    - y (int): Y coordinate on the screen.
    - color (tuple): A tuple of RGB values (r, g, b).
    """
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        screen.set_at((int(x), int(y)), color)

def display_screen():
    """
    Update the screen to reflect the current graphics drawn.
    """
    pygame.display.update()

def load_sprite(image_path):
    """
    Loads a sprite (image) from the given file path.
    Args:
    - image_path (str): The file path of the image to be loaded.
    
    Returns:
    - pygame.Surface: A Surface object representing the loaded image.
    """
    try:
        sprite = pygame.image.load(image_path)
        return sprite
    except pygame.error as e:
        print(f"Error loading image {image_path}: {e}")
        return None


def display_sprite(sprite, x, y, scale=1):
    """
    Displays a sprite at the specified coordinates on the screen, with an optional scaling factor.
    
    Args:
    - sprite (pygame.Surface): The sprite (image) to be displayed.
    - x (int): The x-coordinate where the sprite should be placed.
    - y (int): The y-coordinate where the sprite should be placed.
    - scale (int): The factor by which the sprite should be scaled (default is 1, meaning no scaling).
    """
    if sprite:
        # Scale the sprite based on the scale factor
        scaled_sprite = pygame.transform.scale(sprite, (sprite.get_width() * scale, sprite.get_height() * scale))
        screen.blit(scaled_sprite, (x, y))


def display_line(x1, y1, x2, y2, color):
    """
    Draw a line from (x1, y1) to (x2, y2) with the given color.
    Args:
    - x1, y1 (int): Starting point of the line.
    - x2, y2 (int): Ending point of the line.
    - color (tuple): A tuple of RGB values for the line color.
    """
    pygame.draw.line(screen, color, (x1, y1), (x2, y2))

def audio(frequency, duration):
    """
    Play a sound at a specific frequency for a given duration.
    Args:
    - frequency (int): The frequency of the sound in Hz.
    - duration (float): The duration of the sound in seconds.
    """
    sample_rate = 44100
    amplitude = 32767
    samples_count = int(sample_rate * duration)


    t = np.linspace(0, duration, samples_count, endpoint=False)
    waveform = (amplitude * np.sin(2 * np.pi * frequency * t)).astype(np.int16)

    stereo_waveform = np.column_stack((waveform, waveform))

    sound = pygame.mixer.Sound(stereo_waveform)
    sound.play()
    pygame.time.delay(int(duration * 1000))
    sound.stop()


# To store the keys being pressed
keys_pressed = []

keys_pressed = []

def snapshot_input():
    """
    Returns a snapshot of the keys that are currently pressed, updating continuously
    while a key is held down. It works for every key on the keyboard.
    """
    global keys_pressed

    # Poll for all pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None
        
        if event.type == pygame.KEYDOWN:  # A key is pressed
            key_name = pygame.key.name(event.key)
            if key_name not in keys_pressed:  # Avoid duplicate key presses
                keys_pressed.append(key_name)
        
        elif event.type == pygame.KEYUP:  # A key is released
            key_name = pygame.key.name(event.key)
            if key_name in keys_pressed:  # Remove the key from the pressed list
                keys_pressed.remove(key_name)

    # Return all keys that are currently pressed
    return tuple(keys_pressed)  # Return as a tuple of keys



def input():
    """
    Check for any key press and return the name of the key pressed.
    Returns:
    - (str): The name of the key pressed (e.g., 'a', 'space', etc.).
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None
        if event.type == pygame.KEYDOWN:
            return pygame.key.name(event.key)
    return ""

def clear(color):
    screen.fill(color)

def get_mouse_position():
    """
    Get the current mouse position (X, Y).
    Returns:
    - (tuple): A tuple containing the current mouse position (X, Y).
    """
    return pygame.mouse.get_pos()

def get_mouse_state():
    """
    Get the state of the mouse (clicking and scrolling).
    Returns:
    - (dict): A dictionary with keys:
        - 'left_click': Boolean indicating if the left mouse button was clicked.
        - 'right_click': Boolean indicating if the right mouse button was clicked.
        - 'scroll_up': Boolean indicating if the scroll wheel was scrolled up.
        - 'scroll_down': Boolean indicating if the scroll wheel was scrolled down.
    """
    mouse_state = {
        'left_click': False,
        'right_click': False,
        'scroll_up': False,
        'scroll_down': False
    }

    # Check mouse button states
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # Left button pressed
        mouse_state['left_click'] = True
    if mouse_buttons[2]:  # Right button pressed
        mouse_state['right_click'] = True

    # Check for scroll wheel events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                mouse_state['scroll_up'] = True
            elif event.button == 5:  # Scroll down
                mouse_state['scroll_down'] = True

    return mouse_state

# Initialize joystick
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None
    print("No joystick detected!")


