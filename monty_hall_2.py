def player_choice(doors):
    # 플레이어가 문 하나를 선택 (0, 1, 2 중 무작위 선택)
    player_selected = random.randint(0, 2)
    
    # 진행자가 염소가 있는 문을 하나 열기
    for i in range(3):
        if i != player_selected and doors[i] == "goat":
            host_revealed = i
            break
    
    return player_selected, host_revealed
