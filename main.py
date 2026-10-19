import os
import time
import math
os.system("clear")

#Grid works like this:
#(0, 0) (1, 0) (2, 0)
#(0, 1) (1, 1)
#(0, 2)
track_1 = [
    "WWWWWWWWWWWWWWWWWWWW",
    "WWWWW..........WWWWW",
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
    "WWWWW..........WWWWW",
    "WWWWWWWWWWWWWWWWWWWW"
]
t1_cp = [
    (4, 9),
    (7, 14),
    (12, 14),
    (12, 4),
    (7, 4),
    (4, 7)
]
track_2 = [
    "WWWWWWWWWWWWWWwWWWWWW",
    "W.1..2WWWW........WWW",
    "WW.....WWw.........WW",
    "WWW.....WW..........W",
    "WWWW....wW....wWW...W",
    "WWWW....WWW....wW...W",
    "WWW.....WWWW....W...W",
    "WW......WWWW...wW...W",
    "W......WWWW....w....W",
    "W....WWWWW....wW....W",
    "WW....WWW.....W...wWW",
    "WWW..........Ww.....W",
    "WWWW........WWWW....W",
    "WFFWWWWWWWWWWW......W",
    "W..................WW",
    "WW................WWW",
    "WWW..............WWWW",
    "WWWWWWWWWWWWWWWWWWWWW"
]
t2_cp = [
    (3, 1),
    (4, 9),
    (14, 3),
    (16, 13),
    (2, 13)
]
track_3 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WW...........Fw2.......................WWWW",
    "WW...........Fw.........................wwW",
    "WW...........Fw1.........................wW",
    "WW.....Wwwwwwwwwwwwwwwwwwwwwwwwwwww......wW",
    "WWw......wwwwww.............wwwwww.......wW",
    "WWww.......www...............wwww........wW",
    "WWwww........ww.....wwww.......w.........wW",
    "WWwwwww.......ww......www................wW",
    "WWwwwwwww......ww.......wwww.............wW",
    "WWwwwwww.......ww..........www..........wwW",
    "WWwwwww........www..........wwwwwwwwwwwwwwW",
    "WWwww..........wwwwww.........wwwwwwwwwwwwW",
    "WWw............wwwwwwwwww.......wwwwwwwwwwW",
    "WW............www.......www.......wwwwwwwwW",
    "WW...........wwww.........www..........wwwW",
    "WW..........wwwww...........www..........wW",
    "WWw.......wwww........w.......wwww.......wW",
    "WWww..................ww................wwW",
    "WWwww................wwww..............wwwW",
    "wwwwww..............wwwwww............wwwww",
    "WWwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwW"
]
t3_cp = [
    (16, 2),
    (35, 3),
    (31, 8),
    (23, 6),
    (17, 7),
    (34, 17),
    (23, 16),
    (14, 18),
    (7, 17),
    (10, 8),
    (4, 4),
    (13, 1)
]
track_4 = [
    "WWWWWWWWWWWW",
    "WFW........W",
    "W.W.WWWWW..W",
    "W.W....1W.WW",
    "W.WWWWW2W..W",
    "W.W...WWWW.W",
    "W.W.W..WW..W",
    "W...WW.....W",
    "WWWWWWWWWWWW"
]
t4_cp = [
    (7, 3),
    (3, 3),
    (3, 1),
    (9, 1),
    (10, 5),
    (8, 7),
    (4, 5),
    (2, 7),
    (1, 1)
]

track_template_list = [track_1, track_2, track_3, track_4]

print("What track would you like to race on (#)?")
print("1) Oval")
print("2) Snake")
print("3) Z-Track")
print("4) Baby Race")
while 1:
    track = input()
    if 1 <= int(track) <= len(track_template_list):
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

if player_count > 1:
    px2, py2 = 0, 0
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
p2_turns = 0
p1_turns = 0
p1_checkpoints = 0
p2_checkpoints = 0
slip = []
points = []

def checkpoint_prox(px, py, current_cp):
    if int(track) == 1:
        checkpoints = t1_cp
    elif int(track) == 2:
        checkpoints = t2_cp
    elif int(track) == 3:
        checkpoints = t3_cp
    elif int(track) == 4:
        checkpoints = t4_cp
    next_cp = (current_cp + 1) % len(checkpoints)
    cp_x, cp_y = checkpoints[next_cp]
    distance = math.sqrt((px - cp_x)**2 + (py - cp_y)**2)
    return distance

def draw_frame():
    print("\033[2J\033[H\033[3J", end="")
    print(f"--- Vector Racing --- Turns: {min(p1_turns, p2_turns)}")
    if player_turn == 1:
        print(f"\u001b[1m\033[38;2;255;165;0m--- Player {player_turn}'s Turn! ---\u001b[0m\033[0m")
    elif player_turn == 2:
        print(f"\u001b[1m\033[34m--- Player {player_turn}'s Turn! ---\u001b[0m\033[0m")
    if "n" in slip:
        print("Eligible for \033[103mNorth\033[0m Slipstream")
    elif "e" in slip:
        print("Eligible for \033[103mEast\033[0m Slipstream")
    elif "s" in slip:
        print("Eligible for \033[103mSouth\033[0m Slipstream")
    elif "w" in slip:
        print("Eligible for \033[103mWest\033[0m Slipstream")
    if player_turn == 1:
        print(f"Current Velocity Vector: ({vx1}, {vy1})")
        print(f"Next Move Preview: Coasting to ({px1+vx1+ax1}, {py1+vy1+ay1})")
    elif player_turn == 2:
        print(f"Current Velocity Vector: ({vx2}, {vy2})")
        print(f"Next Move Preview: Coasting to ({px2+vx2+ax2}, {py2+vy2+ay2})")
    full_frame = ""
    for y in range(height):
        row = ""
        for x in range(width):
            tile = track_template[y][x]
            if x == px1 and y == py1:
                if abs(vy1) >= abs(vx1):
                    if vy1 >= 0:
                        row += "\033[38;2;255;165;0m" + "▼ " + "\033[0m"
                    else:
                        row += "\033[38;2;255;165;0m" + "▲ " + "\033[0m"
                elif abs(vx1) > abs(vy1):
                    if vx1 > 0:
                        row += "\033[38;2;255;165;0m" + "► " + "\033[0m"
                    else:
                        row += "\033[38;2;255;165;0m" + "◄ " + "\033[0m"
            elif tile == "W" or tile == "w":
                row += "\033[37m" + "█ " + "\033[0m"
            elif tile == "F" or tile == "f":
                row += "\033[32m" + "🏁" + "\033[0m"
            elif player_count > 1:
                if x == px2 and y == py2:
                    if abs(vy2) >= abs(vx2):
                        if vy2 >= 0:
                            row += "\033[34m" + "▼ " + "\033[0m"
                        else:
                            row += "\033[34m" + "▲ " + "\033[0m"
                    elif abs(vx2) > abs(vy2):
                        if vx2 > 0:
                            row += "\033[34m" + "► " + "\033[0m"
                        else:
                            row += "\033[34m" + "◄ " + "\033[0m"
                elif player_turn == 2 and x == px2 + vx2 + ax2 and y == py2 + vy2 + ay2:
                    row += "\033[94m" + "● " + "\033[0m"
                elif player_turn == 1 and x == px1 + vx1 + ax1 and y == py1 + vy1 + ay1:
                    row += "\033[93m" + "● " + "\033[0m"
                elif player_turn == 2 and abs(x - (px2+vx2)) <= 1 and abs(y - (py2+vy2)) <= 1:
                    row += "* "
                elif player_turn == 1 and abs(x - (px1+vx1)) <= 1 and abs(y - (py1+vy1)) <= 1:
                    row += "* "
                else:
                    row += ". "
            elif player_turn == 1 and x == px1 + vx1 + ax1 and y == py1 + vy1 + ay1:
                row += "\033[93m" + "● " + "\033[0m"
            elif player_turn == 1 and abs(x - (px1+vx1)) <= 1 and abs(y - (py1+vy1)) <= 1:
                row += "∗ "
            else:
                row += ". "                    
        full_frame += row + "\n"
    print(full_frame, end="", flush=True)
    if player_turn == 1:
        print(f"\nAdjusted Input Accel Vector: ({ax1}, {ay1})")
    elif player_turn == 2:
        print(f"\nAdjusted Input Accel Vector: ({ax2}, {ay2})")

def get_line_points(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return [{"x": x1, "y": y1}]
    global points
    points.clear()
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

def slipstream(trail_x, lead_x, trail_y, lead_y, trail_vx, trail_vy):
    global slip
    slip.clear()
    dx = lead_x - trail_x
    dy = lead_y - trail_y
    if dx == 1 and dy == 0 and trail_vx > 0: #East
        slip.append("e")
    if dx == -1 and dy == 0 and trail_vx <= 0 and abs(trail_vx) >= abs(trail_vy): #West
        slip.append("w")
    if dy == 1 and dx == 0 and trail_vy > 0: #South
        slip.append("s")
    if dy == -1 and dx == 0 and trail_vy <= 0 and abs(trail_vy) >= abs(trail_vx): #North
        slip.append("n")
def turn_order():
    global p1_checkpoints
    global p2_checkpoints
    global player_turn
    global round_start
    p1_dist = checkpoint_prox(px1, py1, p1_checkpoints)
    if player_count > 1:
        p2_dist = checkpoint_prox(px2, py2, p2_checkpoints)
    if p1_dist < 2.5:
        p1_checkpoints += 1
    if player_count > 1:
        if p2_dist < 2.5:
            p2_checkpoints += 1
        if p1_turns == p2_turns:
            if p1_checkpoints > p2_checkpoints:
                player_turn = 1
                round_start = 1
                slipstream(px2, px1, py2, py1, vx2, vy2)
            elif p2_checkpoints > p1_checkpoints:
                player_turn = 2
                round_start = 2
                slipstream(px1, px2, py1, py2, vx1, vy1)
            elif p1_dist < p2_dist:
                player_turn = 1
                round_start = 1
                slipstream(px2, px1, py2, py1, vx2, vy2)
            else:
                player_turn = 2
                round_start = 2
                slipstream(px1, px2, py1, py2, vx1, vy1)
        else:
            if p2_turns < p1_turns:
                player_turn = 2
            else:
                player_turn = 1
    else:
        player_turn = 1
        round_start = 1

while True:
    time.sleep(0.03)
    turn_order()
    time.sleep(0.03)
    draw_frame()
    time.sleep(0.03)
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

            if round_start == 1:
                if "n" in slip:
                    stream = input("Slipstream north (y, n)? ")
                    if stream == "y":
                        new_py2 -= 1
                if "e" in slip:
                    stream = input("Slipstream east (y, n)? ")
                    if stream == "y":
                        new_px2 += 1
                if "s" in slip:
                    stream = input("Slipstream south (y, n)? ")
                    if stream == "y":
                        new_py2 += 1
                if "w" in slip:
                    stream = input("Slipstream west (y, n)? ")
                    if stream == "y":
                        new_px2 -= 1

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
            px2, py2 = new_px2, new_py2
            if px2 == px1 and py2 == py1:
                print("\nYou have crashed into Player 1! Player 1 wins!")
                break
            if hit_wall:
                print("\nYou have crashed! Player 1 wins!")
                break

            travel_path.clear()
            ax2 = 0
            ay2 = 0
            p2_turns += 1
            
            if crossed_finish:
                print(f"\nYou finished! You completed in {p2_turns} turns!")
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

            if round_start == 2:
                if "n" in slip:
                    stream = input("Slipstream north (y, n)? ")
                    if stream == "y":
                        new_py1 -= 1
                if "e" in slip:
                    stream = input("Slipstream east (y, n)? ")
                    if stream == "y":
                        new_px1 += 1
                if "s" in slip:
                    stream = input("Slipstream south (y, n)? ")
                    if stream == "y":
                        new_py1 += 1
                if "w" in slip:
                    stream = input("Slipstream west (y, n)? ")
                    if stream == "y":
                        new_px1 -= 1

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
            px1, py1 = new_px1, new_py1
            if player_count > 1:
                if px1 == px2 and py1 == py2:
                    print("\nYou have crashed into Player 2! Player 2 wins!")
                    break
            if hit_wall:
                if player_count > 1:
                    print("\nYou have crashed! Player 2 wins!")
                else:
                    print("\nYou have crashed! Game over.")
                break

            ax1 = 0
            ay1 = 0
            travel_path.clear()
            p1_turns += 1

            if crossed_finish:
                print(f"\nYou finished! You completed in {p1_turns} turns!")
                if player_count > 2:
                    print("Player 1 wins!")
                break
