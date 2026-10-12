import os

width, height = 20, 15
inner_x1, inner_x2 = 6, 14
inner_y1, inner_y2 = 1, 10
finish_x = 15
finish_y_start = 1
finish_y_end = 3

px, py = 2, 2
vx, vy = 0, 0
ax, ay = 0, 0
turns = 0

def draw_frame():
    os.system('clear')
    print(f"{px}, {py}")
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
            elif x == 0 or x == width - 1 or y == 0 or y == height - 1:
                row += "x "
            elif inner_x1 <= x <= inner_x2 and inner_y1 <= y <= inner_y2:
                row += "x "
            elif x == finish_x and finish_y_start <= y <= finish_y_end:
                row += "f "
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
    if x <= 0 or x >= width - 1 or y <= 0 or y >= height - 1:
        return True
    if inner_x1 <= x <= inner_x2 and inner_y1 <= y <= inner_y2:
        return True
    return False

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
        for step in travel_path:
            if wall_collide(step["x"], step["y"]):
                hit_wall = True
                break
        if hit_wall:
            print("\nYou have crashed! Game over.")
            break

        px, py = new_px, new_py
        turns += 1
        ax = 0
        ay = 0

        if old_px > finish_x and px <= finish_x and finish_y_start <= py <= finish_y_end:
            print(f"\n You finished! You completed in {turns} turns!")
            break