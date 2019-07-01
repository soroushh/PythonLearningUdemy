the_list = [1,2,3,4,5]

print([ item for item in the_list if item %2 == 0])

print(list(filter(lambda x: x % 2 ==0, the_list)))

def is_even(x):
    return(x%2 == 0)

print(list(filter(is_even, the_list)))
