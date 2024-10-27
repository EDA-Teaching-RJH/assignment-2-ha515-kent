### Part Three -- your code goes here. 

num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
def main():

    
    num_list.sort()
    
    num_list.extend([7, 8])

    while 1 in num_list:
        num_list.remove(1)

    print (num_list)

main()