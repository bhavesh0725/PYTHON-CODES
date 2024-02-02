


print("********************SHALLOW COPY************************")

original=[1,2,3,4,5]
shallowCopy= original
shallowCopy[0]=999

print(original)
print(shallowCopy)


print(id(original))
print(id(shallowCopy))





print("********************DEEP COPY************************")

deepCopy= original.copy()
deepCopy[4]=999

print(original)
print(deepCopy)


print(id(original))
print(id(deepCopy))



# output:
# ********************SHALLOW COPY************************
# [999, 2, 3, 4, 5]
# [999, 2, 3, 4, 5]
# 139704976706112
# 139704976706112
# ********************DEEP COPY************************
# [999, 2, 3, 4, 5]
# [999, 2, 3, 4, 999]
# 139704976706112
# 139704977501440
