# montyhall

# Method
3 modules

## 1. Setup
import random

def setup_game():
    # 자동차가 있는 문 위치를 무작위로 설정
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    return doors

## 2. Player choice
def player_choice(doors):
    # 플레이어가 문 하나를 선택 (0, 1, 2 중 무작위 선택)
    player_selected = random.randint(0, 2)
    
    # 진행자가 염소가 있는 문을 하나 열기
    for i in range(3):
        if i != player_selected and doors[i] == "goat":
            host_revealed = i
            break
    
    return player_selected, host_revealed
## 3. Simulation
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
## 4. Main 

#from monty_hall_1 import setup_game
#from monty_hall_2 import player_choice
#from monty_hall_3 import simulate_game
  
def main():
    n = 1000
    wins_switch = sum(simulate_game(setup_game(), *player_choice(setup_game()), switch=True) for _ in range(n))
    print(f"Switching wins: {wins_switch/n*100:.2f}%")

    wins_no_switch = sum(simulate_game(setup_game(), *player_choice(setup_game()), switch=False) for _ in range(n))
    print(f"No switching wins: {wins_no_switch/n*100:.2f}%")

# Result
Switching wins: 32.10%
No switching wins: 35.40%
