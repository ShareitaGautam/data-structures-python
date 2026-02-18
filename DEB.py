from utility import (
    remove_number,
    remove_duplicatesfromsortedlist,
    remove_duplicatefromunsortedlist,
     sum_of_2_num_eqaul_target,
    sum_of_2_num_eqaul_target_1)

if __name__ == '__main__':
    # This block runs ONLY when you run this file directly (not when imported)

    print('Bootcamp')  # prints a simple message
    print('Hello World')  # prints another message

    # ------------------- LIST BASICS -------------------
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # create a list of numbers from 1 to 10

    print(numbers[-2])  # negative index: -1 is last element (10), -2 is second last (9)

    # ------------------- SLICING (SUBLIST) -------------------
    # slicing format: numbers[start : end]
    # start is INCLUDED, end is EXCLUDED
    # here: -4 means 4th element from the end, -1 means last element (but excluded)
    print(numbers[-4:-1])  # prints [7, 8, 9]

    # ------------------- ADDING AND UPDATING LIST -------------------
    numbers.append(11)  # append adds an element at the end of the list
    print(numbers)  # now list becomes [1..10, 11]

    numbers[9] = 100  # update by index: index 9 was 10, now it becomes 100
    print(numbers)  # list now has 100 instead of 10

    x = numbers[0]  # store the first element (index 0) into variable x
    print(x)  # prints 1

    # ------------------- LOOP THROUGH LIST -------------------
    # for-loop reads the list left to right and gives each element one by one
    for num in numbers:
        print(num)  # prints each element on a new line

    # ------------------- IF / ELIF / ELSE -------------------
    a = 50
    b = 50

    # compare a and b and print which condition is true
    if a > b:
        print("a>b")
    elif a < b:
        print("a<b")
    else:
        print("a==b")  # runs when both above conditions are false (means a == b)

    # ------------------- EVEN / ODD CHECK -------------------
    # % is modulus operator (remainder)
    # if a % 2 == 0, it means a is divisible by 2 => even
    if a % 2 == 0:
        print("a is even")
    else:
        print("a is odd")

    # ------------------- EMPTY LIST + APPEND -------------------
    names = []  # create an empty list
    print(names)  # prints []

    names.append("john")  # add one string to the list
    print(names)  # prints ['john']

    # ------------------- CREATE EVEN-NUMBERS LIST -------------------
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # reset numbers list
    even = []  # empty list to store even numbers

    # iterate through numbers
    for num in numbers:
        # check if the number is even
        if num % 2 == 0:
            # collect: add even number into even list
            even.append(num)

    print(even)  # prints [2, 4, 6, 8, 10]

    # ------------------- ITERATE WITH INDEX (range) -------------------
    # range(start, stop, step)
    # start = 0
    # stop = len(numbers) (not included)
    # step = 3 means jump by 3 positions each time
    #upper end is length of numbers
    for i in range(0, len(numbers), 3):
        print(numbers[i])  # prints elements at index 0, 3, 6, 9

    # ------------------- FIND MINIMUM NUMBER IN LIST -------------------
    numbers = [10, 2, 3, 4, 5, 8, 7, 6, 9, 1]  # new list
    min = numbers[0]  # assume first element is the smallest initially

    # check every number and update min when a smaller number is found
    for num in numbers:
        if num < min:
            min = num

    print(min)  # prints the smallest value (1)

    # ------------------- DICTIONARY (KEY-VALUE PAIRS) -------------------
    # dictionary stores values using unique keys (like HashMap)
    d = {}
    d["a"] = 5  # key "a" has value 5
    d["b"] = 6  # key "b" has value 6
    print(d)  # prints dictionary

    # update: fetch current value of "a" and add 1
    d["a"] = d["a"] + 1
    print(d)  # now "a" becomes 6 and replace the current value of a to 6

    d["c"] = 10  # create key "c"
    d["c"] = 11  # overwrite value of "c" (10 replaced by 11)
    print(d)

    # ------------------- CHECK IF A KEY EXISTS we use in operator -------------------
    x = "e" # define a variable
    if x in d:  # checks whether key "e" exists
        print(d[x])  # if exists, print its value
    else:
        print("key does not exist in dictionary")

    # check for key "a"
    if "a" in d:
        print(d["a"])  # prints value of "a"
    else:
        print("key does not exist in a dictionary")

    # ------------------- COUNT OCCURRENCES OF A TARGET -------------------
    numbers = [10, 2, 3, 4, 5, 8, 7, 6, 9, 1, 10, 3, 2, 1, 2]
    target = 1  # we want to count how many times 1 appears
    count = 0  #counter

    for num in numbers:
        if num == target:  # if current element matches target
            count += 1  # increase count by 1

    print(count)  # prints total occurrences of target (1)

    # ------------------- COUNT OCCURRENCES OF ALL NUMBERS (FREQUENCY MAP) -------------------
    numbers = [1, 2, 2, 3]
    d = {}  # dictionary to store: number -> count

    for num in numbers:
        if num in d:  # if number already seen, increase its count
            d[num] = d[num] + 1
        else:  # first time seeing this number, start count at 1
            d[num] = 1

    print(d)  # prints frequency dictionary (example: {1:1, 2:2, 3:1}), entry in a dictionary

    # ------------------- NUMBER WITH MAX OCCURRENCES (MOST FREQUENT NUMBER) -------------------
    numbers = [10, 20, 20, 30]

    d = {}  # dictionary to store frequency: number -> how many times it appears

    # Build the frequency dictionary
    for num in numbers:
        if num in d:  # if num already exists as a key in dictionary
            d[num] = d[num] + 1  # increase its count by 1
        else:  # first time seeing this num
            d[num] = 1  # start count at 1

    print(d)  # example output: {10: 1, 20: 2, 30: 1}

    freq = 0  # freq keeps track of the highest frequency seen so far
    max = 0  # max keeps track of the number that has the highest frequency

    # Find the key (number) with the maximum count (frequency)
    for key in d.keys():  # loop over all unique numbers (keys) in dictionary
        value = d[key]  # value is the frequency/count of that number
        if value > freq:  # if this number's count is bigger than current max frequency
            max = key  # store this number as the current answer
            freq = value  # update highest frequency

    print(max)  # prints the number that appears the most times (here: 20)

    # ------------------- WORD COUNT (MOST FREQUENT WORD) -------------------
    line = "hello world hi world hi nepal"

    # split() breaks the sentence into a list of words using space as separator
    words = line.split(' ')
    print(words)  # ['hello', 'world', 'hi', 'world', 'hi', 'nepal']

    word_counts = {}  # dictionary: word -> count

    # Count frequency of each word
    for word in words:
        if word in word_counts:  # if word already seen
            word_counts[word] = word_counts[word] + 1
        else:  # first time seeing word
            word_counts[word] = 1

    print(word_counts)  # example: {'hello':1, 'world':2, 'hi':2, 'nepal':1}

    freq = 0  # highest word frequency seen so far
    word = 0  # will store the word that has the highest frequency

    # Find the word with maximum frequency
    for key in word_counts.keys():  # loop over words (keys)
        count = word_counts[key]  # count of that word
        if count > freq:  # if this word is more frequent than current best
            word = key  # store the word
            freq = count  # store its frequency

    print(word)  # prints most frequent word (could be 'world' or 'hi' since both appear 2 times)

    # ------------------- REMOVE DUPLICATES USING SET (QUICK METHOD) -------------------
    # NOTE: set removes duplicates BUT it does NOT guarantee order
    list = [1, 2, 2, 3, 4, 4, 5]
    s = set(list)  # converts list to set => duplicates removed automatically
    print(s)  # output looks like {1, 2, 3, 4, 5} (order may vary)

    # ------------------- REMOVE DUPLICATES (KEEP ORDER) USING SET + OUTPUT LIST -------------------
    list = [1, 2, 2, 3, 4, 4, 5]

    output = []  # final result list without duplicates (keeps order)
    visited = set()  # visited set: remembers what numbers we have already added

    # loop through each number in the list
    for num in list:
        if num not in visited:  # if we have NOT seen this number before
            visited.add(num)  # mark it as seen
            output.append(num)  # add it to output list

    print(output)  # [1, 2, 3, 4, 5]

    # ------------------- REMOVE DUPLICATES FROM SORTED INPUT (NO SET NEEDED) -------------------
    # Idea: in a sorted list, duplicates are next to each other
    output = []
    list = [1, 2, 3, 2, 5, 4, 6, 4]  # NOTE: your comment says "sorted", but this list is NOT sorted

    prev = list[0]  # store first value as "previous"
    output.append(prev)  # put first value into output

    # compare each number with prev; only add when it changes
    for num in list:
        if num != prev:  # means it's a new/different number than previous
            output.append(num)
            prev = num  # update prev to current number

    print(output)  # removes only consecutive duplicates (works correctly only when input is sorted)

    # ------------------- REMOVE SPECIFIC VALUE FROM LIST (EX: REMOVE ALL 3s) -------------------
    list = [1, 2, 3, 4, 5, 3]
    value = 3

    output = []  # store elements that are NOT equal to value

    for num in list:
        if num != value:  # keep only numbers that are not 3
            output.append(num)

    print(output)  # [1, 2, 4, 5]

    # ------------------- USING A FUNCTION (METHOD) FOR REUSABILITY -------------------
    # Instead of writing same logic again and again, we create a function like remove_number(list, value)
    # Then we can call it for different inputs.

    value = 3
    list = [1, 2, 3, 4, 5, 3]

    # remove_number() should be a function you define somewhere above (not shown here)
    # It should return a list after removing 'value' from 'list'
    output = remove_number(list, value)
    print(output)

    value = 4
    list = [1, 2, 3, 4, 5, 3]
    output = remove_number(list, value)
    print(output)

    # ------------------- REMOVE DUPLICATES FROM SORTED LIST USING FUNCTION -------------------
    list = [1, 2, 3, 2, 5, 4, 6, 4]
    output = remove_duplicatesfromsortedlist(list)  # function should return duplicates removed (works best if input sorted)
    print(output)

    list = [1, 2, 3, 4, 5, 5]
    output = remove_duplicatesfromsortedlist(list)
    print(output)

    # ------------------- REMOVE DUPLICATES FROM UNSORTED LIST USING FUNCTION -------------------
    # remove_duplicatefromunsortedlist() should handle unsorted input using set/visited technique
    list = [1, 2, 2, 3, 4, 4, 5]
    output = remove_duplicatefromunsortedlist(list)
    print(output)

    # ------------------- TWO SUM PROBLEM (FIND 2 NUMBERS WHOSE SUM = TARGET) -------------------
    list = [1, 2, 3, 4, 5]
    sum = 6

    # These functions should return something like a pair (1,5) or (2,4) depending on implementation
    output = sum_of_2_num_eqaul_target(list, sum)
    print(output)

    output = sum_of_2_num_eqaul_target_1(list, sum)
    print(output)

    # ------------------- TUPLE BASICS -------------------
    # tuple is like a list but IMMUTABLE (cannot be changed after creation)
    t = (1, 2, 3, 4)
    print(t)

    # Notes (your comments):
    # - list may allocate extra memory behind the scenes to allow growth
    # - tuple is fixed-size, so it is more memory efficient for fixed data


    # ------------------- STRING + VOWEL COUNT (METHOD 1) -------------------
    s = "Hello World"

    # Count vowels by checking each character one by one
    count = 0
    for ch in s:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count = count + 1

    print(count)  # counts only lowercase vowels; 'Hello World' has 'e' and 'o' (lowercase check may miss uppercase)

    # ------------------- STRING + VOWEL COUNT (METHOD 2 - USING SET FOR FAST CHECK) -------------------
    s = "Hello World"

    count = 0
    vowels = set('aeiou')  # set of vowels for quick membership checking

    for ch in s:
        if ch in vowels:  # checks if ch is one of a,e,i,o,u
            count = count + 1

    print(count)  # same result logic, but cleaner and faster membership check
