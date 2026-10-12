import os

width, height = 20, 15
inner_x1, inner_x2 = 6, 14
inner_y1, inner_y2 = 4, 10
finish_x = 10
finish_y_start = 11
finish_y_end = 13

px, py = 2, 2
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
        px += vx
        py += vy
        turns += 1

        ax = 0
        ay = 0

        if px <= 0 or px >= width - 1 or py <= 0 or py >= height - 1:
            print("\n You hit the outer wall. Game over!")
            break
        if inner_x1 <= px <= inner_x2 and inner_y1 <= py <= inner_y2:
            print("\n You hit the inner wall.")
        if px <= finish_x and finish_y_start <= py <= finish_y_end:
            print(f"\n You finished! You completed in {turns} turns!")