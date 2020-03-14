# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phone_book = {}

for i in range(n):
    name_numbers = input().rstrip().split()
    phone_book[name_numbers[0]] = name_numbers[1]

    
while True:
    try:
        name = input()
        if name in phone_book:
            print(f'{name}={phone_book[name]}')
        else:
            print('Not found')
    except:
        break
    
