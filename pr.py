def two(number):
    if number%1 == 0 and number%number == 0:
        return True

    return False

print(two(3))