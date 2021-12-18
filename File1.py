def read_data(name):
    data = []
    with open(name) as f:
        for line in f:
            for x in line.split():
                data.append(int(x))
    return data


def minimum(data):
    mini = int(data[0])
    for el in data:
        if el < mini:
            mini = el
    return no_problem(mini)


def maximum(data):
    maxi = int(data[0])
    for el in data:
        if el > maxi:
            maxi = el
    return no_problem(maxi)


def summa(data):
    s = 0
    for el in data:
        s += el
    return no_problem(s)


def product(data):
    s = 1
    for el in data:
        s *= el
    return no_problem(s)


def no_problem(el):
    if el >= 1000000:
        return str(el)
    else:
        return int(el)


mydata = read_data("file1.txt")
mydata2 = read_data("file2.txt")
