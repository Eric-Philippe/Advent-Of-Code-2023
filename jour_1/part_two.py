# Read the content of the file input.txt
input_file = open("input_1.txt", "r")
file_content = input_file.read()

# Cut the content of the file into a list of lines
lines = file_content.split("\n")

nums = [(1, '1', 'one'),
        (2, '2', 'two'),
        (3, '3', 'three'),
        (4, '4', 'four'),
        (5, '5', 'five'),
        (6, '6', 'six'),
        (7, '7', 'seven'),
        (8, '8', 'eight'),
        (9, '9', 'nine')]

total = 0
for line in lines:
    index = []
    for num in nums:
        try:
            i = line.index(num[1])
            index.append((num[0], i))

            i = line.rindex(num[1])
            index.append((num[0], i))

        except ValueError:
            pass

        try:
            i = line.index(num[2])
            index.append((num[0], i))

            i = line.rindex(num[2])
            index.append((num[0], i))
        except ValueError:
            pass

    index.sort(key=lambda t: t[1])

    total += index[0][0] * 10 + index[-1][0]

print(total)
