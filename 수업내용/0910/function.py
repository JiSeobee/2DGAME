def add(a,b):
    sum=a+b
    return sum

result = add(100,10)
print(result)






def sum(a,b):
    return a+b

print(sum('Daehyun', 'Lee'))






def sum_and_mul(a,b):
    return a+b,a*b

a=sum_and_mul(3,4)
print(a)

sum,mul=sum_and_mul(3,4)
print('sum=%d'%sum)
print('mul=%d'%mul)

