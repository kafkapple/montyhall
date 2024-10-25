import random

def setup_game():
    # 자동차가 있는 문 위치를 무작위로 설정
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    return doors
