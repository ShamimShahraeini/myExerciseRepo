import re

birthday = input()

res = re.findall('..', birthday)

print("saal:" + str(res[0]))
print("maah:" + str(res[1]))