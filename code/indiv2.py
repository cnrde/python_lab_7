if __name__ == '__main__':
    a = list(map(int, input("введите элементы списка: ").split()))
    print(min(a, key=abs))
    print(sum(map(abs, a[a.index(0):])))
    print(a[1::2] + a[::2])