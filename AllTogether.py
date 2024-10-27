### Part Four -- your code goes here. 
import random
random_num_list = []
new_list = 0

def main(random_num_list, new_list):

    for i in range(10):
        num_list = random.randint(1, 100)
        random_num_list.append(num_list)

    print(*random_num_list, sep=", ")
    print()

    while new_list < len(random_num_list):
        if random_num_list[new_list] % 2 == 0:
          random_num_list.pop(new_list)  
        else:
            new_list = new_list + 1
    
        print(random_num_list)

main(random_num_list, new_list)