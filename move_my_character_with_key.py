from pico2d import *

open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('fox.png')

def handle_events():
    global running, dir, x, MoveRight, MoveFront, StandRight, StandFront, state

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                MoveRight = True
                state = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                MoveRight = False
                state = 1
            elif event.key == SDLK_UP:
                dir += 1
                MoveFront = True
                state = 2
            elif event.key == SDLK_DOWN:
                dir -= 1
                MoveFront = False
                state = 2
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                StandRight = True
                state = 3
            elif event.key == SDLK_LEFT:
                dir += 1
                StandRight = False
                state = 3
            elif event.key == SDLK_UP:
                dir -= 1
                StandFront = True
                state = 4
            elif event.key == SDLK_DOWN:
                dir += 1
                StandFront = False
                state = 4

running = True
MoveRight = True
MoveFront = True
StandRight = True
StandFront = True

state = 3
x = 800 // 2
y = 600 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    ground.draw(400, 300, 800, 600)

    if MoveRight == True and state == 1:
        character.clip_draw(frame * 30 + 4, 157, 30, 30, x, y, 90, 90)

    elif MoveRight == False and state == 1:
        character.clip_composite_draw(frame * 30 + 4, 157, 30, 30, 0, 'h' , x, y, 90, 90)

    if MoveFront == True and state == 2:
        character.clip_composite_draw(frame * 30 + 5, 224, 30, 30, 0, 'v', x, y, 90, 90)

    elif MoveFront == False and state == 2:
        character.clip_draw(frame * 30 + 5, 224, 30, 30, x, y, 90, 90)

    if StandRight == True and state == 3:
        character.clip_draw(frame * 30 + 131, 90, 30, 30, x, y, 90, 90)

    elif StandRight == False and state == 3:
        character.clip_composite_draw(frame * 30 + 131, 90, 30, 30, 0, 'h' , x, y, 90, 90)

    if MoveFront == True and state == 4:
        character.clip_composite_draw(frame * 30 + 158, 91, 30, 30, 0, 'v', x - 10, y, 90, 90)

    elif MoveFront == False and state == 4:
        character.clip_draw(frame * 30 + 158, 91, 30, 30, x - 10, y, 90, 90)

    update_canvas()
    handle_events()

    if state == 1 or state == 2 or state == 4:
        frame = (frame + 1) % 3
    elif state == 3:
        frame = (frame + 1) % 2

    if x < 760 and MoveRight == True and state == 1:
        x += dir * 10
    elif x > 40 and MoveRight == False and state == 1:
        x += dir * 10
    elif y < 540 and MoveFront == True and state == 2:
        y += dir * 10
    elif y > 40 and MoveFront == False and state == 2:
        y += dir * 10

    delay(0.1)

close_canvas()

