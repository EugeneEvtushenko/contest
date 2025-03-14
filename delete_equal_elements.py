"""Меняет повторяющиеся элементы списка на '_' и перемещает в конец списка."""


def delete_equal_elements(n, array):
    """Алгоритм замены."""
    i = 1
    while i < n and type(array[i]) is int:
        if array[i] == array[i-1]:
            array.remove(array[i])
            array.append('_')
        elif array[i] != array[i-1]:
            i += 1
    # array.append(n)
    return array


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        n = int(file_in.readline())
        array = file_in.readline().split(' ')
    # n = 10
    # array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = delete_equal_elements(n, array)
    print(result)
