DATAFILE = 'data.txt'


def store(extracted):
    with open(DATAFILE, 'a') as file:
        file.write(f'{extracted}\n')


def read():
    try:
        with open(DATAFILE) as file:
            # rows = [tuple(map(str.strip, line.split(','))) for line in file.read().split('\n') if line ]
            content = file.read()
            lines = [line for line in content.split('\n') if line]
            rows = [line.split(',') for line in lines]
            rows = [tuple(map(str.strip, fields)) for fields in rows]
            return rows
    except FileNotFoundError:
        return []
