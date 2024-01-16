if __name__ == '__main__':
    a = list(map(int, input("введите элементы списка: ").split()))
    for i, item in enumerate(a):
        if item == 0:
            print(f"({i}, {item})")