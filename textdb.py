def store(extracted):
    with open('data.txt', 'a') as file:
        file.write(f'{extracted}\n')


def read():
    try:
        with open('data.txt') as file:
            return file.read()
    except FileNotFoundError:
        return []
