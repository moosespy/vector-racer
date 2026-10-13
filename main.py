import os
import time
track_1 = [
    "WWWWWWWWWWWWWWWWWWWW", 
    "WWWW............wwWW", 
    "WWw..............wwW", 
    "Ww......wwww......wW", 
    "Ww.....wwWwww.....wW", 
    "WW.....wWWWWw.....wW", 
    "WWFFFFFwWWWWw.....wW", 
    "WWWWWWWwWWWWw.....wW", 
    "Ww.1.2.WWWWWw.....wW", 
    "Ww.....WWWwWw.....wW", 
    "WW.....WWwwWw.....WW", 
    "WW.....WWWwww.....wW", 
    "WW.....WWwwww.....wW", 
    "Ww......wwww......wW", 
    "Www..............wwW", 
    "WWww............wwwW", 
    "WWWWWWWWWWWWWWWWWWWW"
]
track_2 = [
    "WWWWWWWWWWWWWWWWWWWW", 
    "W.1.2.WWWW.......WWW", 
    "WW.....WW.........WW", 
    "WWW.....WW...WW....W", 
    "WWWW.....Ww...WW...W", 
    "WWWW....WWWW...W...W", 
    "WWW.....WWWW...W...W", 
    "WW......WWWW...W...W", 
    "W......WWWW....W...W", 
    "W....WWWWW....WW...W", 
    "WW....WWW....WW...WW", 
    "WWW.........WW.....W", 
    "WWWW.......WWWWW...W", 
    "WFFWWWWWWWWWWW.....W", 
    "W.................WW", 
    "WW...............WWW", 
    "WWWWWWWWWWWWWWWWWWWW"
]
track_template_list = [track_1, track_2]

print("What track would you like to race on (#)?")
print("1) Oval")
print("2) Snake")
while 1:
    track = input()
    if 1 <= int(track) <= 2:
        break
    else:
        print("Please pick a track number.")
if 1 <= int(track) <= len(track_template_list):
    track_template = track_template_list[int(track)-1]

print("How many players are playing (1, 2)?")
while 1:
    player_count = input()
    if 1 <= int(player_count) <= 2:
        break
    else:
        print("Please pick a valid amount of players.")
player_count = int(player_count)


height = len(track_template)
width = len(track_template[0])
for y in range(height):
    for x in range(width):
        if track_template[y][x] == "1":
            px1, py1 = x, y
        if player_count > 1:
            if track_template[y][x] == "2":
                px2, py2 = x, y

vx1, vy1, vx2, vy2 = 0, 0, 0, 0
ax1, ay1, ax2, ay2 = 0, 0, 0, 0
turns = 0
player_turn = 1

def draw_frame():
    os.system('clear')
    print(f"--- Vector Racing --- Turns: {turns}")
    print(f"--- Player {player_turn}'s Turn! ---")
    if player_turn == 1:
        print(f"Current Velocity Vector: ({vx1}, {vy1})")
        print(f"Next Move Preview: Coasting to ({px1+vx1+ax1}, {py1+vy1+ay1})")
    elif player_turn == 2:
        print(f"Current Velocity Vector: ({vx2}, {vy2})")
        print(f"Next Move Preview: Coasting to ({px2+vx2+ax2}, {py2+vy2+ay2})")
    for y in range(height):
        row = ""
        for x in range(width):
            tile = track_template[y][x]
            if x == px1 and y == py1:
                if abs(vy1) >= abs(vx1):
                    if vy1 >= 0:
                        string = "\033[38;2;255;165;0m" + "▼ " + "\033[0m"
                    else:
                        string = "\033[38;2;255;165;0m" + "▲ " + "\033[0m"
                elif abs(vx1) > abs(vy1):
                    if vx1 > 0:
                        string = "\033[38;2;255;165;0m" + "► " + "\033[0m"
                    else:
                        string = "\033[38;2;255;165;0m" + "◄ " + "\033[0m"
                row += string
            elif tile == "W" or tile == "w":
                string = "\033[37m" + "█ " + "\033[0m"
                row += string
            elif tile == "F" or tile == "f":
                string = "\033[32m" + "🏁" + "\033[0m"
                row += string
            elif player_count > 1:
                if x == px2 and y == py2:
                    if abs(vy2) >= abs(vx2):
                        if vy2 >= 0:
                            string = "\033[34m" + "▼ " + "\033[0m"
                        else:
                            string = "\033[34m" + "▲ " + "\033[0m"
                    elif abs(vx2) > abs(vy2):
                        if vx2 > 0:
                            string = "\033[34m" + "► " + "\033[0m"
                        else:
                            string = "\033[34m" + "◄ " + "\033[0m"
                    row += string                
                elif player_turn == 2 and x == px2 + vx2 + ax2 and y == py2 + vy2 + ay2:
                    string = "\033[94m" + "● " + "\033[0m"
                    row += string
                elif player_turn == 2 and abs(x - (px2+vx2)) <= 1 and abs(y - (py2+vy2)) <= 1:
                    row += "* "
                elif player_turn == 1 and x == px1 + vx1 + ax1 and y == py1 + vy1 + ay1:
                    string = "\033[93m" + "● " + "\033[0m"
                    row += string
                elif player_turn == 1 and abs(x - (px1+vx1)) <= 1 and abs(y - (py1+vy1)) <= 1:
                    row += "* "
                else:
                    row += ". "
            elif player_turn == 1 and abs(x - (px1+vx1)) <= 1 and abs(y - (py1+vy1)) <= 1:
                row += "* "
            elif player_turn == 1 and x == px1 + vx1 + ax1 and y == py1 + vy1 + ay1:
                string = "\033[93m" + "● " + "\033[0m"
                row += string
            else:
                row += ". "                    
        print(row)
    if player_turn == 1:
        print(f"\nAdjusted Input Accel Vector: ({ax1}, {ay1})")
    elif player_turn == 2:
        print(f"\nAdjusted Input Accel Vector: ({ax2}, {ay2})")
        

def get_line_points(x1, y1, x2, y2):
    points = []
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while True:
        points.append({"x": x1, "y": y1})
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points

def wall_collide(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return True
    return track_template[y][x] == "W" or track_template[y][x] == "w"

while True:
    draw_frame()
    user_input = input("Enter action (w/a/s/d to adjust accel, space to reset, enter to confirm): ").lower().strip()
    if player_turn == 2:
        if user_input == 'w':
            ay2 = max(-1, ay2 - 1)
        elif user_input == 's':
            ay2 = min(1, ay2 + 1)
        elif user_input == 'a':
            ax2 = max(-1, ax2 - 1)
        elif user_input == 'd':
            ax2 = min(1, ax2 + 1)
        elif user_input == ' ':
            ax2 = 0
            ay2 = 0
        elif user_input == '':
            vx2 += ax2
            vy2 += ay2
            old_px2, old_py2 = px2, py2
            new_px2 = px2 + vx2
            new_py2 = py2 + vy2

            travel_path = get_line_points(old_px2, old_py2, new_px2, new_py2)
            hit_wall = False
            crossed_finish = False
            for step in travel_path:
                sx, sy = step["x"], step["y"]
                if wall_collide(sx, sy):
                    hit_wall = True
                    break
                if track_template[sy][sx] == "F":
                    crossed_finish = True
                    break
            if hit_wall:
                print("\nYou have crashed! Player 1 wins!")
                break

            px2, py2 = new_px2, new_py2
            player_turn = 1
            turns += 1
            travel_path = []
            ax2 = 0
            ay2 = 0

            if crossed_finish:
                print(f"\nYou finished! You completed in {turns} turns!")
                print("Player 2 wins!")
                break
    elif player_turn == 1:
        if user_input == 'w':
            ay1 = max(-1, ay1 - 1)
        elif user_input == 's':
            ay1 = min(1, ay1 + 1)
        elif user_input == 'a':
            ax1 = max(-1, ax1 - 1)
        elif user_input == 'd':
            ax1 = min(1, ax1 + 1)
        elif user_input == ' ':
            ax1 = 0
            ay1 = 0
        elif user_input == '':
            vx1 += ax1
            vy1 += ay1
            old_px1, old_py1 = px1, py1
            new_px1 = px1 + vx1
            new_py1 = py1 + vy1

            travel_path = get_line_points(old_px1, old_py1, new_px1, new_py1)
            hit_wall = False
            crossed_finish = False
            for step in travel_path:
                sx, sy = step["x"], step["y"]
                if wall_collide(sx, sy):
                    hit_wall = True
                    break
                if track_template[sy][sx] == "F":
                    crossed_finish = True
                    break
            if hit_wall:
                if player_count > 1:
                    print("\nYou have crashed! Player 2 wins!")
                else:
                    print("\nYou have crashed! Game over.")
                break

            px1, py1 = new_px1, new_py1
            ax1 = 0
            ay1 = 0
            travel_path = []

            if crossed_finish:
                print(f"\nYou finished! You completed in {turns} turns!")
                if player_count > 2:
                    print("Player 1 wins!")
                break
            if player_count > 1:
                player_turn = 2
            elif player_count == 1:
                turns += 1