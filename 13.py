import matplotlib.pyplot as plt
import math

a = int(input('ezt a sort ird ki: '))
b = int(input('masodik szam: '))


def pascal_triangle(n,m):
    line = [1]
    for k in range(max(n, 0)):
        line.append(line[k] * (n - k) / (k + 1))
    line_two = [1]
    for l in range(max(m, 0)):
        line_two.append(line_two[l] * (m - l) / (l + 1))
    list = []
    z = 0
    for i in range(len(line_two)):
        list.append(z)
    y=line_two
    x=list
    plt.title('sor')
    plt.scatter([line_two],[list], color='green')
    plt.show()
    return line



print(pascal_triangle(a, b))

