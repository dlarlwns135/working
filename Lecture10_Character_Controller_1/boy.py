from pico2d import load_image

class Idle:
    @staticmethod
    def enter():
        print('IDLE Enter - 고개숙이기')
        pass

    @staticmethod
    def exit():
        print('IDLE Exit - 고개들기')
        pass

    @staticmethod
    def do():
        print('IDLE Do')
        #boy.frame = (boy.frame + 1) % 8
        pass

    @staticmethod
    def draw():
        pass
class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine()
        self.state_machine.start()

    def update(self):
        #self.frame = (self.frame + 1) % 8
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.action * 100, 100, 100, self.x, self.y)

class StateMachine:
    def __init__(self):
        self.cur_state = Idle
    def start(self):
        self.cur_state.enter()
    def update(self):
        self.cur_state.do()
    def draw(self):
        self.cur_state.draw()
