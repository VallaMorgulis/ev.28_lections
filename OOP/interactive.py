# a = 4682
# b = [int(i) for i in str(a)]
# c = b.copy()
# c.pop(b.index(max(b)))
# c.insert(b.index(max(b)), min(b))
# c.pop(b.index(min(b)))
# c.insert(b.index(min(b)), max(b))
# res = int(''.join([str(i) for i in c]))
# print(res)

      #age   #orbit        
day = (20 / (225 / 365))*365 # дни Венера
hours = (20 / (12 / 365))*365  # Юпитер
hours = round(20 * 365 // 12 * 365 * 24)

print(hours)
