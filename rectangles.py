arr = [[1, 1, 1],
       [1, 1, 1]]


def numRectangles():
    counter = 0
    pairs = []

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            for k in range(len(arr[i])):
                if arr[i][k] == arr[j][k] == 1:
                    pairs.append([[i, k], [j, k]])

    for i in range(len(pairs) - 1):
        for j in range(i + 1, len(pairs)):
            if pairs[i][0][0] == pairs[j][0][0] and pairs[i][1][0] == pairs[j][1][0]:
                counter += 1

    return counter


print(numRectangles())