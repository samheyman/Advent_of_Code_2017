result = 0
div = 0

text = open('input.txt','r')
content = text.readlines()

# First step
# for line in content:
#     numbers = line.split('\t')
#     max = int(numbers[0])
#     min = int(numbers[0])
#     for num in numbers:
#         if int(num) > max:
#             max = int(num)
#         if int(num) < min:
#             min = int(num)

#     result = result + (max-min)
#     print("{} numbers, maximum is {}, minimum is {}, difference is {}".format(len(numbers),max, min, max-min))


# Second step
for line in content:
    numbers = line.split('\t')
    for num in numbers:
        for i in range(0, len(numbers)) :
            print("dividing {} by {}".format(num, numbers[i]))
            if int(num) != int(numbers[i]) and int(num) % int(numbers[i]) == 0:
                div = int(num) / int(numbers[i])

    result = result + div
    print("{} numbers, division is {}".format(len(numbers), div))

print("Checksum is {}".format(result))

