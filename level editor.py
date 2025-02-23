import chatter

level = []

walker_pos = [336, 574, 'R', 'alive']

coins_pos = [192, 574, 'N', 432, 574, 'N', 0, 615, 'N', 48, 574, 'N', 96, 533, 'N', 576, 533, 'N']

lives_pos = [336, 574, 'N']

invis_pos = []

shooter_pos = []

poison_shooter_pos = []

level_ID = level

grass_block = chatter.load_sprite("assets\\grass.png")
stone_block = chatter.load_sprite("assets\\stone.png")
walker = chatter.load_sprite("assets\\walker.png")
eme = chatter.load_sprite("assets\\live.png")
coin = chatter.load_sprite("assets\\coin.png")
invis = chatter.load_sprite("assets\\Invincibility.png")
cr = chatter.load_sprite("assets\\level_editor_cursor.png")
platform_1 = chatter.load_sprite("assets\\platform1.png")
platform_2 = chatter.load_sprite("assets\\platform2.png")
platform_3 = chatter.load_sprite("assets\\platform3.png")
lava = chatter.load_sprite("assets\\lava.png")
rock = chatter.load_sprite("assets\\rock.png")
boss = chatter.load_sprite("assets\\player_invis6.png")
door_top = chatter.load_sprite("assets\\door_top.png")
door_bottom = chatter.load_sprite("assets\\door_bottom.png")
shooter = chatter.load_sprite("assets\\shooter.png")
poison_shooter = chatter.load_sprite("assets\\shooter_poison.png")
poison_lava = chatter.load_sprite("assets\\poison_lava.png")
grava_shooter = chatter.load_sprite("assets\\grava_shooter.png")
grava_shooterL = chatter.load_sprite("assets\\grava_shooter_L.png")
grava_shooterR = chatter.load_sprite("assets\\grava_shooter_R.png")
grava_shooterU = chatter.load_sprite("assets\\grava_shooter_U.png")

crx = 0
cry = 0

grid = True

pressed_keys = []

bid = 1



def add_tile(cursor_x, cursor_y, block_id):
    new_tile = (cursor_x, cursor_y, block_id)
    level.append(new_tile)  # Appending the new tile to the level list

def remove_tile(cursor_x, cursor_y):
    global level  # Ensure we're modifying the global level list
    for tile in level:
        if tile[0] == cursor_x and tile[1] == cursor_y:  # Check if X and Y match
            level.remove(tile)  # Remove the matching tile
            print(f"Tile at ({cursor_x}, {cursor_y}) has been removed.")
            return  # Exit the function once the tile is removed
    print(f"No tile found at ({cursor_x}, {cursor_y}).")  # If no match is found

def add_shooter(cursor_x, cursor_y):
    new_tile = (cursor_x, cursor_y)
    shooter_pos.append(new_tile)  # Appending the new tile to the level list

def remove_shooter(cursor_x, cursor_y):
    global shooter_pos  # Ensure we're modifying the global level list
    for tile in shooter_pos:
        if tile[0] == cursor_x and tile[1] == cursor_y:  # Check if X and Y match
            shooter_pos.remove(tile)  # Remove the matching tile
            print(f"Tile at ({cursor_x}, {cursor_y}) has been removed.")
            return  # Exit the function once the tile is removed
    print(f"No tile found at ({cursor_x}, {cursor_y}).")  # If no match is found

def add_poison_shooter(cursor_x, cursor_y):
    new_tile = (cursor_x, cursor_y)
    poison_shooter_pos.append(new_tile)  # Appending the new tile to the level list

def remove_poison_shooter(cursor_x, cursor_y):
    global poison_shooter_pos  # Ensure we're modifying the global level list
    for tile in poison_shooter_pos:
        if tile[0] == cursor_x and tile[1] == cursor_y:  # Check if X and Y match
            poison_shooter_pos.remove(tile)  # Remove the matching tile
            print(f"Tile at ({cursor_x}, {cursor_y}) has been removed.")
            return  # Exit the function once the tile is removed
    print(f"No tile found at ({cursor_x}, {cursor_y}).")  # If no match is found

def add_walker(cursor_x, cursor_y, direction, state):
    # Create and append the new walker attributes
    walker_pos.extend([cursor_x, cursor_y, direction, state])
    print(f"Walker added at ({cursor_x}, {cursor_y}) with direction {direction} and state {state}.")


def remove_walker(cursor_x, cursor_y):
    global walker_pos  # Ensure we modify the global list
    for i in range(0, len(walker_pos), 4):  # Step through the list in chunks of 4
        if walker_pos[i] == cursor_x and walker_pos[i + 1] == cursor_y:
            # Remove the 4 elements representing the walker
            del walker_pos[i:i + 4]
            print(f"Walker at ({cursor_x}, {cursor_y}) has been removed.")
            return
    print(f"No walker found at ({cursor_x}, {cursor_y}).")

def add_coin(cursor_x, cursor_y, state):
    # Append the new coin attributes to the coin_pos list
    coins_pos.append(cursor_x)
    coins_pos.append(cursor_y)
    coins_pos.append(state)
    print(f"Coin added at ({cursor_x}, {cursor_y}) with state {state}.")

def remove_coin(cursor_x, cursor_y):
    global coins_pos  # Ensure we modify the global list
    for i in range(0, len(coins_pos), 3):  # Step through the list in chunks of 3
        if coins_pos[i] == cursor_x and coins_pos[i + 1] == cursor_y:
            # Remove the 3 elements representing the coin
            del coins_pos[i:i + 3]
            print(f"Coin at ({cursor_x}, {cursor_y}) has been removed.")
            return
    print(f"No coin found at ({cursor_x}, {cursor_y}).")

def add_live(cursor_x, cursor_y, state):
    # Append the new coin attributes to the coin_pos list
    lives_pos.append(cursor_x)
    lives_pos.append(cursor_y)
    lives_pos.append(state)
    print(f"Live added at ({cursor_x}, {cursor_y}) with state {state}.")

def remove_live(cursor_x, cursor_y):
    global lives_pos  # Ensure we modify the global list
    for i in range(0, len(lives_pos), 3):  # Step through the list in chunks of 3
        if lives_pos[i] == cursor_x and lives_pos[i + 1] == cursor_y:
            # Remove the 3 elements representing the coin
            del lives_pos[i:i + 3]
            print(f"Live at ({cursor_x}, {cursor_y}) has been removed.")
            return
    print(f"No Live found at ({cursor_x}, {cursor_y}).")

def add_invis(cursor_x, cursor_y, state):
    # Append the new coin attributes to the coin_pos list
    invis_pos.append(cursor_x)
    invis_pos.append(cursor_y)
    invis_pos.append(state)
    print(f"invis added at ({cursor_x}, {cursor_y}) with state {state}.")

def remove_invis(cursor_x, cursor_y):
    global invis_pos  # Ensure we modify the global list
    for i in range(0, len(invis_pos), 3):  # Step through the list in chunks of 3
        if invis_pos[i] == cursor_x and invis_pos[i + 1] == cursor_y:
            # Remove the 3 elements representing the coin
            del invis_pos[i:i + 3]
            print(f"invis at ({cursor_x}, {cursor_y}) has been removed.")
            return
    print(f"No invis found at ({cursor_x}, {cursor_y}).")

while True:
    chatter.clear((0, 255, 255))
    bx = 100
    for block in level_ID:
        bx, by, id = block
        if id == 1:
            chatter.display_sprite(grass_block, bx, by, 3)
        elif id == 2:
            chatter.display_sprite(stone_block, bx, by, 3)
        elif id == 3:
            chatter.display_sprite(platform_1, bx, by, 3)
        elif id == 4:
            chatter.display_sprite(platform_2, bx, by, 3)
        elif id == 5:
            chatter.display_sprite(platform_3, bx, by, 3)
        elif id == 6:
            chatter.display_sprite(lava, bx, by, 3)
        elif id == 7:
            chatter.display_sprite(rock, bx, by, 3)
        elif id == 8:
            chatter.display_sprite(boss, bx, by, 5)
        elif id == 9:
            chatter.display_sprite(door_top, bx, by, 3)
        elif id == 10:
            chatter.display_sprite(door_bottom, bx, by, 3)
        elif id == 11:
            chatter.display_sprite(shooter, bx, by, 3)
        elif id == 12:
            chatter.display_sprite(poison_shooter, bx, by, 3)
        elif id == 13:
            chatter.display_sprite(grava_shooter, bx, by, 3)
        elif id == 14:
            chatter.display_sprite(grava_shooterL, bx, by, 3)
        elif id == 15:
            chatter.display_sprite(grava_shooterR, bx, by, 3)
        elif id == 16:
            chatter.display_sprite(grava_shooterU, bx, by, 3)
    for i in range(0, len(walker_pos), 4):
        walker_pos_x = walker_pos[i]
        walker_pos_y = walker_pos[i + 1]
        if walker_pos[i + 3] == "alive":
            chatter.display_sprite(walker, walker_pos_x, walker_pos_y, 4)
        i += 4
    chatter.display_sprite(cr, crx, cry, 3)
    for i in range(0, len(coins_pos), 3):
        coins_pos_x = coins_pos[i]
        coins_pos_y = coins_pos[i + 1]
        status = coins_pos[i + 2]
        chatter.display_sprite(coin, coins_pos_x, coins_pos_y, 3)
    for i in range(0, len(lives_pos), 3):
        lives_pos_x = lives_pos[i]
        lives_pos_y = lives_pos[i + 1]
        status = lives_pos[i + 2]
        chatter.display_sprite(eme, lives_pos_x, lives_pos_y, 3)
        i += 3
    for i in range(0, len(invis_pos), 3):
        invis_pos_x = invis_pos[i]
        invis_pos_y = invis_pos[i + 1]
        status = invis_pos[i + 2]
        chatter.display_sprite(invis, invis_pos_x, invis_pos_y, 3)
        i += 3
    for i, (pos_x, pos_y) in enumerate(shooter_pos):
        pos_x, pos_y = shooter_pos[i]
        chatter.display_sprite(shooter, pos_x, pos_y, 3)
        i += 2
    for i, (pos_x, pos_y) in enumerate(poison_shooter_pos):
        pos_x, pos_y = poison_shooter_pos[i]
        chatter.display_sprite(poison_shooter, pos_x, pos_y, 3)
        i += 2
    # Input handling
    if not grid:
        press = chatter.snapshot_input()
        if press:
            for key in press:
                if key not in pressed_keys:
                    pressed_keys.append(key)
    else:
        press = chatter.input()

    # Move cursor with WASD
    if not grid:
        if "a" in pressed_keys:
            crx -= 1
        elif "d" in pressed_keys:
            crx += 1
        elif "s" in pressed_keys:
            cry += 1
        elif "w" in pressed_keys:
            cry -= 1
    else:
        if press == "a":
            crx -= 48
        elif press == "d":
            crx += 48
        elif press == "s":
            cry += 41
        elif press == "w":
            cry -= 41

    # Handling the "i" and "k" key presses for changing the block ID
    if press == "i":
        bid += 1
    elif press == "k":
        bid -= 1
    if bid < 1:
        bid = 1
    if bid > 20:
        bid = 20
    if press == "z":
        break

    test = chatter.get_mouse_state()

    chatter.display_text(0, 15, str(bid), chatter.black, 3)
    # Your dictionary
    input_data = test
    left_click = input_data['left_click']
    right_click = input_data['right_click']
    scroll_up = input_data['scroll_up']
    scroll_down = input_data['scroll_down']

    # Add or remove tiles based on mouse input
    if grid:
        if bid <= 2:
            if press == "e":
                add_tile(crx, cry, bid)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 3:
            if press == "e":
                add_walker(crx, cry, "R", "alive")
            if press == "q":
                remove_walker(crx, cry)
        elif bid == 4:
            if press == "e":
                add_coin(crx, cry, "N")
            if press == "q":
                remove_coin(crx, cry)
        elif bid == 5:
            if press == "e":
                add_live(crx, cry, "N")
            if press == "q":
                remove_live(crx, cry)
        elif bid == 6:
            if press == "e":
                add_invis(crx, cry, "N")
            if press == "q":
                remove_invis(crx, cry)
        elif bid == 7:
            if press == "e":
                add_tile(crx, cry, 3)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 8:
            if press == "e":
                add_tile(crx, cry, 4)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 9:
            if press == "e":
                add_tile(crx, cry, 5)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 10:
            if press == "e":
                add_tile(crx, cry, 6)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 11:
            if press == "e":
                add_tile(crx, cry, 7)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 12:
            if press == "e":
                add_tile(crx, cry, 8)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 13:
            if press == "e":
                add_tile(crx, cry, 9)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 14:
            if press == "e":
                add_tile(crx, cry, 10)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 15:
            if press == "e":
                add_poison_shooter(crx, cry)
            if press == "q":
                remove_poison_shooter(crx, cry)
        elif bid == 16:
            if press == "e":
                add_shooter(crx, cry)
            if press == "q":
                remove_shooter(crx, cry)
        elif bid == 17:
            if press == "e":
                add_tile(crx, cry, 13)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 18:
            if press == "e":
                add_tile(crx, cry, 14)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 19:
            if press == "e":
                add_tile(crx, cry, 15)
            if press == "q":
                remove_tile(crx, cry)
        elif bid == 20:
            if press == "e":
                add_tile(crx, cry, 16)
            if press == "q":
                remove_tile(crx, cry)
    chatter.display_screen()
    pressed_keys.clear()



print("Level data\n\n")
print(level)
print("\n\nWalker data\n\n")
print(walker_pos)
print("\n\nCoin data\n\n")
print(coins_pos)
print("\n\nLive data\n\n")
print(lives_pos)
print("\n\nInvis data\n\n")
print(invis_pos)
print("\n\nShooter data\n\n")
print(shooter_pos)
print("\n\nPoison shooter data\n\n")
print(poison_shooter_pos)