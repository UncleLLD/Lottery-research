# FileUsing: 随机生成一个双色球序列
import random


def generate_ssq_sequence():
    green_balls = [i for i in range(1, 34)]
    red_balls = [i for i in range(1, 17)]

    random_green_balls = random.sample(green_balls, 6)
    random_red_ball = random.choice(red_balls)

    res = sorted(random_green_balls) + [random_red_ball]
    return res


res = generate_ssq_sequence()
print(res)
