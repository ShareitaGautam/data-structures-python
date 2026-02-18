
#              PYTHON PRACTICE FUNCTIONS

# 1) REMOVE A SPECIFIC NUMBER FROM A LIST

def remove_number(lst, value):
    """
    Removes ALL occurrences of 'value' from the list.
    Creates and returns a NEW list (original list is unchanged).
    """
    output = []   # new list to store result

    for num in lst:        # iterate over each element
        if num != value:   # keep only numbers NOT equal to value
            output.append(num)

    return output



# 2) REMOVE DUPLICATES FROM SORTED LIST

def remove_duplicatesfromsortedlist(lst):
    """
    Works ONLY when list is SORTED.
    Idea: duplicates appear next to each other.
    Compare each number with previous one.
    """
    output = []

    # if list is empty, return empty list (safety check)
    if len(lst) == 0:
        return output

    prev = lst[0]          # take first element
    output.append(prev)    # first element is always unique

    for num in lst:
        if num != prev:    # new number found
            output.append(num)
            prev = num     # update previous number

    return output



# 3) REMOVE DUPLICATES FROM UNSORTED LIST

def remove_duplicatefromunsortedlist(lst):
    """
    Works for UNSORTED list.
    Uses a set to remember already-seen numbers.
    Keeps the order of first appearance.
    """
    output = []
    seen = set()    # memory of visited numbers

    for num in lst:
        if num not in seen:   # first time seeing this number
            seen.add(num)
            output.append(num)

    return output



# 4) TWO SUM - BRUTE FORCE (SLOW)

def sum_of_2_num_eqaul_target(lst, target):
    """
    Returns True if ANY two DIFFERENT positions
    in the list add up to target.
    Tries all pairs -> O(n^2)
    """

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:   # avoid using same element twice
                if lst[i] + lst[j] == target:
                    return True

    return False



# 5) TWO SUM - OPTIMAL (FAST)

def sum_of_2_num_eqaul_target_1(lst, target):
    """
    Optimal approach using a set.
    For each number, check if its needed partner
    was seen before.
    Time: O(n)
    """

    seen = set()

    for num in lst:
        difference = target - num

        if difference in seen:
            return True   # pair found

        seen.add(num)     # remember this number

    return False



# 6) COLLECT ALL PAIRS THAT SUM TO TARGET (YOUR TASK)

def collect_all_pairs(lst, target):
    """
    Returns a list of all pairs whose sum = target.
    Example output: [(1,5), (2,4)]
    """

    seen = set()
    pairs = []

    for num in lst:
        difference = target - num

        if difference in seen:
            pairs.append((difference, num))

        seen.add(num)

    return pairs


#                EXAMPLE TESTS (MAIN)

if __name__ == "__main__":

    print("---- remove_number ----")
    print(remove_number([1,2,3,4,3], 3))

    print("---- remove_duplicatesfromsortedlist ----")
    print(remove_duplicatesfromsortedlist([1,2,2,3,4,4,5]))

    print("---- remove_duplicatefromunsortedlist ----")
    print(remove_duplicatefromunsortedlist([1,2,1,3,2,4]))

    print("---- two sum brute ----")
    print(sum_of_2_num_eqaul_target([1,2,3,4,5], 6))

    print("---- two sum optimal ----")
    print(sum_of_2_num_eqaul_target_1([1,2,3,4,5], 6))

    print("---- collect all pairs ----")
    print(collect_all_pairs([1,2,3,4,5], 6))
