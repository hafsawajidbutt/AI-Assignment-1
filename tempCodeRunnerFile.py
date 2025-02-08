import numpy as np
my_list = [1, 2, 3, 4, 5]
l2 = np.array(my_list)
if(my_list == l2.all()):
    print("Equal")