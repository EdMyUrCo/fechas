#FECHAS
def validar(d, m, a):
    flag = 0
    # Son aquellos que no son multiplos de 4
    if (a % 4 != 0) or (a % 4 == 0 and a % 100 == 0 and a % 400 != 0):
        flag = 0
    else:
        flag = 1

    if flag == 0 and m == 2 and (d >= 29):
        print("Fecha Incorrecta")
    elif (m in [4, 6, 9, 11]) and d > 30:
        print("Fecha Incorrecta")
    elif (m not in [2, 4, 6, 9, 11] and d > 31):
        print("Fecha Incorrecta")
    elif d < 1 or m > 12 or m < 1:
        print("Fecha Incorrecta")
    else:
        print("Fecha Correcta")


def main():
    n = int(input())

    for _ in range(n):
        d, m, a = list(map(int, input().split()))
        validar(d, m, a)


if __name__ == "__main__":
    main()
