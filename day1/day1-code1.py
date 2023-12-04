with open('day1-input1.txt') as f:
    totalSum = 0

    line = f.readline()
    while line:
        digits = []
        for letter in line:
            if (letter.isdigit()):
                digits.append(letter)
        if (len(digits) == 1):
            totalSum += int(digits[0] + digits[0])
        else:
            totalSum += int(digits[0] + digits[len(digits) - 1])
        line = f.readline()
    print('final sum: ', totalSum)

f.close()