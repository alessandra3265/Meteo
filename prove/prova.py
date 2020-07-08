s = "2020/0019_2020_PREC.htm"
result = s.split('/')
print(result)
res = result[1].split('_', 1)
print(res)

s1 = "Molini (Laghi) (191)"
result = s1.split(' (')
print(result[0])