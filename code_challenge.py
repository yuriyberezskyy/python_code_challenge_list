# 1. Every Three Numbers
# Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.
# Write your function here


def every_three_nums(start):
    if(start <= 100):
        my_list = range(start, 101, 3)
        return list(my_list)
    else:
        list2 = []
        return list2


print(every_three_nums(91))


# 2.More Frequent Item
# Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
# Return either item1 or item2 depending on which item appears more often in lst.
# If the two items appear the same number of times, return item1.
# Write your function here
def more_frequent_item(lst, item1, item2):
    item1_count = lst.count(item1)
    item2_count = lst.count(item2)
    if item1_count > item2_count:
        return item1
    elif (item1_count < item2_count):
        return item2
    else:
        return item1


# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
