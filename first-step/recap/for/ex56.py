print('== CHALLENGE 56 ==')

name = []
age = []
sex = []

for i in range(0,4):
    print('\n== {}° Person =='.format(i+1))
    n = str(input('Insert a name: '))
    name.append(n)
    a = int(input('Insert a age: '))
    age.append(a)
    s = str(input('Insert a sex: ')).upper()
    sex.append(s)

media = sum(age)/4

older_age = age[0]
older_name = name[0]
counter_young_woman = 0

for i in range(0,4):
    if 'MALE' == sex[i]:
        if older_age < age[i]:
            older_age = age[i]
            older_name = name[i]
    elif 'FEMALE' == sex[i]:
        if age[i] < 21:
            counter_young_woman +=1

print('''
\nThe medium age of the group is : {:.1f} years old
The name of the older man is: {}
The quantity of women under the age of 21: {}
'''.format(media,older_name,counter_young_woman))
