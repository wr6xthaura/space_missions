from missions import *

def main():

    show_missions(missions_list)

    while True:
        direction = input("Введите направление для поиска: ")
        if not direction:
            print('Вы не ввели направление для поиска.\n')
            continue
        else:
            break

    find_mission = search_mission(direction)

    if not find_mission:
        print(f'Миссий по направлению {direction} не найдено.')
        all_direction = set(mission["direction"] for mission in missions_list)
        print('Доступные направления:', *all_direction)
    else:
        print(f'Найдено миссий по направлению {direction}:')
        show_missions(find_mission)

if __name__ == "__main__":
    main()