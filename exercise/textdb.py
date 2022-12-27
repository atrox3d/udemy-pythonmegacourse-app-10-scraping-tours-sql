def headers():
    return 'date,temperature'


def store(date, temp, filename='temps.csv', headers=headers()):
    try:
        with open(filename) as test:
            test.readline()
    except FileNotFoundError:
        with open(filename, 'w') as head:
            head.write(f'{headers}\n')

    with open(filename, 'a') as out:
        line = f'{date},{temp}\n'
        out.write(line)
