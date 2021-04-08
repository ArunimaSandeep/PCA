# import re
# median_m= "0.100"
#
# print(float(median_m))


# pattern=re.compile(r'\d.\d\d')
#
# matches=pattern.finditer(median_m)
#
# for match in matches:
#     print(match)

a=[3.145, 3.155, 3.678960]


# for i in a:
#     m=round(i,2)
#     print(m)
#     b.append(m)
# print(b)

for i in range(0,len(a)):
    a[i]=str(a[i])[::-1].find('.')

print(a)


max = a[0]
for i in range(1, len(a)):
    if a[i] > max:
        max = a[i]
print(max)

res = 1/10**(max)
print(res)
