# # enumerate function
# # ---- etar kaj hocche list er item r sathe sathe index o dibe.
# girlFriend = ['Chowa', 'Sanam', 'Naiyara', 'Boldy', 'CutePoison']
# for index, i in enumerate(girlFriend):
#     print(f"{i} is in the index of {index}")

# # iter() function
# # eta hoise emn ekta function jeta next element re select kore. loop er moto. but loop na. 
# # eidare access er jonno next() de kora lage example
# list = [1, 2, 3, 4, 5, 6]
# # ekhon list re iter e dukai
# it = iter(list)
# for i in range(len(list)):
#     print(f"{i} is the index. And iter list value{next(it)}")

# map() eta kore hocche amader pura list r sob element re eksathe nei ar function e apply kore
# tobe show koranur jonno eino list(map(function, num_list))
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def isBigger(x):
#     if x>5:
#         return "{} number is bigger than 5".format(x)
    
# result = list(map(isBigger, num_list))
# print(result)

# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# c = zip(a, b)
# print(list(c))
# # for x in c:
# #     print(x)

# for i in[1, 2, 3, 4, 5, 6][1::2]:
#     print(i)

# n = int(input("n"))
# total = 0
# for i in range(n):
#     total += 1/(i+1)
# print(total)    


# list er sob kichu
# extend er kaj 2 ta re ek sathe ek list banani
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
print(thislist)

# extend tuple reu add kore
thislist2 = ["lodirfut", "kuttarbaccha", "madarchud"]
this_tuple = ("kankirpula", "sourerbaccha", "salarput")

thislist2.extend(this_tuple)
print(thislist2)