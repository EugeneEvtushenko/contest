"""Меняет повторяющиеся элементы списка на '_' и перемещает в конец списка."""


def delete_equal_elements(n, array):
    """Алгоритм замены."""
    i = 1
    while i < n and type(array[i]) is int:
        if array[i] == array[i-1]:
            array.remove(array[i])
            array.append('_')
        else:
            i += 1
    return array


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        a = int(file_in.readline())
        numbers = list(map(int, file_in.readline().split(' ')))
    # a = int(input())
    # numbers = list(map(int, input().split(' ')))
    result = delete_equal_elements(a, numbers)
    for i in range(a):
        print(f'{result[i]}', end=' ')
