# question 1
def hello_greeting(name):
    print(f"Hello {name}!")


hello_greeting("Allan")

# question 2


def first_odds():
    for number in range(1, 101, 2):
        print(number)


first_odds()

# question 3
numbers = [3, 1, 2, 5, 4]


def max_num_in_list(a_list):
    a_list.sort()
    max_num = a_list[-1]
    return max_num


print(max_num_in_list(numbers))


# question 4

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        leap_year = True
    elif a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0:
        leap_year = True
    else:
        leap_year = False
    return leap_year


print(is_leap_year(2000))

# question 5
list1 = [1, 2, 3]
list2 = [2, 3, 1]


def is_consecutive(a_list2):
    return a_list2 == list(range(min(a_list2), max(a_list2) + 1))


print(is_consecutive(list1))
print(is_consecutive(list2))
