def remove_odd_numbers(num_list):
    new_list=[]
    for n in num_list:
        if n%2==0:
            new_list.append(n)
    return new_list
my_list = [1,2,3,4,5,6,7,8,9,10]
cut_down_list= remove_odd_numbers(my_list)
print("Original list:",my_list)
print("Cut-down list:",cut_down_list)