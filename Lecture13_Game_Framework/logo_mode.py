import game_framework
from pico2d import *
def init():
    global image
    global running
    global logo_start_time
    image = load_image('tuk_credit.png')
    running = True
    logo_start_time = get_time()
def finish():
    global image
    del image
def update():
    global running
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        running = False
def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
def handle_events():
    events = get_events()
