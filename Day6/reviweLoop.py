num_test_cases = int(input())

for i in range(num_test_cases):
    s = str(input())
    l = len(s)

    print(s[0:l:2], s[1:l:2])
