missions_list = [
    {
        "name": "Mars 2020",
        "year": "2020",
        "direction": "Марс"
    },
    {
        "name": "Artemis I",
        "year": "2022",
        "direction": "Луна"
    },
    {
        "name": "Voyager 1",
        "year": "1977",
        "direction": "Дальний космос"
    }
]

def show_missions(missions):
    print('=== Каталог космических миссий ===\n')
    for number, mission in enumerate(missions, start=1):
        print(f'{number}. {mission["name"]}')
        print(f'Год запуска: {mission["year"]}')
        print(f'Направление: {mission["direction"]}\n')