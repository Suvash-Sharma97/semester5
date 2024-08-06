#list comprehension


ls1 = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]

sq = [x*x for x in ls1]

sq1 = list(map(lambda x:x*x, ls1))

print(sq)

print(sq1)


string = 'abcd'
nums = '1234'

pair = [(x, y) for x in string  for y in range(4)]
print(pair)