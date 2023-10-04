from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 599  # x 좌표는 랜덤,  y좌표는 599에서 시작
        self.falling_speed = random.randint(5, 20)   # 공마다 떨어지는 속도를 랜덤하게 설정함
        # 랜덤 값에 따라 큰 공과 작은 공을 결정 -> 객체 생성시 큰공과 작은 공중 랜덤하게 생성하도록 함
        self.image = load_image('ball21x21.png') if (random.randint(0, 100) % 2) == 1 else load_image('ball41x41.png')

    def update(self):
        self.y -= self.falling_speed  # 공은 랜덤하게 설정된 속도로 아래를 향해 이동함
        self.is_fall_on_grass() # 공이 땅에 떨어 졌는지 확인하고 땅에 닿으면 멈추게하는 함수

    def is_fall_on_grass(self):
        if self.y < 55 + self.image.h // 2: # 땅에 닿았는가를 결정할 때 공의 이미지 크기를 기준으로 계산하게 함
            self.y = 55 + self.image.h // 2
            self.falling_speed = 0

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team  # 소년 10개의 객체를 만들고 월드 리스트에 저장

    balls = [Ball() for i in range(20)]
    world += balls  # 큰 공 작은 공을 랜덤하게 20개 만들어 월드 리스트에 저장


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # game logic
    render_world()  # draw game world
    delay(0.05)

# finalization code

close_canvas()
