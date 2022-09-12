""" bytearray """
# a=b'hi'
# print(type(a))
# print(bytearray(a))

# y=b"python"
# # print(y,type(y))
# print(list(y))
# print(tuple(y))
# print(set(y))

# y=b"python"
# for i in y:
#     print(i)

# print(ord('S'))
# print(chr(90))

# y=b"python"
# print(type(y))
# y[0]=95  # no modifications

# v=b'[1,2,3]'
# print(list(v))

# print(ord('['))
# print(ord(']'))
# print(ord(','))

m=bytearray(b"python")
print(m,type(m))
m[0]=90
print(m)
m[0]=80
print(m)