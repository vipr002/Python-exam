
# question 5

# Assignment says "Assume that the user does not enter invalid inputs"
# Therefor, the solution does not handle invalid input from the user

def main():
    zeroes = []
    positives = []
    negatives = []
    running = True
    while running:
        temp_int = input("Enter an integer (blank to quit): ")
        if len(temp_int) != 0:
            temp_int = int(temp_int)
            if temp_int == 0:
                zeroes.append(temp_int)
            elif temp_int > 0:
                positives.append(temp_int)
            elif temp_int < 0:
                negatives.append(temp_int)
            else:
                print("Invalid input")
        else:
            running = False

    print(*positives, *zeroes, *negatives, sep=" ")


main()
