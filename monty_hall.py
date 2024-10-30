import random

#from monty_hall_1 import setup_game
#from monty_hall_2 import player_choice
#from monty_hall_3 import simulate_game

def setup_game():
    # 자동차가 있는 문 위치를 무작위로 설정
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    return doors

def player_choice(doors):
    # 플레이어가 문 하나를 선택 (0, 1, 2 중 무작위 선택)
    player_selected = random.randint(0, 2)
    
    # 진행자가 염소가 있는 문을 하나 열기
    for i in range(3):
        if i != player_selected and doors[i] == "goat":
            host_revealed = i
            break
    
    return player_selected, host_revealed

def simulate_game(doors, player_selected, host_revealed, switch=True):
    # 문을 바꿀지 여부에 따라 최종 선택을 결정
    if switch:
        # 플레이어가 고르지 않은 다른 문으로 바꾼다
        for i in range(3):
            if i != player_selected and i != host_revealed:
                final_choice = i
                break
    else:
        # 바꾸지 않으면 처음 선택을 그대로 유지
        final_choice = player_selected
    
    # 최종 선택이 자동차인지 확인하여 결과 반환
    return doors[final_choice] == "car"


def main():
    n = 1000
    switch_wins = 0
    no_switch_wins = 0

    for _ in range(n):
        # 각 게임마다 동일한 doors 설정을 사용
        doors = setup_game()
        player_selected, host_revealed = player_choice(doors)
        
        # switch와 no-switch 케이스에 동일한 초기 조건 사용
        if simulate_game(doors, player_selected, host_revealed, switch=True):
            switch_wins += 1
        if simulate_game(doors, player_selected, host_revealed, switch=False):
            no_switch_wins += 1
    print(f"Switching wins: {switch_wins/n*100:.2f}%")
    print(f"No switching wins: {no_switch_wins/n*100:.2f}%")

if __name__ == "__main__":
    main()    #simulate_game(setup_game(), *player_choice(setup_game()), switch=True)

# problem: 기존 코드, 계속해서 독립적인 게임 생성: 원래 코드에서는 각 시뮬레이션마다 새로운 게임(doors)을 생성했습니다:
