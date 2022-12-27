def store(extracted):
    with open('data.txt', 'a') as file:
        file.write(f'{extracted}\n')


def read():
    with open('data.txt') as file:
        return file.read()
