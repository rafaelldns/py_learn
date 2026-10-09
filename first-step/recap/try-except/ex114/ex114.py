import requests 

print('{:^55}'.format('CHALLENGE 114')+'\n'+55*'=')

url = 'https://www.pudim.com.br'

print('Testing the site pudim.com.br')

try:
    res = requests.get(url)
except requests.ConnectionError:
    print('\033[0;31mERROR: The site it is inacessible or does not exist!\033[m')
else:
    print('The is working and open in this PC!')
