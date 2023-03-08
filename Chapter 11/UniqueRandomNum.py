

import random

retries = 0

def unique_random_ints(how_many, max_num, seed):
    global retries
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""
    random.seed(seed)
    num_list = []
    for number in range(0, how_many):
        new_num = random.randint(0, max_num)
        if new_num in num_list:
            retries += 1
        else:
            num_list.append(new_num)
        
    print(num_list)
    print(retries)
    # Type your code here. #


if __name__ == '__main__':
    seed = int(input("seed:"))
    how_many = int(input("how many:"))
    max_num = int(input("max number:"))


    unique_random_ints(how_many, max_num, seed)
    # Type your code here. #