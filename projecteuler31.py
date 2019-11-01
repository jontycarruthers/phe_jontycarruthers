# -*- coding: utf-8 -*-
"""
@author: Jonty
"""
   
""" Project Euler, problem 31: """

counter = 0
# loop over the number of 2ps
for j in range(101):
    # loop over the number of 5ps
    for k in range(1+(200-2*j)//5):
        # loop over the number of 10ps
        for l in range(1+(200-2*j-5*k)//10):
            # loop over the number of 20ps
            for m in range(1+(200-2*j-5*k-10*l)//20):
                # loop over the number of 50ps
                for n in range(1+(200-2*j-5*k-10*l-20*m)//50):
                    # loop over the number of £1s
                    for o in range(1+(200-2*j-5*k-10*l-20*m-50*n)//100):
                        counter += 1

# since we have not yet included the case where we just use a single £2 coin...
print("There are %s ways to obtain £2 using the coins provided." % (counter+1))
