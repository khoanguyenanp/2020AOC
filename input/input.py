def transform(value):
    res = value.replace("\n", '')
    return int(res)

def getDay1Input():
    with open('./input/day1_input.txt', 'r') as f:
        lines = f.readlines()
    return list(map(transform, lines))