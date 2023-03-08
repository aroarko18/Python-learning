# List functions---------------
# # append()
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list1.append(10)
# print(list1)

# # count()
# list2 = [1, 2, 3, 4, 5, 6, 5, 6, 5, 10]
# count_item = list2.count(5)
# print(count_item)

# # index()
# list3 = [23, 32, 33, 54, 23]
# position = list3.index(23)
# print(position)

# # insert()
# list4 = [1, 2, 3, 4, 5, 6]
# list4.insert(0, 0)
# print(list4)

# # pop()-------delete element by default last but pop(index) remove specific position element 
# list5 = [1, 2, 3, 4, 5, 6]
# list5.pop()
# print(list5)

# # remove() -- remove(object) - it only removes the object that has been instructed to be removed
# list6 = [12, 23, 32, 43, 34, 54]
# list6.remove(43)
# print(list6)

# # reverse()
# list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list7.reverse()
# print(list7)

# # sort()
# list8 = [1, 3, 1, 2, 3, 4, 5, 6, 65, 77]
# list8.sort()
# print(list8)

# # extend()
# list9 = [1, 2, 3, 4, 5]
# list10 = [6,7, 8, 9, 10]
# list9.extend(list10)
# print(list9)

# # copy()
# a = [1, 2, 3, 4]
# b = a.copy()
# print(b)

# ---------------- Basic Tuple Functions--------------------

# # len()
# a = (1, 2, 3, 4, 5, 6, 7)
# print(len(a))

# # Tuple concatenation
# t1 = (1, 2, 3, 4)
# t2 = (5, 6, 7, 8, 9)
# t3 = t1 + t2
# print(t3)

# # Tuple repeatation
# t = ('Arko...')
# result = t * 3
# print(result)

# # Membership
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# result = 5 in t
# print(result) 

# # Tuple iteration
# t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for i in t1:
#     print(i, end="_")

# # Comparision
# tup1 = (0, 1, 2, 3)
# tup2 = (1, 2, 2, 3)
# print(tup1 > tup2)

# # Maximum
# t1 = (1, 3, 4, 55, 65, 64, 66, 99)
# print(max(t1))

# # Minimum
# t1 = (0, 1, -6, 4, 6, 22)
# print(min(t1))

# # Conversion to tuple
# name = 'Arko'
# print(tuple(name))

# num_list = [1, 2, 3, 4, 5]
# print(tuple(num_list))
