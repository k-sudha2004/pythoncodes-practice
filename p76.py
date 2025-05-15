

if __name__ == '__main__':
    number = int(input().strip())
    if number % 2 != 0:
        print("Weird")
    elif 2 <= number <= 5:
        print("Not Weird")
    elif 6 <= number <= 20:
        print("Weird")
    elif number > 20:
        print("Not Weird")