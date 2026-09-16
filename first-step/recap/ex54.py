print('== CHALLENGE 54 ==')

year_birth = []
for i in range(0,7):
    year = int(input('Insert you birth year: '))
    age = 2026 - year
    year_birth.append(age)

counter_larger = 0
counter_smaller = 0

for i in range(0,7):
    if year_birth[i] > 20:
        counter_larger += 1
    else:
        counter_smaller += 1

print('{} people have already reached the age of majority.'.format(counter_larger))
print('{} people have not reached the age of majority.'.format(counter_smaller))
