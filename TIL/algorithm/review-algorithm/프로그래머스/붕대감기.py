def solution(bandage, health, attacks):
    atk_log = {} # sec : demage
    max_hp = health
    for attack in attacks:
        atk_log[attack[0]] = attack[1]
    sec = 1
    bonus_sec = 0
    while health > 0 and sec <= attacks[-1][0]:
        if sec in atk_log:
            health = health - atk_log[sec]
            bonus_sec = 0
            sec += 1
            if health <= 0:
                return -1
            continue
        health += bandage[1]
        bonus_sec += 1
        if bonus_sec == bandage[0]:
            health += bandage[2]
            bonus_sec = 0
        if health > max_hp:
            health = max_hp
        sec += 1
    return health