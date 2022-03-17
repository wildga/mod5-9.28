address = int(input("Input address >>> "))

pageNum = address // 4096
offsetNum = address % 4096

print("=============================")
print("The address {} contains:".format(address))
print("page number =", pageNum)
print("offset =", offsetNum)