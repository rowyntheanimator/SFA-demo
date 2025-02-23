import chatter
import time
import sys
import subprocess
import json


def display_character(x, y, char, color, scale=2):
    chatter.display_character(x, y, char, color, scale)

def display_text(x, y, text, color, scale=2):
    chatter.display_text(x, y, text, color, scale)



chatter.clear(chatter.black)
display_text(0, 10, "LOADING...", chatter.green, 2)
chatter.display_screen()
player = chatter.load_sprite("assets\\player.png")
grass_block = chatter.load_sprite("assets\\grass.png")
stone_block = chatter.load_sprite("assets\\stone.png")
walker = chatter.load_sprite("assets\\walker.png")
eme = chatter.load_sprite("assets\\live.png")
coin = chatter.load_sprite("assets\\coin.png")
underground_back_1 = chatter.load_sprite("assets\\back_level_2_B.png")
underground_back_2 = chatter.load_sprite("assets\\back_level_2_C.png")
nan = chatter.load_sprite("assets\\nan.png")
invis = chatter.load_sprite("assets\\Invincibility.png")
player_ane_invis_1 = chatter.load_sprite("assets\\player_invis1.png")
player_ane_invis_2 = chatter.load_sprite("assets\\player_invis2.png")
player_ane_invis_3 = chatter.load_sprite("assets\\player_invis3.png")
player_ane_invis_4 = chatter.load_sprite("assets\\player_invis4.png")
player_ane_invis_5 = chatter.load_sprite("assets\\player_invis5.png")
player_ane_invis_6 = chatter.load_sprite("assets\\player_invis6.png")
lava = chatter.load_sprite("assets\\lava.png")
rock = chatter.load_sprite("assets\\rock.png")
player_rock = chatter.load_sprite("assets\\player_rock.png")
boss = chatter.load_sprite("assets\\player_invis6.png")
shooter = chatter.load_sprite("assets\\shooter.png")
arrow = chatter.load_sprite("assets\\arrow.png")
poison_shooter = chatter.load_sprite("assets\\shooter_poison.png")
poison_arrow = chatter.load_sprite("assets\\poison_arrow.png")
player_white = chatter.load_sprite("assets\\player_white.png")
arrow_l = chatter.load_sprite("assets\\arrow_l.png")
poison_arrow_l = chatter.load_sprite("assets\\poison_arrow_l.png")
player_crouching = chatter.load_sprite("assets\\player_c.png")
arrow_walker = chatter.load_sprite("assets\\arrow_walker.png")
grava_shooter = chatter.load_sprite("assets\\grava_shooter.png")
gravaton = chatter.load_sprite("assets\\gravaton.png")
gravaton1 = chatter.load_sprite("assets\\gravaton1.png")
gravaton2 = chatter.load_sprite("assets\\gravaton2.png")
gravaton3 = chatter.load_sprite("assets\\gravaton3.png")
gravaton4 = chatter.load_sprite("assets\\gravaton4.png")
gravaton5 = chatter.load_sprite("assets\\gravaton5.png")
gravaton6 = chatter.load_sprite("assets\\gravaton6.png")
gravaton7 = chatter.load_sprite("assets\\gravaton7.png")
grava_shooterL = chatter.load_sprite("assets\\grava_shooter_L.png")
grava_shooterR = chatter.load_sprite("assets\\grava_shooter_R.png")
grava_shooterU = chatter.load_sprite("assets\\grava_shooter_U.png")
col = []

def draw_collision_boundary(x, y, player_width, player_height, scale, color):
    """Draws the boundary around the player's collision area."""
    scaled_player_width = player_width * scale
    scaled_player_height = player_height * scale

    # Draw the four sides of the boundary rectangle
    chatter.display_line(x, y, x + scaled_player_width, y, color)  # Top side
    chatter.display_line(x, y, x, y + scaled_player_height, color)  # Left side
    chatter.display_line(x + scaled_player_width, y, x + scaled_player_width, y + scaled_player_height, color)  # Right side
    chatter.display_line(x, y + scaled_player_height, x + scaled_player_width, y + scaled_player_height, color)  # Bottom side

def check_collision(x, y, col, player_width, player_height, block_width, block_height, scale):
    """Checks if the player's bounding box collides with any block."""
    for i in range(0, len(col), 2):
        block_x = col[i]
        block_y = col[i + 1]

        # Adjust for scaling
        scaled_player_width = player_width * scale
        scaled_player_height = player_height * scale
        scaled_block_width = block_width * scale
        scaled_block_height = block_height * scale

        # Check if the player's rectangle overlaps with the block's rectangle
        if (block_x < x + scaled_player_width and block_x + scaled_block_width > x and
            block_y < y + scaled_player_height and block_y + scaled_block_height > y):
            return True
    return False

def check_multiple_walker_collisions(player_x, player_y, player_width, player_height, walker_positions, walker_width, walker_height, scale=2):
    """
    Checks for collisions between the player and any Walker in the list of walkers, applying scaling.
    """
    for i in range(0, len(walker_positions), 4):
        walker_x = walker_positions[i]
        walker_y = walker_positions[i + 1]

        # Adjust for scaling
        scaled_player_width = player_width * scale
        scaled_player_height = player_height * scale
        scaled_walker_width = walker_width * scale
        scaled_walker_height = walker_height * scale

        # Check if the player's rectangle overlaps with the walker's rectangle
        if (walker_x < player_x + scaled_player_width and walker_x + scaled_walker_width > player_x and
            walker_y < player_y + scaled_player_height and walker_y + scaled_walker_height > player_y):
            return True  # Collision detected
    
    return False  # No collision

print()

def draw_walker_boundaries(walker_positions, walker_width, walker_height, scale, color, size):
    """
    Draws the boundaries of all Walkers in the game.
    
    walker_positions: List of Walkers' X and Y positions (alternating: [x1, y1, x2, y2, ...])
    walker_width: Width of a Walker.
    walker_height: Height of a Walker.
    scale: Scaling factor for Walker size.
    color: Color of the boundary lines.
    """
    for i in range(0, len(walker_positions), size):
        walker_x = walker_positions[i]
        walker_y = walker_positions[i + 1]

        # Adjust for scaling
        scaled_walker_width = walker_width * scale
        scaled_walker_height = walker_height * scale

        # Draw the four sides of the Walkers' boundary rectangle
        chatter.display_line(walker_x, walker_y, walker_x + scaled_walker_width, walker_y, color)  # Top side
        chatter.display_line(walker_x, walker_y, walker_x, walker_y + scaled_walker_height, color)  # Left side
        chatter.display_line(walker_x + scaled_walker_width, walker_y, walker_x + scaled_walker_width, walker_y + scaled_walker_height, color)  # Right side
        chatter.display_line(walker_x, walker_y + scaled_walker_height, walker_x + scaled_walker_width, walker_y + scaled_walker_height, color)  # Bottom side

def draw_gravaton_boundaries(walker_positions, walker_width, walker_height, scale, color, size):

    for i, (x_arrow, y_arrow, dir_a) in enumerate(gravaton_pos):

        # Adjust for scaling
        scaled_walker_width = walker_width * scale
        scaled_walker_height = walker_height * scale

        # Draw the four sides of the Walkers' boundary rectangle
        chatter.display_line(x_arrow, y_arrow, x_arrow + scaled_walker_width, y_arrow, color)  # Top side
        chatter.display_line(x_arrow, y_arrow, x_arrow, y_arrow + scaled_walker_height, color)  # Left side
        chatter.display_line(x_arrow + scaled_walker_width, y_arrow, x_arrow + scaled_walker_width, y_arrow + scaled_walker_height, color)  # Right side
        chatter.display_line(x_arrow, y_arrow + scaled_walker_height, x_arrow + scaled_walker_width, y_arrow + scaled_walker_height, color)  # Bottom side


no_gravity_player = False

def handle_player_movement(x, y, pressed_keys, speed, scale, col, player_width, player_height, block_width, block_height, gravity, jump_force, max_jump_speed, jump_acceleration):
    """Handles player movement with gravity, jump timer, and checks for collisions."""
    global no_gravity_player
    px = x  # Store previous x
    py = y  # Store previous y
    velocity_y = 0  # Vertical velocity starts at 0
    velocity_x = 0  # Horizontal velocity starts at 0
    on_ground = False  # Variable to track if the player is on the ground
    jump_timer = 0  # Timer to track jump duration
    max_jump_duration = 30  # Maximum number of frames the jump can last

    if not check_collision(x, y + player_height + 1 - 39, col, player_width, player_height, block_width, block_height, scale):
        on_ground = False  # Mark that the player is not on the ground
    else:
        on_ground = True
        jump_timer = 0  # Reset the jump timer when the player lands

    # Horizontal movement (left and right)
    if Player_con_A in pressed_keys:
        velocity_x = -speed  # Move left
    elif Player_con_D in pressed_keys:
        velocity_x = speed  # Move right
    
    if no_gravity_player:
        if Player_con_W in pressed_keys:
            velocity_y = -speed  # Move left
        elif Player_con_S in pressed_keys:
            velocity_y = speed  # Move right

    # Jumping logic with timer
    if Player_con_SPACE in pressed_keys and on_ground:
        jump_timer = 1  # Start the jump timer
        on_ground = False  # The player is no longer on the ground

    if jump_timer > 0:  # If the player is in the middle of a jump
        if jump_timer <= max_jump_duration:  # Limit the jump duration
            # Calculate the upward velocity for this frame based on the timer
            velocity_y = -jump_force * (1 - jump_timer / max_jump_duration)
            jump_timer += 1  # Increment the timer
        else:
            jump_timer = 0  # Stop the jump when the maximum duration is reached

    # Apply gravity if the player is not affected by no gravity
    if not no_gravity_player:
        if not on_ground and jump_timer == 0:
            velocity_y += gravity  # Gravity pulls the player down

    # Check for ground collision (standing on top of a platform)
    if check_collision(x, y + velocity_y, col, player_width, player_height, block_width, block_height, scale):
        if velocity_y > 0:  # Falling and colliding with the ground
            y = py  # Reset y to previous position (before collision)
            velocity_y = 0  # Stop vertical movement
            on_ground = True  # Mark the player as on the ground
        elif velocity_y < 0:  # If moving up and hitting something above (head collision)
            velocity_y = 0  # Stop upward movement

    # Check for horizontal collisions with walls (left/right)
    if check_collision(x + velocity_x, y, col, player_width, player_height, block_width, block_height, scale):
        velocity_x = 0  # Stop horizontal movement if collision is detected
        x = px

    # Update the player position after collision checks
    y += velocity_y  # Apply vertical velocity
    x += velocity_x  # Apply horizontal velocity
    x = max(0, min(x, 700))  # Keep the player within screen bounds

    return x, y, velocity_x, velocity_y, on_ground, jump_timer




def check_one_collision(x1, y1, width1, height1, x2, y2, width2, height2, scale1=1, scale2=1, debug=False):
    """
    Check if two objects are colliding based on their positions and dimensions.
    
    :param x1, y1: Coordinates of the first object.
    :param width1, height1: Dimensions of the first object.
    :param x2, y2: Coordinates of the second object.
    :param width2, height2: Dimensions of the second object.
    :param scale1, scale2: Scale factors for the objects (default is 1 for both objects).
    :return: True if the objects are colliding, False otherwise.
    """
    # Apply the scale factors to the dimensions
    width1 *= scale1
    height1 *= scale1
    width2 *= scale2
    height2 *= scale2

    # Debug: Print scaled dimensions

    # Check for overlap in both x and y axes
    if (x1 + width1 > x2 and x1 < x2 + width2 and
        y1 + height1 > y2 and y1 < y2 + height2):
        return True  # Objects are colliding
    else:
        return False  # No collision

print()




def draw_block_boundaries(col, block_width, block_height, scale, color):
    """Draws the boundaries of all blocks in the world."""
    for i in range(0, len(col), 2):
        block_x = col[i]
        block_y = col[i + 1]

        # Adjust for scaling
        scaled_block_width = block_width * scale
        scaled_block_height = block_height * scale

        # Draw the four sides of the block's boundary rectangle
        chatter.display_line(block_x, block_y, block_x + scaled_block_width, block_y, color)  # Top side
        chatter.display_line(block_x, block_y, block_x, block_y + scaled_block_height, color)  # Left side
        chatter.display_line(block_x + scaled_block_width, block_y, block_x + scaled_block_width, block_y + scaled_block_height, color)  # Right side
        chatter.display_line(block_x, block_y + scaled_block_height, block_x + scaled_block_width, block_y + scaled_block_height, color)  # Bottom side

times = 0

background_color = (0, 255, 255)
back_sprite = nan

lava_pos = []

rock_pos = []

boss_pos = []

shooter_pos = []

poison_shooter_pos = []

arrow_walker_pos = []

grava_shooter_pos = []

grava_shooter_posL = []

grava_shooter_posR = []

grava_shooter_posU = []

spawn_pos_x = 0
spawn_pos_y = 0

level_1_A = [(0, 492, 1), (0, 533, 2), (0, 574, 2), (0, 615, 2), (0, 656, 2), (48, 656, 1), (96, 656, 1), (144, 656, 1), (192, 615, 2), (192, 656, 2), (240, 656, 2), (288, 656, 2), (288, 615, 2), (288, 574, 2), (432, 656, 2), (432, 615, 2), (432, 574, 1), (480, 656, 1), (528, 656, 2), (528, 533, 2), (528, 492, 2), (528, 451, 1), (576, 656, 2), (576, 533, 2), (576, 492, 2), (576, 451, 1), (624, 656, 2), (624, 533, 2), (624, 492, 2), (624, 451, 1), (672, 656, 2), (672, 615, 2), (672, 574, 1)]
level_1_B = [(0, 492, 1), (0, 533, 2), (0, 574, 2), (0, 615, 2), (0, 656, 2), (48, 656, 1), (96, 656, 1), (144, 656, 1), (192, 615, 2), (192, 656, 2), (240, 656, 2), (288, 656, 2), (288, 615, 2), (288, 574, 2), (432, 656, 2), (432, 615, 2), (432, 574, 1), (480, 656, 1), (528, 656, 2), (528, 533, 2), (528, 492, 2), (528, 451, 1), (576, 656, 2), (576, 533, 2), (576, 492, 2), (576, 451, 1), (624, 656, 2), (624, 533, 2), (624, 492, 2), (624, 451, 1), (672, 656, 2)]
level_2_A = [(0, 492, 1), (0, 533, 2), (0, 574, 2), (0, 615, 2), (0, 656, 2), (48, 656, 1), (96, 656, 1), (144, 656, 1), (192, 656, 2), (192, 615, 2), (192, 410, 2), (240, 656, 2), (240, 410, 2), (288, 656, 2), (288, 410, 2), (336, 656, 2), (336, 410, 2), (384, 656, 2), (384, 615, 2), (384, 410, 2), (432, 656, 2), (432, 410, 2), (480, 656, 2), (480, 410, 2), (528, 656, 2), (528, 410, 2), (576, 656, 2), (576, 410, 2), (624, 656, 2), (624, 410, 2), (672, 656, 2), (672, 410, 2), (672, 615, 2)]
level_2_B = [(0, 656, 2), (0, 410, 2), (48, 410, 2), (96, 656, 2), (96, 410, 2), (144, 410, 2), (192, 656, 2), (192, 615, 2), (192, 410, 2), (240, 656, 2), (240, 410, 2), (288, 656, 2), (288, 410, 2), (336, 656, 2), (336, 410, 2), (384, 656, 2), (384, 615, 2), (384, 410, 2), (432, 656, 2), (432, 410, 2), (480, 656, 2), (480, 410, 2), (528, 656, 2), (528, 410, 2), (576, 656, 2), (576, 410, 2), (624, 656, 2), (624, 410, 2), (672, 656, 2), (672, 410, 2), (672, 615, 2)]
level_3_A = [(0, 533, 2), (0, 574, 2), (0, 615, 2), (0, 656, 2), (336, 656, 1), (384, 656, 1), (432, 656, 1), (480, 656, 1), (528, 656, 1), (672, 656, 2), (96, 656, 2), (48, 656, 2), (96, 615, 2), (144, 574, 2), (192, 533, 2), (0, 492, 2), (0, 451, 2), (0, 410, 2), (0, 369, 2), (0, 328, 2), (0, 287, 2), (0, 246, 2), (0, 205, 2), (0, 164, 2), (0, 123, 2), (0, 82, 2), (0, 0, 2), (0, 41, 2), (48, 492, 2), (192, 574, 2), (144, 656, 2), (192, 656, 2), (240, 656, 2), (288, 656, 2), (288, 615, 2), (240, 574, 2), (240, 615, 2), (192, 615, 2), (144, 615, 2), (240, 492, 2), (576, 656, 2), (624, 656, 2), (576, 615, 2), (624, 410, 1), (576, 410, 1), (528, 410, 1), (480, 410, 1), (432, 410, 1), (384, 410, 1), (336, 451, 1), (672, 410, 2), (672, 410, 2), (672, 369, 2), (672, 328, 2), (672, 287, 2), (672, 246, 2), (672, 205, 2), (672, 164, 2), (672, 123, 2), (672, 82, 2), (672, 41, 2), (672, 0, 2), (48, 533, 2), (48, 574, 2), (48, 615, 2)]
level_3_B = [(672, 656, 2), (96, 410, 2), (144, 410, 2), (192, 410, 2), (240, 410, 2), (288, 410, 2), (336, 410, 2), (384, 410, 2), (432, 410, 2), (480, 410, 2), (528, 410, 2), (576, 410, 2), (624, 410, 2), (672, 410, 2), (0, 656, 2), (48, 656, 2), (96, 656, 2), (288, 656, 2), (480, 656, 2), (624, 656, 2), (672, 615, 2), (48, 615, 2), (48, 410, 2), (0, 410, 2), (240, 656, 2), (432, 656, 2)]
level_3_C = [(672, 656, 2), (96, 410, 2), (144, 410, 2), (0, 656, 2), (48, 656, 2), (96, 656, 2), (624, 656, 2), (48, 410, 2), (0, 410, 2), (576, 656, 2), (144, 656, 2), (144, 615, 2), (336, 656, 2), (384, 656, 2), (288, 656, 6)]
level_3_D = [(672, 656, 2), (0, 656, 2), (48, 656, 2), (96, 656, 2), (624, 656, 2), (576, 656, 2), (144, 656, 2), (528, 656, 2), (336, 656, 2), (144, 615, 1), (576, 615, 1), (624, 615, 1), (672, 615, 1), (96, 615, 1), (48, 615, 1), (0, 615, 1), (192, 656, 6), (240, 656, 6), (288, 656, 6), (480, 656, 6), (432, 656, 6), (384, 656, 2)]
level_4_A = [(0, 656, 2), (48, 656, 2), (96, 656, 2), (144, 656, 2), (576, 574, 8), (480, 656, 2), (528, 656, 2), (576, 656, 2), (672, 656, 2), (624, 656, 2), (384, 656, 2), (336, 656, 2), (288, 656, 2), (240, 656, 2), (192, 656, 2), (432, 656, 2)]
level_5_A = [(0, 656, 2), (48, 656, 2), (240, 656, 2), (288, 656, 2), (384, 656, 2), (432, 656, 2), (624, 656, 2), (672, 656, 2), (48, 615, 2), (0, 615, 2), (336, 656, 2), (240, 615, 2), (288, 615, 2), (384, 615, 2), (432, 615, 2), (672, 615, 2), (96, 615, 2), (336, 615, 6)]
level_5_B = [(0, 656, 2), (48, 656, 2), (288, 656, 2), (384, 656, 2), (432, 656, 2), (624, 656, 2), (672, 656, 2), (672, 615, 2), (624, 615, 2), (576, 656, 2), (576, 615, 2), (528, 615, 2), (528, 656, 2), (480, 615, 2), (480, 656, 2), (432, 615, 2), (384, 615, 2), (288, 615, 2), (192, 656, 2), (96, 656, 2), (96, 615, 2), (192, 615, 2), (48, 615, 2), (0, 615, 2), (0, 410, 2), (48, 410, 2), (96, 410, 2), (144, 410, 2), (192, 410, 2), (240, 410, 2), (288, 410, 2), (336, 410, 2), (384, 410, 2), (432, 410, 2), (480, 410, 2), (480, 410, 2), (576, 410, 2), (528, 410, 2), (624, 410, 2), (672, 410, 2), (432, 451, 12), (480, 451, 12), (528, 451, 12), (576, 451, 11)]
level_5_C = [(0, 656, 2), (48, 656, 2), (288, 656, 2), (384, 656, 2), (432, 656, 2), (624, 656, 2), (672, 656, 2), (672, 615, 2), (624, 615, 2), (432, 615, 2), (384, 615, 2), (288, 615, 2), (192, 656, 2), (96, 656, 2), (96, 615, 2), (192, 615, 2), (48, 615, 2), (0, 615, 2), (336, 615, 2), (336, 656, 2), (240, 656, 2), (240, 615, 2), (144, 615, 2), (144, 656, 2), (192, 574, 2), (432, 574, 2), (480, 369, 2), (528, 369, 2), (528, 369, 2), (576, 369, 2), (624, 369, 2), (672, 369, 2), (432, 369, 2), (384, 369, 2), (384, 369, 2), (384, 369, 2), (336, 369, 2), (288, 369, 2), (240, 369, 2), (192, 369, 2), (192, 369, 2), (144, 369, 2), (144, 369, 2), (96, 369, 2), (96, 369, 2), (48, 369, 2), (0, 369, 2), (384, 410, 12), (240, 410, 12)]
level_5_D = [(0, 656, 2), (48, 656, 2), (624, 656, 2), (672, 656, 2), (672, 615, 2), (624, 615, 2), (96, 656, 2), (96, 615, 2), (48, 615, 2), (0, 615, 2), (144, 615, 2), (144, 656, 2), (480, 656, 2), (528, 656, 2), (576, 656, 2), (576, 615, 2), (528, 615, 2), (480, 615, 2), (432, 656, 6), (384, 656, 6), (336, 656, 6), (288, 656, 6), (240, 656, 6), (192, 656, 6), (192, 615, 6), (240, 615, 6), (384, 615, 6), (432, 615, 6), (288, 615, 2), (336, 615, 2), (144, 574, 2), (528, 574, 2), (672, 369, 2), (624, 369, 2), (576, 369, 2), (528, 369, 2), (528, 369, 2), (528, 369, 2), (480, 369, 2), (432, 369, 2), (384, 369, 2), (336, 369, 2), (288, 369, 2), (240, 369, 2), (192, 369, 2), (144, 369, 2), (96, 369, 2), (48, 369, 2), (0, 369, 2)]
level_6_A = [(0, 656, 2), (48, 656, 2), (624, 656, 2), (672, 656, 2), (672, 615, 2), (624, 615, 2), (96, 656, 2), (96, 615, 2), (48, 615, 2), (0, 615, 2), (144, 615, 2), (144, 656, 2), (480, 656, 2), (528, 656, 2), (576, 656, 2), (576, 615, 2), (528, 615, 2), (480, 615, 2), (288, 615, 2), (336, 615, 2), (672, 369, 2), (624, 369, 2), (576, 369, 2), (528, 369, 2), (528, 369, 2), (528, 369, 2), (480, 369, 2), (432, 369, 2), (384, 369, 2), (336, 369, 2), (288, 369, 2), (240, 369, 2), (192, 369, 2), (144, 369, 2), (96, 369, 2), (48, 369, 2), (0, 369, 2), (336, 656, 2), (384, 656, 2), (432, 656, 2), (432, 615, 2), (384, 615, 2), (288, 656, 2), (240, 656, 2), (192, 656, 2), (192, 615, 2), (240, 615, 2), (624, 574, 2), (144, 574, 2)]
level_6_B = [(0, 656, 2), (48, 656, 2), (624, 656, 2), (672, 656, 2), (672, 615, 2), (624, 615, 2), (96, 656, 2), (96, 615, 2), (48, 615, 2), (0, 615, 2), (144, 615, 2), (144, 656, 2), (384, 615, 2), (336, 615, 2), (288, 615, 2), (240, 615, 2), (192, 615, 2), (192, 615, 2), (192, 656, 2), (240, 656, 2), (240, 656, 2), (288, 656, 2), (336, 656, 2), (336, 656, 2), (384, 656, 2), (192, 574, 2), (192, 533, 2), (336, 410, 2), (384, 369, 2), (384, 410, 2), (432, 574, 2), (576, 574, 2), (576, 656, 6), (576, 615, 6), (432, 615, 6), (480, 615, 6), (528, 615, 6), (528, 656, 6), (480, 656, 6), (432, 656, 6), (672, 451, 2), (672, 451, 2), (672, 410, 2), (624, 410, 2), (624, 369, 2), (672, 369, 2), (240, 574, 2), (240, 533, 2), (240, 492, 2), (144, 574, 2), (288, 451, 2), (288, 492, 2), (288, 533, 2), (288, 574, 2), (624, 451, 14)]
level_6_C = [(0, 656, 2), (48, 656, 2), (624, 656, 2), (672, 656, 2), (672, 615, 2), (624, 615, 2), (96, 656, 2), (96, 615, 2), (48, 615, 2), (0, 615, 2), (144, 615, 2), (144, 656, 2), (384, 615, 2), (336, 615, 2), (288, 615, 2), (240, 615, 2), (192, 615, 2), (192, 615, 2), (192, 656, 2), (240, 656, 2), (240, 656, 2), (288, 656, 2), (336, 656, 2), (336, 656, 2), (384, 656, 2), (432, 656, 2), (480, 656, 2), (480, 656, 2), (528, 656, 2), (576, 656, 2), (576, 615, 2), (528, 615, 2), (480, 615, 2), (432, 615, 2), (144, 492, 2), (144, 451, 2), (240, 451, 2), (240, 492, 2), (240, 533, 2), (144, 410, 2), (144, 369, 2), (144, 328, 2), (192, 328, 2), (240, 328, 2), (144, 328, 2), (144, 287, 2), (144, 246, 2), (144, 205, 2), (192, 205, 2), (240, 205, 2), (288, 205, 2), (336, 246, 2), (336, 205, 2), (336, 287, 2), (336, 328, 2), (336, 451, 2), (336, 492, 2), (384, 492, 2), (432, 492, 2), (384, 369, 2), (432, 369, 2), (384, 205, 2), (432, 205, 2), (480, 205, 2), (528, 205, 2), (528, 328, 2), (528, 369, 2), (528, 410, 2), (528, 451, 2), (528, 574, 2), (576, 328, 2), (576, 205, 2), (624, 205, 2), (624, 205, 2), (672, 205, 2), (672, 246, 2), (672, 287, 2), (672, 328, 2), (672, 369, 2), (672, 451, 2), (672, 492, 2), (576, 492, 2), (528, 492, 2), (336, 369, 2), (240, 574, 2), (240, 574, 14), (336, 369, 14), (672, 287, 14), (528, 574, 14), (528, 410, 14), (192, 205, 13), (480, 205, 13), (672, 410, 2), (528, 533, 2), (528, 533, 15)]
level_6_D = [(0, 656, 2), (48, 656, 2), (96, 656, 2), (144, 656, 2), (192, 656, 2), (240, 656, 2), (288, 656, 2), (336, 656, 2), (384, 656, 2), (432, 656, 2), (480, 656, 2), (528, 656, 2), (576, 656, 2), (624, 656, 2), (672, 656, 2), (672, 615, 2), (432, 615, 2), (384, 615, 2), (0, 615, 2), (48, 615, 2), (144, 615, 2), (192, 615, 2), (240, 615, 2), (384, 615, 2), (432, 615, 2), (528, 615, 2), (576, 615, 2), (624, 615, 2), (672, 615, 2), (96, 615, 2), (288, 615, 2), (336, 615, 2), (480, 615, 2), (288, 574, 2), (288, 533, 2), (192, 492, 2), (192, 451, 2), (192, 410, 2), (192, 369, 2), (192, 328, 2), (192, 287, 2), (192, 246, 2), (192, 205, 2), (192, 164, 2), (192, 123, 2), (192, 82, 2), (192, 41, 2), (192, 0, 2), (240, 0, 2), (336, 0, 2), (432, 0, 2), (528, 0, 2), (576, 0, 2), (624, 0, 2), (672, 0, 2), (672, 41, 2), (672, 41, 2), (672, 82, 2), (720, 82, 2), (672, 123, 2), (672, 164, 2), (672, 205, 2), (672, 246, 2), (672, 287, 2), (672, 328, 2), (672, 410, 2), (672, 369, 2), (672, 451, 2), (672, 492, 2), (288, 451, 2), (288, 492, 2), (288, 410, 2), (288, 369, 2), (288, 328, 2), (384, 328, 2), (384, 369, 2), (384, 287, 2), (288, 287, 2), (288, 246, 2), (384, 246, 2), (384, 246, 2), (384, 205, 2), (384, 164, 2), (384, 123, 2), (384, 82, 2), (384, 41, 2), (384, 0, 2), (480, 246, 2), (480, 287, 2), (480, 328, 2), (480, 369, 2), (480, 369, 2), (480, 410, 2), (480, 451, 2), (480, 492, 2), (480, 533, 2), (480, 574, 2), (576, 369, 2), (576, 328, 2), (576, 287, 2), (576, 246, 2), (576, 205, 2), (576, 164, 2), (576, 123, 2), (576, 82, 2), (576, 41, 2), (288, 574, 14), (480, 574, 14), (576, 41, 14), (384, 41, 14), (480, 0, 2), (288, 0, 2)]

def do_level():
    global level_ID, lev1_A, lev2_A, lev2_B, lev3_A, lev3_B, x, y, walker_pos, times, coins_pos, lives_pos, background_color, back_sprite, invis_pos, col, rock_pos, spawn_pos_x, spawn_pos_y, shooter_pos, poison_shooter_pos, arrow_pos, poison_arrow_pos, grava_shooter_pos, grava_shooter_posL, grava_shooter_posR, grava_shooter_posU
    # Define level data in a dictionary
    level_data = {
        'lev2_A': {'x_range': (652, 695), 'level': level_2_A, 'pos': walker_pos_level_2_A, 'coins_pos': coins_pos_level_2_A, 'lives_pos': lives_pos_level_2_A, 'invis_pos': invis_pos_level_2_A, 'back_sprite': None, 'lev_flag': lev2_A, 'spawn_pos': (150, 500)},
        'lev2_B': {'x_range': (652, 695), 'level': level_2_B, 'pos': walker_pos_level_2_B, 'coins_pos': coins_pos_level_2_B, 'lives_pos': lives_pos_level_2_B, 'invis_pos': invis_pos_level_2_B, 'background_color': (100, 100, 100), 'back_sprite': underground_back_1, 'lev_flag': lev2_B, 'spawn_pos': (150, 500)},
        'lev3_A': {'x_range': (652, 695), 'level': level_3_A, 'pos': walker_pos_level_3_A, 'coins_pos': coins_pos_level_3_A, 'lives_pos': lives_pos_level_3_A, 'invis_pos': invis_pos_level_3_A, 'back_sprite': underground_back_2, 'lev_flag': lev3_A, 'spawn_pos': (150, 500)},
        'lev3_B': {'x_range': (652, 695), 'level': level_3_B, 'pos': walker_pos_level_3_B, 'coins_pos': coins_pos_level_3_B, 'lives_pos': lives_pos_level_3_B, 'invis_pos': invis_pos_level_3_B, 'back_sprite': underground_back_1, 'lev_flag': lev3_B, 'spawn_pos': (150, 500)},
        'lev3_C': {'x_range': (652, 695), 'level': level_3_C, 'pos': walker_pos_level_3_C, 'coins_pos': coins_pos_level_3_C, 'lives_pos': lives_pos_level_3_C, 'invis_pos': invis_pos_level_3_C, 'background_color': (100, 100, 100), 'lev_flag': lev3_C, 'spawn_pos': (150, 500)},
        'lev3_D': {'x_range': (652, 695), 'level': level_3_D, 'pos': walker_pos_level_3_D, 'coins_pos': coins_pos_level_3_D, 'lives_pos': lives_pos_level_3_D, 'invis_pos': invis_pos_level_3_D, 'background_color': (0, 255, 255), 'back_sprite': None, 'lev_flag': lev3_D, 'spawn_pos': (150, 500)},
        'lev4_A': {'x_range': (652, 695), 'level': level_4_A, 'pos': walker_pos_level_4_A, 'coins_pos': coins_pos_level_4_A, 'lives_pos': lives_pos_level_4_A, 'invis_pos': invis_pos_level_4_A, 'background_color': (0, 255, 255), 'back_sprite': None, 'lev_flag': lev4_A, 'spawn_pos': (150, 500)},
        'lev5_A': {'x_range': (652, 695), 'level': level_5_A, 'pos': walker_pos_level_5_A, 'coins_pos': coins_pos_level_5_A, 'lives_pos': lives_pos_level_5_A, 'invis_pos': invis_pos_level_5_A, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev5_A, 'spawn_pos': (100, 500)},
        'lev5_B': {'x_range': (652, 695), 'level': level_5_B, 'pos': walker_pos_level_5_B, 'coins_pos': coins_pos_level_5_B, 'lives_pos': lives_pos_level_5_B, 'invis_pos': invis_pos_level_5_B, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev5_B, 'spawn_pos': (100, 500), 'shooter_pos': [(576, 451)], 'poison_shooter_pos': [(432, 451), (480, 451), (528, 451)]},
        'lev5_C': {'x_range': (652, 695), 'level': level_5_C, 'pos': walker_pos_level_5_C, 'coins_pos': coins_pos_level_5_C, 'lives_pos': lives_pos_level_5_C, 'invis_pos': invis_pos_level_5_C, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev5_C, 'spawn_pos': (100, 500), 'shooter_pos': [], 'poison_shooter_pos': [(384, 410), (240, 410)]},
        'lev5_D': {'x_range': (652, 695), 'level': level_5_D, 'pos': walker_pos_level_5_D, 'coins_pos': coins_pos_level_5_D, 'lives_pos': lives_pos_level_5_D, 'invis_pos': invis_pos_level_5_D, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev5_D, 'spawn_pos': (100, 500), 'shooter_pos': [], 'poison_shooter_pos': [(432, 410), (336, 410), (288, 410), (192, 410)]},
        'lev6_A': {'x_range': (652, 695), 'level': level_6_A, 'pos': walker_pos_level_6_A, 'coins_pos': coins_pos_level_6_A, 'lives_pos': lives_pos_level_6_A, 'invis_pos': invis_pos_level_6_A, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev6_A, 'spawn_pos': (100, 500), 'shooter_pos': [(192, 410), (240, 410), (288, 410), (384, 410), (432, 410), (480, 410), (528, 410), (576, 410)], 'poison_shooter_pos': []},
        'lev6_B': {'x_range': (652, 695), 'level': level_6_B, 'pos': walker_pos_level_6_B, 'coins_pos': coins_pos_level_6_B, 'lives_pos': lives_pos_level_6_B, 'invis_pos': invis_pos_level_6_B, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev6_B, 'spawn_pos': (100, 500), 'shooter_pos': [], 'poison_shooter_pos': []},
        'lev6_C': {'x_range': (652, 695), 'level': level_6_C, 'pos': walker_pos_level_6_C, 'coins_pos': coins_pos_level_6_C, 'lives_pos': lives_pos_level_6_C, 'invis_pos': invis_pos_level_6_C, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev6_C, 'spawn_pos': (100, 500), 'shooter_pos': [], 'poison_shooter_pos': []},
        'lev6_D': {'x_range': (652, 695), 'level': level_6_D, 'pos': walker_pos_level_6_D, 'coins_pos': coins_pos_level_6_D, 'lives_pos': lives_pos_level_6_C, 'invis_pos': invis_pos_level_6_D, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev6_D, 'spawn_pos': (100, 500), 'shooter_pos': [(288, 0), (480, 0), (624, 0)], 'poison_shooter_pos': []},
    }

    # Loop through each level's data
    for level_key, data in level_data.items():
        # Check if the level is not already activated and if the player is within the range
        if x > data['x_range'][0] and x < data['x_range'][1] and not data['lev_flag']:
            arrow_pos = []
            poison_arrow_pos = []
            grava_shooter_pos = []
            grava_shooter_posL = []
            grava_shooter_posR = []
            grava_shooter_posU = []
            # Update global variables
            level_ID = data['level']
            walker_pos = data.get('pos', walker_pos)
            coins_pos = data.get('coins_pos', coins_pos)
            lives_pos = data.get('lives_pos', lives_pos)
            invis_pos = data.get('invis_pos', invis_pos)
            background_color = data.get('background_color', background_color)
            back_sprite = data.get('back_sprite', back_sprite)
            shooter_pos = data.get('shooter_pos', shooter_pos)
            poison_shooter_pos = data.get('poison_shooter_pos', poison_shooter_pos)

            # Set player spawn position for this level
            # Inside the level data loop
            x, y = data['spawn_pos']  # Set the player's position to the spawn position
            spawn_pos_x = x  # Set the spawn position to global variables
            spawn_pos_y = y


            # Clear and update the collision map
            col.clear()

            # Create a list to hold blocks to remove
            blocks_to_remove = []

            for block in level_ID:
                bx, by, id = block
                if id == 6:  # lava
                    lava_pos.append((bx, by))
                elif id == 7:  # rock
                    # Add rock position to rock_pos
                    rock_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 8:  # boss
                    # Add rock position to rock_pos
                    boss_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 11:  # shooter
                    # Add shooter position to shooter_pos
                    shooter_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 12:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    poison_shooter_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 13:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    grava_shooter_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 14:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    grava_shooter_posL.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 15:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    grava_shooter_posR.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 16:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    grava_shooter_posU.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                else:
                    # Append non-rock or non-lava blocks to collision map
                    col.append(bx)
                    col.append(by)

            # Remove blocks from level data after processing rocks
            for block in blocks_to_remove:
                level_ID.remove(block)

            # Mark the level as activated
            globals()[level_key] = True

            break  # Exit the loop after processing the current level

    # Add this check right before using walker_pos in check_multiple_walker_collisions or any other place
    if walker_pos is None:
        walker_pos = []  # or some other fallback like an initial position

def do_level_load_save():
    global level_ID, lev1_A, lev2_A, lev2_B, lev3_A, lev3_B, x, y, walker_pos, times, coins_pos, lives_pos, background_color, back_sprite, invis_pos, col, rock_pos, spawn_pos_x, spawn_pos_y, shooter_pos, poison_shooter_pos, arrow_pos, poison_arrow_pos, grava_shooter_pos, grava_shooter_posL, grava_shooter_posR, grava_shooter_posU
    # Define level data in a dictionary
    level_data = {
        'lev1_A': {'x_range': (0, 695), 'level': level_1_B, 'pos': walker_pos_level_2_A, 'coins_pos': coins_pos_level_2_A, 'lives_pos': lives_pos_level_2_A, 'invis_pos': invis_pos_level_2_A, 'back_sprite': None, 'lev_flag': lev2_A, 'spawn_pos': (150, 500)},
        'lev1_B': {'x_range': (0, 695), 'level': level_2_A, 'pos': walker_pos_level_2_B, 'coins_pos': coins_pos_level_2_B, 'lives_pos': lives_pos_level_2_B, 'invis_pos': invis_pos_level_2_B, 'background_color': (100, 100, 100), 'back_sprite': underground_back_1, 'lev_flag': lev2_B, 'spawn_pos': (150, 500)},
        'lev2_A': {'x_range': (0, 695), 'level': level_2_B, 'pos': walker_pos_level_3_A, 'coins_pos': coins_pos_level_3_A, 'lives_pos': lives_pos_level_3_A, 'invis_pos': invis_pos_level_3_A, 'back_sprite': underground_back_2, 'lev_flag': lev3_A, 'spawn_pos': (150, 500)},
        'lev2_B': {'x_range': (0, 695), 'level': level_3_A, 'pos': walker_pos_level_3_B, 'coins_pos': coins_pos_level_3_B, 'lives_pos': lives_pos_level_3_B, 'invis_pos': invis_pos_level_3_B, 'back_sprite': underground_back_1, 'lev_flag': lev3_B, 'spawn_pos': (150, 500)},
        'lev2_C': {'x_range': (0, 695), 'level': level_3_B, 'pos': walker_pos_level_3_C, 'coins_pos': coins_pos_level_3_C, 'lives_pos': lives_pos_level_3_C, 'invis_pos': invis_pos_level_3_C, 'background_color': (100, 100, 100), 'lev_flag': lev3_C, 'spawn_pos': (150, 500)},
        'lev2_D': {'x_range': (0, 695), 'level': level_3_C, 'pos': walker_pos_level_3_D, 'coins_pos': coins_pos_level_3_D, 'lives_pos': lives_pos_level_3_D, 'invis_pos': invis_pos_level_3_D, 'background_color': (0, 255, 255), 'back_sprite': None, 'lev_flag': lev3_D, 'spawn_pos': (150, 500)},
        'lev3_A': {'x_range': (0, 695), 'level': level_3_D, 'pos': walker_pos_level_4_A, 'coins_pos': coins_pos_level_4_A, 'lives_pos': lives_pos_level_4_A, 'invis_pos': invis_pos_level_4_A, 'background_color': (0, 255, 255), 'back_sprite': None, 'lev_flag': lev4_A, 'spawn_pos': (150, 500)},
        'lev4_A': {'x_range': (0, 695), 'level': level_4_A, 'pos': walker_pos_level_5_A, 'coins_pos': coins_pos_level_5_A, 'lives_pos': lives_pos_level_5_A, 'invis_pos': invis_pos_level_5_A, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev5_A, 'spawn_pos': (100, 500)},
        'lev4_B': {'x_range': (0, 695), 'level': level_5_A, 'pos': walker_pos_level_5_B, 'coins_pos': coins_pos_level_5_B, 'lives_pos': lives_pos_level_5_B, 'invis_pos': invis_pos_level_5_B, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev5_B, 'spawn_pos': (100, 500), 'shooter_pos': [(576, 451)], 'poison_shooter_pos': [(432, 451), (480, 451), (528, 451)]},
        'lev4_C': {'x_range': (0, 695), 'level': level_5_B, 'pos': walker_pos_level_5_C, 'coins_pos': coins_pos_level_5_C, 'lives_pos': lives_pos_level_5_C, 'invis_pos': invis_pos_level_5_C, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev5_C, 'spawn_pos': (100, 500), 'shooter_pos': [], 'poison_shooter_pos': [(384, 410), (240, 410)]},
        'lev4_D': {'x_range': (0, 695), 'level': level_5_C, 'pos': walker_pos_level_5_D, 'coins_pos': coins_pos_level_5_D, 'lives_pos': lives_pos_level_5_D, 'invis_pos': invis_pos_level_5_D, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev5_D, 'spawn_pos': (100, 500), 'shooter_pos': [], 'poison_shooter_pos': [(432, 410), (336, 410), (288, 410), (192, 410)]},
        'lev5_A': {'x_range': (0, 695), 'level': level_5_D, 'pos': walker_pos_level_6_A, 'coins_pos': coins_pos_level_6_A, 'lives_pos': lives_pos_level_6_A, 'invis_pos': invis_pos_level_6_A, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev6_A, 'spawn_pos': (100, 500), 'shooter_pos': [(192, 410), (240, 410), (288, 410), (384, 410), (432, 410), (480, 410), (528, 410), (576, 410)], 'poison_shooter_pos': []},
        'lev5_B': {'x_range': (0, 695), 'level': level_6_A, 'pos': walker_pos_level_6_B, 'coins_pos': coins_pos_level_6_B, 'lives_pos': lives_pos_level_6_B, 'invis_pos': invis_pos_level_6_B, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev6_B, 'spawn_pos': (100, 500), 'shooter_pos': [], 'poison_shooter_pos': []},
        'lev5_C': {'x_range': (0, 695), 'level': level_6_B, 'pos': walker_pos_level_6_C, 'coins_pos': coins_pos_level_6_C, 'lives_pos': lives_pos_level_6_C, 'invis_pos': invis_pos_level_6_C, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev6_C, 'spawn_pos': (100, 500), 'shooter_pos': [], 'poison_shooter_pos': []},
        'lev5_D': {'x_range': (0, 695), 'level': level_6_C, 'pos': walker_pos_level_6_D, 'coins_pos': coins_pos_level_6_D, 'lives_pos': lives_pos_level_6_C, 'invis_pos': invis_pos_level_6_D, 'background_color': (0, 0, 0), 'back_sprite': None, 'lev_flag': lev6_D, 'spawn_pos': (100, 500), 'shooter_pos': [(288, 0), (480, 0), (624, 0)], 'poison_shooter_pos': []},
    }

    # Loop through each level's data
    for level_key, data in level_data.items():
        # Check if the level is not already activated and if the player is within the range
        if x > data['x_range'][0] and x < data['x_range'][1] and not data['lev_flag']:
            arrow_pos = []
            poison_arrow_pos = []
            grava_shooter_pos = []
            grava_shooter_posL = []
            grava_shooter_posR = []
            grava_shooter_posU = []
            # Update global variables
            level_ID = data['level']
            walker_pos = data.get('pos', walker_pos)
            coins_pos = data.get('coins_pos', coins_pos)
            lives_pos = data.get('lives_pos', lives_pos)
            invis_pos = data.get('invis_pos', invis_pos)
            background_color = data.get('background_color', background_color)
            back_sprite = data.get('back_sprite', back_sprite)
            shooter_pos = data.get('shooter_pos', shooter_pos)
            poison_shooter_pos = data.get('poison_shooter_pos', poison_shooter_pos)

            # Set player spawn position for this level
            # Inside the level data loop
            x, y = data['spawn_pos']  # Set the player's position to the spawn position
            spawn_pos_x = x  # Set the spawn position to global variables
            spawn_pos_y = y


            # Clear and update the collision map
            col.clear()

            # Create a list to hold blocks to remove
            blocks_to_remove = []

            for block in level_ID:
                bx, by, id = block
                if id == 6:  # lava
                    lava_pos.append((bx, by))
                elif id == 7:  # rock
                    # Add rock position to rock_pos
                    rock_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 8:  # boss
                    # Add rock position to rock_pos
                    boss_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 11:  # shooter
                    # Add shooter position to shooter_pos
                    shooter_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 12:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    poison_shooter_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 13:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    grava_shooter_pos.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 14:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    grava_shooter_posL.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 15:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    grava_shooter_posR.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                elif id == 16:  # poison shooter
                    # Add shooter position to poison_shooter_pos
                    grava_shooter_posU.append((bx, by))
                    # Mark this block for removal
                    blocks_to_remove.append(block)
                else:
                    # Append non-rock or non-lava blocks to collision map
                    col.append(bx)
                    col.append(by)

            # Remove blocks from level data after processing rocks
            for block in blocks_to_remove:
                level_ID.remove(block)

            # Mark the level as activated
            globals()[level_key] = True

            break  # Exit the loop after processing the current level

    # Add this check right before using walker_pos in check_multiple_walker_collisions or any other place
    if walker_pos is None:
        walker_pos = []  # or some other fallback like an initial position

import sys

def game_over():
    chatter.clear(chatter.black)
    display_text(60, 60, "GAME OVER", chatter.green, 4)
    chatter.display_screen()
    time.sleep(5)
    print("The game will now close.")
    restart_program()

def close():
    x = 2 / 0


walker_pos = [100, 100]





void_levels = [level_5_A, level_5_B, level_5_C, level_5_D, level_6_A, level_6_B, level_6_C, level_6_D]

boss_levels = [level_4_A]

level_ID = level_1_B
# (48, 615, 8)
pressed_keys = []

lives = 3
coins = 0

vir = "SFA ALF 1.4.0"



lev1_A = False
lev2_A = False
lev2_B = False
lev3_A = False
lev3_B = False
lev3_C = False
lev3_D = False
lev4_A = False
lev5_A = False
lev5_B = False
lev5_C = False
lev5_D = False
lev6_A = False
lev6_B = False
lev6_C = False
lev6_D = False


# Load JSON data from file
def load_data():
    global level_ID, lev1_A, lev2_A, lev2_B, lev3_A, lev3_B, lev3_C, lev3_D, lev4_A, lev5_A, lev5_B, lev5_C, lev5_D, lev6_A, lev6_B, lev6_C, col
    with open(json_file, "r") as file:
        data_dict = json.load(file)
    
    # Extract and assign variables individually
    level_ID = data_dict["level_ID"]
    lev1_A = data_dict["lev1_A"]
    lev2_A = data_dict["lev2_A"]
    lev2_B = data_dict["lev2_B"]
    lev3_A = data_dict["lev3_A"]
    lev3_B = data_dict["lev3_B"]
    lev3_C = data_dict["lev3_C"]
    lev3_D = data_dict["lev3_D"]
    lev4_A = data_dict["lev4_A"]
    lev5_A = data_dict["lev5_A"]
    lev5_B = data_dict["lev5_B"]
    lev5_C = data_dict["lev5_C"]
    lev5_D = data_dict["lev5_D"]
    lev6_A = data_dict["lev6_A"]
    lev6_B = data_dict["lev6_B"]
    lev6_C = data_dict["lev6_C"]

    # Placeholder for level ID modification
    level_ID = data_dict["level_ID"]
    col = []
    for blocks in level_ID:
        bx, by, id = blocks
        col.append(bx)
        col.append(by)
    do_level_load_save()


def start_screen():
    global Player_con_W, Player_con_A, Player_con_S, Player_con_D, Player_con_ROCK, Player_con_ESC
    C = False
    S = False
    S_KBCS = False
    pressed_keys = []

    while True:
        chatter.clear(chatter.black)
        display_text(0, 10, vir, chatter.green, 3)
        display_text(60, 60, "STICK FIGURE ADVENTURES", chatter.green, 4)
        display_text(200, 500, "PRESS ENTER TO START", chatter.green, 2)
        display_text(0, 675, "MADE WITH CHATTER", chatter.green, 2)
        display_text(450, 675, "PRESS qCq FOR CREDITS", chatter.green, 2)
        display_text(450, 645, "PRESS qSq FOR SETTINGS", chatter.green, 2)
        chatter.display_screen()
        
        press = chatter.input().lower()
        
        if press == "return":
            break
        elif press == "c":
            C = True
        elif press == "s":
            S = True
        elif press == "q":
            close()

        # Credits Screen
        while C:
            chatter.clear(chatter.black)
            display_text(0, 10, vir, chatter.green, 3)
            display_text(60, 60, "CREDITS", chatter.green, 4)
            display_text(200, 500, "MADE BY ROWYN", chatter.green, 2)
            display_text(200, 550, "PROGRAMMING: ROWYN", chatter.green, 2)
            display_text(200, 600, "ARTWORK: ROWYN / LILLY", chatter.green, 2)
            display_text(400, 675, "PRESS qCq TO EXIT CREDITS", chatter.green, 2)
            chatter.display_screen()
            
            press = chatter.input().lower()
            if press == "c":
                C = False

        # Settings Screen
        while S:
            chatter.clear(chatter.black)
            display_text(0, 10, vir, chatter.green, 3)
            display_text(60, 60, "SETTINGS", chatter.green, 4)
            display_text(200, 500, "q1q FOR KEYBOARD CONFIG SETTINGS", chatter.green, 2)
            display_text(400, 675, "PRESS qSq TO EXIT SETTINGS", chatter.green, 2)
            chatter.display_screen()
            
            press = chatter.input().lower()
            if press == "s":
                S = False
            elif press == "1":
                S_KBCS = True

            # Keyboard Configuration
            while S_KBCS:
                chatter.clear(chatter.black)
                display_text(0, 10, vir, chatter.green, 3)
                display_text(60, 60, "KEYBOARD CONFIG SETTINGS", chatter.green, 4)
                display_text(200, 500, "q1q TO SET qWq KEY. q5q TO SET qEq KEY", chatter.green, 2)
                display_text(200, 520, "q2q TO SET qAq KEY. q6q TO SET qQq KEY", chatter.green, 2)
                display_text(200, 540, "q3q TO SET qSq KEY", chatter.green, 2)
                display_text(200, 560, "q4q TO SET qDq KEY", chatter.green, 2)
                display_text(200, 685, "WAITING 5 SEC BEFORE SETTING A KEY...", chatter.green, 2)
                display_text(300, 675, "PRESS qSq TO EXIT", chatter.green, 2)
                chatter.display_screen()
                
                press = chatter.input().lower()
                
                if press == "s":
                    S_KBCS = False
                    break
                if "1" in press:
                    time.sleep(5)
                    next_press = chatter.input()  # Wait for key input
                    if next_press:
                        Player_con_W = next_press[0]  # Set W key to the first pressed key
                    print(Player_con_W)
                if "2" in press:
                    time.sleep(5)
                    next_press = chatter.input()  # Wait for key input
                    if next_press:
                        Player_con_A = next_press[0]  # Set W key to the first pressed key
                    print(Player_con_A)
                if "3" in press:
                    time.sleep(5)
                    next_press = chatter.input()  # Wait for key input
                    if next_press:
                        Player_con_S = next_press[0]  # Set W key to the first pressed key
                    print(Player_con_S)
                if "4" in press:
                    time.sleep(5)
                    next_press = chatter.input()  # Wait for key input
                    if next_press:
                        Player_con_D = next_press[0]  # Set W key to the first pressed key
                    print(Player_con_D)
                if "5" in press:
                    time.sleep(5)
                    next_press = chatter.input()  # Wait for key input
                    if next_press:
                        Player_con_ROCK = next_press[0]  # Set W key to the first pressed key
                    print(Player_con_ROCK)
                if "6" in press:
                    time.sleep(5)
                    next_press = chatter.input()  # Wait for key input
                    if next_press:
                        Player_con_ESC = next_press[0]  # Set W key to the first pressed key
                    print(Player_con_ESC)


bx = 100
by = 375

nb = 9
nbr = nb - 1
# Walker Movement and Collision Logic with Backtracking improvements
def move_walker(pressed_keys, debug):
    global walker_pos, x, y, coins, is_invis, fps
    walker_speed = delta_speed(fps, 250)
    keys_input = pressed_keys

    i = len(walker_pos) - 4
    while i >= 0:
        x_position = walker_pos[i]  # X coordinate
        y_position = walker_pos[i + 1]  # Y coordinate
        direction = walker_pos[i + 2]  # Direction ("R" or "L")
        is_alive = walker_pos[i + 3]  # Is alive status

        # Player collision detection logic here
        player_collision = check_one_collision(x, y, player_width, player_height, x_position, y_position, walker_width, walker_height, 5, 1, debug)
        
        if player_collision and ("left shift" in keys_input or "right shift" in keys_input) and ("a" in keys_input or "d" in keys_input):
            walker_pos[i + 3] = "dead"
        if is_invis and player_collision:
            walker_pos[i + 3] = "dead"

        if walker_pos[i + 3] == "dead":
            coins += 1
            del walker_pos[i:i + 4]
        else:
            # Check for collisions with walls or other objects
            collision = check_collision(x_position, y_position, col, walker_width, walker_height, block_width, block_height, 1)

            if not collision:  # No collision
                if direction == "R":
                    walker_pos[i] += walker_speed
                elif direction == "L":
                    walker_pos[i] -= walker_speed
            else:  # Handle collisions
                if direction == "R":
                    walker_pos[i] -= 5  # Step back
                    walker_pos[i + 2] = "L"  # Change direction
                elif direction == "L":
                    walker_pos[i] += 5  # Step back
                    walker_pos[i + 2] = "R"  # Change direction

        i -= 4  # Adjust index when deleting walkers

arrow_walker_pos = []

def move_arrow_walker(pressed_keys, debug):
    global arrow_walker_pos, x, y, coins, is_invis, fps, arrow_walker_time
    walker_speed = delta_speed(fps, 250)
    keys_input = pressed_keys

    i = len(arrow_walker_pos) - 5  # Recalculate i after deletion
    while i >= 0:
        x_position = arrow_walker_pos[i]  # X coordinate
        y_position = arrow_walker_pos[i + 1]  # Y coordinate
        direction = arrow_walker_pos[i + 2]  # Direction ("R" or "L")
        is_alive = arrow_walker_pos[i + 3]  # Is alive status
        timer = arrow_walker_pos[i + 4]

        # Player collision detection logic here
        player_collision = check_one_collision(x, y, player_width, player_height, x_position, y_position, walker_width, walker_height, 5, 1, debug)
        
        if player_collision:
            arrow_walker_pos[i + 3] = "dead"

        if arrow_walker_pos[i + 3] == "dead":
            coins += 1
            del arrow_walker_pos[i:i + 5]
        else:
            # Check for collisions with walls or other objects
            collision = check_collision(x_position, y_position, col, walker_width, walker_height, block_width, block_height, 1)

            if not collision:  # No collision
                if direction == "R":
                    arrow_walker_pos[i] += walker_speed
                elif direction == "L":
                    arrow_walker_pos[i] -= walker_speed
            else:  # Handle collisions
                if direction == "R":
                    arrow_walker_pos[i] -= 5  # Step back
                    arrow_walker_pos[i + 2] = "L"  # Change direction
                elif direction == "L":
                    arrow_walker_pos[i] += 5  # Step back
                    arrow_walker_pos[i + 2] = "R"  # Change direction
        print(timer)
        if len(arrow_walker_pos) >= i + 4:
            x_position, y_position, direction, is_alive, timer = arrow_walker_pos[i:i + 5]
        else:
            continue  # Skip this walker if not enough data to unpack


        if timer == 1000:
            spawn_arrow(x_position, y_position, 'L')
            arrow_walker_pos[i + 4] = 0

        i -= 5  # Adjust index when deleting walkers
    print(arrow_walker_pos)

def lava_check():
    global x, y, player_width, player_height, block_height, block_width, lava_pos, lives
    for block in lava_pos:
        x_block, y_block = block
        if check_one_collision(x, y, player_width, player_height, x_block, y_block, block_width, block_height, 2, 1, debug):
            lives -= 1
            reset_player_position()

def arrow_check():
    global x, y, player_width, player_height, walker_height, walker_width, arrow_pos, lives
    for i, (x_arrow, y_arrow, dir_a) in enumerate(arrow_pos):
        if dir_a == "D":
            if check_one_collision(x, y, player_width, player_height, x_arrow, y_arrow, walker_width, walker_height, 2, 2, debug):
                lives -= 1
                reset_player_position()
        if dir_a == "L":
            if check_one_collision(x, y, player_width, player_height, x_arrow, y_arrow, walker_height, walker_width, 2, 2, debug):
                lives -= 1
                reset_player_position()

no_gravity_time = 0
no_gravity_player = False
no_gravity = False

def gravaton_check():
    global x, y, player_width, player_height, gravaton_height, gravaton_width, gravaton_pos, lives, no_gravity_time, no_gravity_player, no_gravity
    
    # Check collision with gravitons
    for i, (x_arrow, y_arrow, dir_a) in enumerate(gravaton_pos):
        if dir_a:
            if check_one_collision(x, y, player_width, player_height, x_arrow, y_arrow, gravaton_width, gravaton_height, 2, 2, debug):
                no_gravity = True  # Disable gravity when touching a graviton
                no_gravity_time = 0  # Reset the timer upon collision

    # If no gravity is active, update the timer and maintain no gravity until 300 frames
    if no_gravity:
        if no_gravity_time < 300:  # Keep no gravity for 300 frames
            no_gravity_player = True  # Disable gravity for the player
            no_gravity_time += 1  # Increment the no-gravity timer
        else:
            no_gravity_player = False  # Re-enable gravity after 300 frames
            no_gravity_time = 0  # Reset the timer
            no_gravity = False  # Disable the no-gravity state


paralyzation_timer = 0
is_paralyzation = False

def do_paralyzation():
    global pressed_keys, paralyzation_timer, is_paralyzation
    paralyzation_timer +=1
    if is_paralyzation:
        if paralyzation_timer < 100:
            pressed_keys = []
        else:
            paralyzation_timer = 0
            is_paralyzation = False

def poison_arrow_check():
    global x, y, player_width, player_height, walker_height, walker_width, poison_arrow_pos, lives, is_paralyzation
    for i, (x_arrow, y_arrow, dir_a) in enumerate(poison_arrow_pos):
        if dir_a == "D":
            if check_one_collision(x, y, player_width, player_height, x_arrow, y_arrow, walker_width, walker_height, 2, 2, debug):
                is_paralyzation = True
                do_paralyzation()
        if dir_a == "L":
            if check_one_collision(x, y, player_width, player_height, x_arrow, y_arrow, walker_height, walker_width, 2, 2, debug):
                is_paralyzation = True
                do_paralyzation()


def boss_check():
    global x, y, player_width, player_height, block_height, block_width, boss_pos, lives
    for block in boss_pos:
        x_block, y_block = block
        if check_one_collision(x, y, player_width, player_height, x_block, y_block, player_width, player_height, 2, 1, debug):
            lives -= 1
            reset_player_position()

def rock_check():
    global x, y, player_width, player_height, block_height, block_width, rock_pos, lives, is_player_holding_rock
    for block in rock_pos:
        x_block, y_block = block
        if check_one_collision(x, y, player_width, player_height, x_block, y_block, block_width, block_height, 2, 1, debug):
            is_player_holding_rock = True

kill_rocks = False

def move_rock():
    global rock_pos, x, y, is_player_holding_rock, fps, is_rock_moveing
    for i, (x_rock, y_rock) in enumerate(rock_pos):  # Unpack x and y from each rock position
        is_col_blocks = check_collision(x_rock, y_rock, col, block_width, block_height, block_width, block_height, 1)
        if not is_col_blocks and not is_player_holding_rock and not is_rock_moveing:
            rock_pos[i] = (x_rock, y_rock + 5)  # Update the position of the rock to the left
        if is_player_holding_rock:
            rock_pos[i] = (x - 10, y - 40)  # Update the position of the rock to the player's coordinates
        elif is_rock_moveing:
            rock_pos[i] = (x_rock + delta_speed(fps, 250), y_rock)  # Update the position of the rock to the right
            if x_rock > 700:  # If rock has moved off-screen, remove it
                del rock_pos[i]
        if kill_rocks:
            del rock_pos[i]
            is_player_holding_rock = False
            is_rock_moveing = False

Boss_lives = 3
Rock_timer = 0
Walker_timer = 0
Boss_phase = 2

print()

def spawn_walkers(x, y):
    walker_pos.append(x)
    walker_pos.append(y)
    walker_pos.append('L')
    walker_pos.append('alive')
    walker_pos.append(x)
    walker_pos.append(y - 41)
    walker_pos.append('L')
    walker_pos.append('alive')
    walker_pos.append(x - 48)
    walker_pos.append(y)
    walker_pos.append('L')
    walker_pos.append('alive')
    walker_pos.append(x + 48)
    walker_pos.append(y - 41)
    walker_pos.append('L')
    walker_pos.append('alive')

change_phase = False

poison_arrow_timer = 0

def do_boss():
    global rock_pos, boss_pos, lives, x, y, is_player_holding_rock, is_rock_moveing, change_phase
    global debug, player_width, player_height, Boss_lives, kill_rocks, coins, Rock_timer, x, y, Boss_phase, Walker_timer, poison_arrow_timer

    kill_rocks = False

    # Check for collisions between rocks and the boss
    for block in rock_pos:
        x_block, y_block = block
        for i, (x_boss, y_boss) in enumerate(boss_pos):
            if check_one_collision(
                x_boss, y_boss, player_width, player_height,
                x_block, y_block, player_width, player_height, 5, 1, debug
            ):
                Boss_lives -= 1
                kill_rocks = True
                change_phase = True
            # If the boss's lives are depleted, remove it and reward the player
            if Boss_lives <= 0:
                del boss_pos[i]
                coins += 15
                x = x_boss
                y = y_boss
                kill_rocks = True

    # Handle boss phases
    if Boss_phase == 3:
        for i, (x_boss, y_boss) in enumerate(boss_pos):
            Rock_timer += 1
            print("Rock_timer: " + str(Rock_timer))
    elif Boss_phase == 1:
        for i, (x_boss, y_boss) in enumerate(boss_pos):
            if Walker_timer >= 400:
                for x_boss, y_boss in boss_pos:  # Ensure x_boss, y_boss are defined
                    spawn_walkers(x_boss, y_boss)
                    Walker_timer = 0  # Reset the timer for the next boss phase
                    Boss_phase = 3  # Change to phase 2 (rock phase)
            Walker_timer +=1
            print("Walker_timer: " + str(Walker_timer))
    elif Boss_phase == 2:
        for i, (x_boss, y_boss) in enumerate(boss_pos):
            poison_arrow_timer +=1
            if poison_arrow_timer >= 300:
                spawn_arrow(x_boss, y_boss + 60, 'L')
                poison_arrow_timer = 0  # Reset the timer for the next boss phase
                Boss_phase = 1  # Change to phase 3 (poison arrow phase)

    # Increment Rock Timer once per function call, not per rock

    # Check if the timer has reached the threshold and spawn a new rock
    if Rock_timer >= 400:
        if not rock_pos:  # Check if there are no rocks
            is_player_holding_rock = False
            is_rock_moveing = False
            # Dynamically calculate spawn position (e.g., at a random x-coordinate)
            new_rock_pos = (0, 0)  # Change this to your desired spawn logic
            rock_pos.append(new_rock_pos)
            Rock_timer = 0  # Reset the timer
            Boss_phase = 2
        else:
            Boss_phase = 2
    if change_phase:
        Boss_phase = 2
        change_phase = False


def check_if_dead():
    global lives, x, y, pressed_keys, is_invis

    # Check if the player fell below the screen
    if y > 660:
        lives -= 1
        reset_player_position()
        is_invis = False

    # Check collisions only if the player is not invisible
    if not is_invis:
        if check_multiple_walker_collisions(x, y, player_width, player_height, walker_pos, walker_width, walker_height):
            # If player is running, let the walker die (handled elsewhere)
            if "left shift" in pressed_keys or "right shift" in pressed_keys:
                return  # Skip further checks since walker death is handled elsewhere
            else:
                # Otherwise, player dies
                lives -= 1
                reset_player_position()
        if boss_check():
            lives -= 1
            reset_player_position()
        arrow_check()

    # If lives drop to zero or below, end the game
    if lives <= 0:
        while True:
            game_over()

    # Check for lava-related deaths
    lava_check()



def reset_player_position():
    global x, y, spawn_pos_x, spawn_pos_y
    x, y = 100, 500  # Reset player to starting position





def check_all_coins_col():
    global coins, x, y, player_width, player_height
    for i in range(len(coins_pos) - 3, -1, -3):  # Iterate in reverse, step by -3
        x_coin, y_coin, status = coins_pos[i], coins_pos[i + 1], coins_pos[i + 2]
        is_colliding = check_one_collision(
            x_coin, y_coin, coins_width, coins_height, x, y, player_width, player_height, 1, 3, debug
        )
        if is_colliding:
            coins += 1
            del coins_pos[i:i + 3]  # Remove the coin from the list

def check_all_eme_col():
    global lives, x, y, player_width, player_height
    for i in range(len(lives_pos) - 3, -1, -3):  # Iterate in reverse, step by -3
        x_eme, y_eme, status = lives_pos[i], lives_pos[i + 1], lives_pos[i + 2]
        is_colliding = check_one_collision(
            x_eme, y_eme, coins_width, coins_height, x, y, player_width, player_height, 4, 3, debug
        )
        if is_colliding:
            lives += 1
            del lives_pos[i:i + 3]  # Remove the "eme" item from the list

is_invis = False

is_invis = False  # Global flag to indicate if invincibility is active
invis_duration = 5  # Duration in seconds for invincibility power-up
invis_start_time = None  # Tracks when invincibility was activated


def check_all_invis_col(invis_pos, x, y, player_width, player_height, invis_width, invis_height, debug=False):
    """
    Checks for collisions with invisible items and toggles the invincibility flag.

    Args:
        invis_pos (list): Flat list of invisible items (x, y, status).
        x, y (int): Player's position.
        player_width, player_height (int): Player's dimensions.
        invis_width, invis_height (int): Invisible item dimensions.
        debug (bool): Enables debug mode if True.

    Returns:
        tuple: Updated invis_pos list and is_invis flag.
    """
    global is_invis, invis_start_time

    for i in range(len(invis_pos) - 3, -1, -3):  # Iterate in reverse, step by -3
        x_invis, y_invis, status = invis_pos[i], invis_pos[i + 1], invis_pos[i + 2]
        is_colliding = check_one_collision(
            x_invis, y_invis, invis_width, invis_height, x, y, player_width, player_height, 1, 1, debug
        )
        if is_colliding:
            is_invis = True  # Activate invincibility
            invis_start_time = time.time()  # Record the activation time
            del invis_pos[i:i + 3]  # Remove the "invis" item from the list
    return invis_pos


def update_invincibility():
    """
    Checks and updates the invincibility status based on the timer.
    """
    global is_invis, invis_start_time

    if is_invis and invis_start_time is not None:
        elapsed_time = time.time() - invis_start_time
        if elapsed_time >= invis_duration:
            is_invis = False  # Deactivate invincibility
            invis_start_time = None  # Reset the timer



# check_one_collision(x_coin, y_coin, coins_width, coins_height, x, y, player_width, player_height, 1, 5, debug)
# check_one_collision(x, y, player_width, player_height, x_coin, y_coin, coins_width, coins_height, 1, 5, debug)




# (192, 375),
# Update col list for collision detection
col.clear()  # Clear previous collision data

# Check if level_ID is correctly structured before looping through it
if isinstance(level_ID, list):
    for block in level_ID:
        # Check if the block has exactly 3 elements
        if len(block) == 3:
            bx, by, id = block
            col.append(bx)
            col.append(by)
        else:
            pass
else:
    pass


block_width = 24  # The width of each block (grass block)
block_height = 20  # The height of each block
player_width, player_height = 12, 40  # Adjust to your player's size
walker_width, walker_height = 6, 20 # Adjust to your walker
gravaton_width, gravaton_height = 20, 20 # Adjust to your walker
platform_width, platform_height = 24, 20
coins_width, coins_height = 10, 12
invis_width, invis_height = 25, 25
x, y = 150, 500
scale = 2
speed = 1
# List to hold pressed keys

lev1_A = False
lev2_A = False
lev2_B = False
lev3_A = False
lev3_B = False
lev3_C = False
lev3_D = False
lev4_A = False
lev5_A = False
lev5_B = False
lev5_C = False
lev5_D = False
lev6_A = False
lev6_B = False
lev6_C = False
lev6_D = False

walker_pos_level_1_A = []
walker_pos_level_2_A = [336, 600, "R", "alive", 576, 615, "R", "alive"] # [(576, 615, 2)]
walker_pos_level_2_B = [336, 600, "R", "alive", 576, 615, "R", "alive"] # [(576, 615, 2)]
walker_pos_level_3_A = [432, 615, 'R', 'alive', 528, 615, 'R', 'alive']
walker_pos_level_3_B = [96, 615, 'R', 'alive', 288, 615, 'R', 'alive', 480, 615, 'R', 'alive', 624, 615, 'R', 'alive']
walker_pos_level_3_C = [336, 574, 'L', 'alive']
walker_pos_level_3_D = []
walker_pos_level_4_A = []
walker_pos_level_5_A = []
walker_pos_level_5_B = []
walker_pos_level_5_C = [240, 574, 'R', 'alive', 384, 574, 'R', 'alive']
walker_pos_level_5_D = [336, 574, 'R', 'alive', 240, 574, 'R', 'alive', 432, 574, 'R', 'alive']
walker_pos_level_6_A = [384, 574, 'R', 'alive', 240, 574, 'R', 'alive', 480, 574, 'R', 'alive']
walker_pos_level_6_B = []
walker_pos_level_6_C = [384, 574, 'R', 'alive', 432, 328, 'R', 'alive', 240, 287, 'R', 'alive', 576, 287, 'R', 'alive']
walker_pos_level_6_D = [384, 492, 'R', 'alive']
walker_pos = walker_pos_level_1_A

coins_pos_level_1_A = []
coins_pos_level_2_A = [336, 615, "N", 480, 574, "N", 528, 574, "N", 576, 574, "N", 480, 533, "N", 528, 533, "N", 576, 533, "N"] # [(576, 533, 2)]
coins_pos_level_2_B = [336, 615, "N", 480, 574, "N", 528, 574, "N", 576, 574, "N", 480, 533, "N", 528, 533, "N", 576, 533, "N"] # [(576, 533, 2)]
coins_pos_level_3_A = [144, 533, 'N', 240, 451, 'N', 528, 574, 'N', 480, 574, 'N', 480, 369, 'N', 528, 369, 'N', 576, 369, 'N', 576, 328, 'N', 528, 328, 'N', 480, 328, 'N']
coins_pos_level_3_B = [288, 574, 'N', 288, 533, 'N', 96, 574, 'N', 96, 533, 'N', 480, 533, 'N', 624, 533, 'N', 624, 574, 'N', 480, 574, 'N']
coins_pos_level_3_C = [192, 574, 'N', 432, 574, 'N', 0, 615, 'N', 48, 574, 'N', 96, 533, 'N', 576, 533, 'N']
coins_pos_level_3_D = [336, 574, 'N', 96, 533, 'N', 144, 574, 'N', 528, 615, 'N', 576, 574, 'N']
coins_pos_level_4_A = []
coins_pos_level_5_A = [0, 574, 'N', 288, 574, 'N', 336, 574, 'N', 384, 574, 'N', 624, 574, 'N']
coins_pos_level_5_B = [192, 574, 'N', 288, 574, 'N', 432, 533, 'N', 480, 533, 'N', 528, 533, 'N', 576, 533, 'N']
coins_pos_level_5_C = [192, 533, 'N', 432, 533, 'N']
coins_pos_level_5_D = [288, 533, 'N', 336, 533, 'N']
coins_pos_level_6_A = []
coins_pos_level_6_B = [96, 574, 'N', 192, 492, 'N', 288, 410, 'N', 384, 328, 'N', 384, 533, 'N', 336, 533, 'N', 624, 533, 'N']
coins_pos_level_6_C = [576, 410, 'N', 576, 451, 'N', 576, 369, 'N', 384, 246, 'N', 192, 369, 'N', 384, 451, 'N', 336, 533, 'N', 384, 533, 'N', 432, 533, 'N']
coins_pos_level_6_D = [288, 205, 'N', 288, 164, 'N', 288, 123, 'N', 288, 82, 'N', 288, 41, 'N', 480, 41, 'N', 480, 82, 'N', 480, 123, 'N', 480, 164, 'N', 480, 205, 'N']
coins_pos = coins_pos_level_1_A

lives_pos_level_1_A = []
lives_pos_level_2_A = [384, 492, "N"] # [(384, 492, 2)]
lives_pos_level_2_B = []
lives_pos_level_3_A = [48, 369, 'N']
lives_pos_level_3_B = []
lives_pos_level_3_C = [336, 574, 'N']
lives_pos_level_3_D = []
lives_pos_level_4_A = []
lives_pos_level_5_A = []
lives_pos_level_5_B = []
lives_pos_level_5_C = []
lives_pos_level_5_D = []
lives_pos_level_6_A = []
lives_pos_level_6_B = []
lives_pos_level_6_C = [192, 246, 'N']
lives_pos_level_6_C = [384, 410, 'N']
lives_pos = lives_pos_level_1_A

invis_pos_level_1_A = []
invis_pos_level_2_A = [] # [(384, 492, 2)]
invis_pos_level_2_B = []
invis_pos_level_3_A = []
invis_pos_level_3_B = [0, 451, 'N']
invis_pos_level_3_C = []
invis_pos_level_3_D = []
invis_pos_level_4_A = []
invis_pos_level_5_A = []
invis_pos_level_5_B = []
invis_pos_level_5_C = []
invis_pos_level_5_D = []
invis_pos_level_6_A = []
invis_pos_level_6_B = []
invis_pos_level_6_C = []
invis_pos_level_6_D = []
invis_pos = invis_pos_level_1_A


platform_pos = []

import time  # Import the time module

# Initialize variables for FPS calculation
previous_time = time.time()
fps = 0
target_fps = 10000
frame_duration = 1 / target_fps  # Desired frame duration in seconds (e.g., 0.01 for 100 FPS)

invis_ane_timer = 0

platform_pos = []  # List to store platform positions


def delta_speed(fps, speed):
    if fps == 0:
        print("Warning: FPS is 0. Returning delta speed as 0.")
        return 0
    return speed * (1 / fps)


player_ane_invis_frames = [
    player_ane_invis_1,  # Frame 1
    player_ane_invis_2,  # Frame 2
    player_ane_invis_3,  # Frame 3
    player_ane_invis_4,  # Frame 4
]

gravaton_ane_timer = 0

gravaton_ane_frames = [
    gravaton, # Frame 0
    gravaton, # Frame 0
    gravaton, # Frame 0
    gravaton1,  # Frame 1
    gravaton1,  # Frame 1
    gravaton1,  # Frame 1
    gravaton2,  # Frame 2
    gravaton2,  # Frame 2
    gravaton2,  # Frame 2
    gravaton3,  # Frame 3
    gravaton3,  # Frame 3
    gravaton3,  # Frame 3
    gravaton4,  # Frame 4
    gravaton4,  # Frame 4
    gravaton4,  # Frame 4
    gravaton5,  # Frame 5
    gravaton5,  # Frame 5
    gravaton5,  # Frame 5
    gravaton6,  # Frame 6
    gravaton6,  # Frame 6
    gravaton6,  # Frame 6
    gravaton7,  # Frame 7
    gravaton7,  # Frame 7
    gravaton7,  # Frame 7
]

is_player_holding_rock = False
is_rock_moveing = False

shooter_timer = 0

arrow_pos = []

poison_arrow_pos = []

gravaton_pos = []

def spawn_arrow(x, y, dir_a):
    global arrow_pos
    arrow_pos.append((x, y, dir_a))

def spawn_poison_arrow(x, y, dir_a):
    global poison_arrow_pos
    poison_arrow_pos.append((x, y, dir_a))

def spawn_gravaton(x, y, dir_a):
    global gravaton_pos
    gravaton_pos.append((x, y, dir_a))

def do_arrow():
    global arrow_pos, fps
    for i, (x_arrow, y_arrow, dir_a) in enumerate(arrow_pos):
        if dir_a == 'D':
            arrow_pos[i] = (x_arrow, y_arrow + delta_speed(fps, 300), dir_a)
        elif dir_a == 'L':
            arrow_pos[i] = (x_arrow - delta_speed(fps, 300), y_arrow, dir_a)

def do_gravaton():
    global gravaton_pos, fps
    for i, (x_arrow, y_arrow, dir_a) in enumerate(gravaton_pos):
        if not check_collision(x_arrow, y_arrow, col, gravaton_width, gravaton_height, block_width, block_height, 2):
            if dir_a == 'D':
                gravaton_pos[i] = (x_arrow, y_arrow + delta_speed(fps, 300), dir_a)
            elif dir_a == 'L':
                gravaton_pos[i] = (x_arrow - delta_speed(fps, 300), y_arrow, dir_a)
            elif dir_a == 'U':
                gravaton_pos[i] = (x_arrow, y_arrow - delta_speed(fps, 300), dir_a)
            elif dir_a == 'R':
                gravaton_pos[i] = (x_arrow + delta_speed(fps, 300), y_arrow, dir_a)
        else:
            del gravaton_pos[i]

print()

def do_poison_arrow():
    global poison_arrow_pos, fps
    for i, (x_arrow, y_arrow, dir_a) in enumerate(poison_arrow_pos):
        if dir_a == 'D':
            poison_arrow_pos[i] = (x_arrow, y_arrow + delta_speed(fps, 300), dir_a)
        elif dir_a == 'L':
            poison_arrow_pos[i] = (x_arrow - delta_speed(fps, 300), y_arrow, dir_a)

shooter_timers = []

grava_shooter_timers = []

def do_shooter():
    global shooter_pos, shooter_timers  # shooter_timers is now a list of timers
    # Ensure shooter_timers is the right length
    if len(shooter_timers) < len(shooter_pos):
        shooter_timers.extend([0] * (len(shooter_pos) - len(shooter_timers)))  # Add more timers if needed

    for i, (x_shooter, y_shooter) in enumerate(shooter_pos):
        # Ensure each shooter has their own timer value
        shooter_timers[i] += 1
        
        if shooter_timers[i] == 300:
            spawn_arrow(x_shooter, y_shooter, 'D')
            shooter_timers[i] = 0  # Reset the timer for that shooter

def do_grava_shooter():
    global grava_shooter_pos, grava_shooter_timers  # shooter_timers is now a list of timers
    # Ensure shooter_timers is the right length
    if len(grava_shooter_timers) < len(grava_shooter_pos):
        grava_shooter_timers.extend([0] * (len(grava_shooter_pos) - len(grava_shooter_timers)))  # Add more timers if needed

    for i, (x_shooter, y_shooter) in enumerate(grava_shooter_pos):
        # Ensure each shooter has their own timer value
        grava_shooter_timers[i] += 1
        
        if grava_shooter_timers[i] == 300:
            spawn_gravaton(x_shooter + 60, y_shooter, 'D')
            grava_shooter_timers[i] = 0  # Reset the timer for that shooter

def do_grava_shooterL():
    global grava_shooter_posL, grava_shooter_timers  # shooter_timers is now a list of timers
    # Ensure shooter_timers is the right length
    if len(grava_shooter_timers) < len(grava_shooter_posL):
        grava_shooter_timers.extend([0] * (len(grava_shooter_posL) - len(grava_shooter_timers)))  # Add more timers if needed

    for i, (x_shooter, y_shooter) in enumerate(grava_shooter_posL):
        # Ensure each shooter has their own timer value
        grava_shooter_timers[i] += 1
        
        if grava_shooter_timers[i] == 300:
            spawn_gravaton(x_shooter - 60, y_shooter, 'L')
            grava_shooter_timers[i] = 0  # Reset the timer for that shooter

def do_grava_shooterR():
    global grava_shooter_posR, grava_shooter_timers  # shooter_timers is now a list of timers
    # Ensure shooter_timers is the right length
    if len(grava_shooter_timers) < len(grava_shooter_posR):
        grava_shooter_timers.extend([0] * (len(grava_shooter_posR) - len(grava_shooter_timers)))  # Add more timers if needed

    for i, (x_shooter, y_shooter) in enumerate(grava_shooter_posR):
        # Ensure each shooter has their own timer value
        grava_shooter_timers[i] += 1
        
        if grava_shooter_timers[i] == 300:
            spawn_gravaton(x_shooter, y_shooter + 60, 'R')
            grava_shooter_timers[i] = 0  # Reset the timer for that shooter

def do_grava_shooterU():
    global grava_shooter_posU, grava_shooter_timers  # shooter_timers is now a list of timers
    # Ensure shooter_timers is the right length
    if len(grava_shooter_timers) < len(grava_shooter_posU):
        grava_shooter_timers.extend([0] * (len(grava_shooter_posU) - len(grava_shooter_timers)))  # Add more timers if needed

    for i, (x_shooter, y_shooter) in enumerate(grava_shooter_posU):
        # Ensure each shooter has their own timer value
        grava_shooter_timers[i] += 1
        
        if grava_shooter_timers[i] == 300:
            spawn_gravaton(x_shooter, y_shooter - 60, 'U')
            grava_shooter_timers[i] = 0  # Reset the timer for that shooter

poison_shooter_timers = []

def do_poison_shooter():
    global poison_shooter_pos, poison_shooter_timers  # shooter_timers is now a list of timers
    # Ensure shooter_timers is the right length
    if len(poison_shooter_timers) < len(poison_shooter_pos):
        poison_shooter_timers.extend([0] * (len(poison_shooter_pos) - len(poison_shooter_timers)))  # Add more timers if needed

    for i, (x_shooter, y_shooter) in enumerate(poison_shooter_pos):
        # Ensure each shooter has their own timer value
        poison_shooter_timers[i] += 1
        
        if poison_shooter_timers[i] == 300:
            spawn_poison_arrow(x_shooter, y_shooter, 'D')
            poison_shooter_timers[i] = 0  # Reset the timer for that shooter

def check_coins():
    global coins, lives
    lives += coins // 100  # Use integer division to add the number of lives
    coins = coins % 100  # The remaining coins after dividing by 100

crouching = False

def do_player_crouching():
    global crouching, player_width, player_height
    if crouching:
        player_width, player_height = 12, 20
    else:
        player_width, player_height = 12, 40

gravaton_width, gravaton_height = 20, 20 # Adjust to your walker

presssed_keys = []

is_paused = False


def restart_program():
    """Restarts the current Python program"""
    current_script = sys.argv[0]  # Get the current script name (could be renamed later)
    
    print(f"Attempting to restart the game")
    
    try:
        # Start a new instance of the current script using subprocess
        subprocess.Popen([sys.executable, current_script])  # This runs the program without blocking


        print(f"{current_script} has been successfully launched.")
        
        # Exit the current script to complete the "restart" process
        sys.exit(0)
        
    except Exception as e:
        print(f"Error during restart: {e}")
        sys.exit(1)

Player_con_W = "w"
Player_con_A = "a"
Player_con_S = "s"
Player_con_D = "d"
Player_con_SPACE = "space"
Player_con_RUN = "left shift"
Player_con_ROCK = "e"
Player_con_ESC = "q"

start_screen()

import json

# File path for JSON data


# Save JSON data to file
def save_data():
    data_dict = {
        "level_ID": level_ID,
        "lev1_A": lev1_A,
        "lev2_A": lev2_A,
        "lev2_B": lev2_B,
        "lev3_A": lev3_A,
        "lev3_B": lev3_B,
        "lev3_C": lev3_C,
        "lev3_D": lev3_D,
        "lev4_A": lev4_A,
        "lev5_A": lev5_A,
        "lev5_B": lev5_B,
        "lev5_C": lev5_C,
        "lev5_D": lev5_D,
        "lev6_A": lev6_A,
        "lev6_B": lev6_B,
        "lev6_C": lev6_C
    }
    with open(json_file, "w") as file:
        json.dump(data_dict, file, indent=4)

while True:
    try:
        # Start time of the loop
        start_time = time.time()
        if level_ID in void_levels:
            text_color = chatter.white
            player_color = player_white
        else:
            text_color = chatter.black
            player_color = player
        
        # Update invincibility status
        update_invincibility()
        # Clear the screen and display background sprite
        chatter.clear(background_color)
        chatter.display_sprite(back_sprite, 0, 0, 3)
        
        # Display player sprite with invisibility check
        # If invincibility is active, display the correct frame based on invis_ane_timer
        if is_invis:
            if invis_ane_timer < len(player_ane_invis_frames):
                # Access the frame by its index using invis_ane_timer
                frame = player_ane_invis_frames[invis_ane_timer]
                chatter.display_sprite(frame, x, y, 5)
                invis_ane_timer += 1
            else:
                invis_ane_timer = 0  # Reset the timer when we reach the end of the frames
        elif is_player_holding_rock:
            chatter.display_sprite(player_rock, x, y, 5)
        else:
            chatter.display_sprite(player_color, x, y, 5)


        
        # Display walker sprites in batches for better performance
        for i in range(0, len(walker_pos), 4):
            walker_pos_x, walker_pos_y, _, status = walker_pos[i:i + 4]
            if status == "alive":
                chatter.display_sprite(walker, walker_pos_x, walker_pos_y, 4)
        for i in range(0, len(arrow_walker_pos), 5):
            walker_pos_x, walker_pos_y, _, status = arrow_walker_pos[i:i + 4]
            if status == "alive":
                chatter.display_sprite(arrow_walker, walker_pos_x, walker_pos_y, 4)
        
        # Display coins, lives, and invisibility sprites in batches
        for i, pos in enumerate([coins_pos, lives_pos, invis_pos]):
            sprite = [coin, eme, invis][i]
            for j in range(0, len(pos), 3):
                pos_x, pos_y, _ = pos[j:j + 3]
                chatter.display_sprite(sprite, pos_x, pos_y, 3)
        
        # Display block sprites based on level data
        for block in level_ID:
            bx, by, block_id = block
            sprite = {1: grass_block, 2: stone_block, 6: lava, 7: rock}.get(block_id, None)
            if sprite:
                chatter.display_sprite(sprite, bx, by, 3)
        
        for block in rock_pos:
            bx, by = block
            if sprite:
                chatter.display_sprite(rock, bx, by, 3)
        
        for block in boss_pos:
            bx, by = block
            if sprite:
                chatter.display_sprite(boss, bx, by, 5)
                chatter.display_text(bx, by - 10, str(Boss_lives), chatter.black, 2)

        for block in shooter_pos:
            bx, by = block
            if sprite:
                chatter.display_sprite(shooter, bx, by, 3)
        for block in arrow_pos:
            bx, by, dir_a = block
            if dir_a == 'D':
                    if sprite:
                        chatter.display_sprite(arrow, bx, by, 3)
            if dir_a == 'L':
                    if sprite:
                        chatter.display_sprite(arrow_l, bx, by, 3)

        for block in poison_shooter_pos:
            bx, by = block
            if sprite:
                chatter.display_sprite(poison_shooter, bx, by, 3)
        for block in grava_shooter_pos:
            bx, by = block
            if sprite:
                chatter.display_sprite(grava_shooter, bx, by, 3)
        for block in grava_shooter_posL:
            bx, by = block
            if sprite:
                chatter.display_sprite(grava_shooterL, bx, by, 3)
        for block in grava_shooter_posR:
            bx, by = block
            if sprite:
                chatter.display_sprite(grava_shooterR, bx, by, 3)
        for block in grava_shooter_posU:
            bx, by = block
            if sprite:
                chatter.display_sprite(grava_shooterU, bx, by, 3)
        for block in gravaton_pos:
            bx, by, dir = block
            if sprite:
                if gravaton_ane_timer == len(gravaton_ane_frames):
                    gravaton_ane_timer = 0
                chatter.display_sprite(gravaton_ane_frames[gravaton_ane_timer], bx, by, 3)
                gravaton_ane_timer +=1
        for block in poison_arrow_pos:
            bx, by, dir_a = block
            if dir_a == 'D':
                    if sprite:
                        chatter.display_sprite(poison_arrow, bx, by, 3)
            if dir_a == 'L':
                    if sprite:
                        chatter.display_sprite(poison_arrow_l, bx, by, 3)
        debug = True
        # Debug drawing (conditional based on the debug flag)
        if debug:
            draw_block_boundaries(col, block_width, block_height, scale, chatter.blue)
            draw_collision_boundary(x, y, player_width, player_height, scale, chatter.red)
            draw_walker_boundaries(walker_pos, walker_width, walker_height, 2, chatter.blue, 4)
            draw_walker_boundaries(arrow_walker_pos, walker_width, walker_height, 2, chatter.green, 5)
            draw_walker_boundaries(coins_pos, coins_width, coins_height, 2, chatter.blue, 3)
            draw_walker_boundaries(lives_pos, coins_width, coins_height, 2, chatter.blue, 3)
            draw_walker_boundaries(invis_pos, invis_width, invis_height, 2, chatter.blue, 3)
            draw_gravaton_boundaries(gravaton_pos, gravaton_width, gravaton_height, 2, chatter.blue, 3)
            display_text(10, 450, f"FPS: {int(fps)}", text_color, 3)
        # Handle user input
        press = chatter.snapshot_input()
        if press:
            pressed_keys.extend(key for key in press if key not in pressed_keys)
        
        if Player_con_ROCK in pressed_keys and is_player_holding_rock:
            is_player_holding_rock = False
            is_rock_moveing = True
        if Player_con_ESC in pressed_keys:
            while True:
                chatter.clear(background_color)
                press = chatter.snapshot_input()
                chatter.display_text(0, 5, "ARE YOU SURE YOU WANT TO QUIT?/qYq TO QUIT./qNq TO GO BACK TO THE GAME.", text_color, 3)
                if press:
                    pressed_keys.extend(key for key in press if key not in pressed_keys)
                if "y" in pressed_keys:
                    save_data()
                    restart_program()
                if "n" in pressed_keys:
                    break
                chatter.display_screen()
        # Set movement speed based on shift key press
        speed = delta_speed(fps, 500) if Player_con_RUN in pressed_keys else delta_speed(fps, 250)
        poison_arrow_check()
        # Handle player movement and update player position
        x, y, velocity_x, velocity_y, on_ground, jump_timer = handle_player_movement(
            x, y, pressed_keys, speed, scale, col, player_width, player_height, block_width, block_height, delta_speed(fps, 200), 70, 70, 1)
        
        # Display UI information
        display_text(0, 10, vir, text_color, 3)
        display_text(530, 10, f"LIVES: {lives}", text_color, 3)
        display_text(300, 10, f"COINS: {coins}", text_color, 3)

        # Calculate FPS
        current_time = time.time()
        elapsed_time = current_time - start_time
        fps = 1.0 / max(elapsed_time, frame_duration)  # Avoid division by 0 for very short frames

        # Enforce FPS limit (no longer needed, as it's handled by the frame duration)
        # Wait to enforce FPS limit
        if no_gravity:
            display_text(x - 10, y - 20, str(0 if (300 - no_gravity_time) == 300 else (300 - no_gravity_time)), text_color, 3)
        chatter.display_screen()

        # Call level logic and collision checks
        do_level()
        check_if_dead()

        move_walker(pressed_keys, debug)

        try:
            invis_pos, is_invis = check_all_invis_col(
                invis_pos, x, y, player_width, player_height, invis_width, invis_height, debug
            )
        except Exception:
            pass

        check_all_coins_col()
        check_all_eme_col()
        rock_check()
        move_rock()
        do_boss()
        do_arrow()
        do_shooter()
        check_coins()
        do_poison_shooter()
        do_poison_arrow()
        do_grava_shooter()
        do_grava_shooterL()
        do_grava_shooterR()
        do_grava_shooterU()
        do_gravaton()
        gravaton_check()
        pressed_keys.clear()
    except Exception as e:
        error_message = str(e).upper() + "/RESTART?/TYPE Y"  # Convert the error message to uppercase
        display_text(0, 450, error_message, text_color, 3)
        print(e)
        chatter.display_screen()
        press = chatter.snapshot_input()
        if press:
            pressed_keys.extend(key for key in press if key not in pressed_keys)
        if "y" in pressed_keys:
            restart_program()