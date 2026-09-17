from importlib import import_module

task_module = [
    '00_distance',
    '01_circle',
    '02_operations',
    '03_favorite_movies',
    '04_my_family',
    '05_zoo',
    '06_songs_list',
    '07_secret',
    '08_garden',
    '09_shopping',
    '10_store',
]


def main():
    for task in task_module:
        print(f'Running {task}...')
        module = import_module(f'python_lab_01.{task}')
        module.run()
        print()


if __name__ == '__main__':
    main()