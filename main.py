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
    "WwW.S.WWWWWWw.....wW", 
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
    "W..S..WWWW.......WWW", 
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
    "W..................W", 
    "WW.................W", 
    "WWWWWWWWWWWWWWWWWWWW"
]
track_template_list = [track_1]

print("What track would you like to race on (#)?")
print("1) Oval")
print("2) Snake")
while 1:
    track = input()
    if 1 <= int(track) <= 1:
        break
    else:
        print("Please pick a track number.")
if 1 <= int(track) <= len(track_template_list):
    track_template = track_template_list[int(track)-1]

px, py = 0, 0
height = len(track_template)
width = len(track_template[0])
for y in range(height):
    for x in range(width):
        if track_template[y][x] == "S":
            px, py = x, y

vx, vy = 0, 0
ax, ay = 0, 0
turns = 0

def draw_frame():
    os.system('clear')
    print(f"--- Vector Racing --- Turns: {turns}")
    print(f"Current Velocity Vector: ({vx}, {vy})")
    print(f"Next Move Preview: Coasting to ({px+vx+ax}, {py+vy+ay})")
    for y in range(height):
        row = ""
        for x in range(width):
            if x == px and y == py:
                row += "p "
            elif x == px + vx + ax and y == py + vy + ay:
                row += "o "
            else:
                tile = track_template[y][x]
                if tile == "W" or tile == "w":
                    row += "W "
                elif tile == "F" or tile == "f":
                    row += "F "
                else:
                    row += ". "
        print(row)
    print(f"\nAdjusted Input Accel Vector: ({ax}, {ay})")

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
    return track_template[y][x] == "W"

while True:
    draw_frame()
    user_input = input("Enter action (w/a/s/d to adjust accel, space to reset, enter to comfirm): ").lower().strip()

    if user_input == 'w':
        ay = max(-1, ay - 1)
    elif user_input == 's':
        ay = min(1, ay + 1)
    elif user_input == 'a':
        ax = max(-1, ax - 1)
    elif user_input == 'd':
        ax = min(1, ax + 1)
    elif user_input == ' ':
        ax = 0
        ay = 0
    elif user_input == '':
        vx += ax
        vy += ay
        old_px, old_py = px, py
        new_px = px + vx
        new_py = py + vy

        travel_path = get_line_points(old_px, old_py, new_px, new_py)
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
            print("\nYou have crashed! Game over.")
            break

        px, py = new_px, new_py
        turns += 1
        ax = 0
        ay = 0

        if crossed_finish:
            print(f"\n You finished! You completed in {turns} turns!")
            break