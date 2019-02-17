def sumIntervals(length_of_the_list):
    global sum
    sum = 0
    list = []
    length = len(length_of_the_list)
    for x in range(0, length, 1):
        firstone = length_of_the_list[x][0]
        secondone = length_of_the_list[x][1]
        for y in range(firstone, secondone, 1):
            sum = sum + 1
            for z in range(0, len(list)):
                if y == list[z]:
                    sum = sum - 1
            list.append(y)

    print("the result is ", + sum)


sumIntervals([[1, 2], [6, 10], [11, 15]])
sumIntervals([[1, 4], [7, 10], [3, 5]])
sumIntervals([[1, 5], [10, 20], [1, 6], [16, 19],[5, 11]])




