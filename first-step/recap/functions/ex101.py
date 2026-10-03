def vote(n):
    age = n
    if age >= 16 :
        if age < 18 or age > 69 :
            return 'OPTIONAL'
        else:
            return 'MANDATORY'
    else:
        return 'DENIED'
        


print('{:^55}'.format('CHALLENGE 101')+'\n'+55*'=')
year = int(input('Enter your birth year: '))
year = 2026 - year
vote(year)
print(f'With {year} years, vote is: {vote(year)}')
