import math


# searches for specified item in chosen collection
def binary_search(item, collection):
    lower_bound = 0
    upper_bound = len(collection) - 1

    while lower_bound <= upper_bound:

        mid = math.floor((lower_bound + upper_bound) / 2)

        if collection[mid] == item:
            return mid

        if collection[mid] < item:
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1

    # if item not found
    return -1


alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
letter = 'z'  # user-specified letter

# find index of the letter in alphabet
index = binary_search(letter.upper(), alphabet)

if index == -1:
    print(f"\"{letter}\" letter not found")
else:
    index += 1
    last_digit = index % 10

    print(f"\"{letter}\" is the {index}",
          "th" if 3 < index % 100 < 21
          else "st" if last_digit == 1
          else "nd" if last_digit == 2
          else "rd" if last_digit == 3
          else "th",
          " letter in english alphabet",
          sep='')
