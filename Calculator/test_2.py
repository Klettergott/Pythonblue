import re
txt = 'The rain in Spain dog dog cat'
x = re.findall('dog', txt)
z = re.findall('cat', txt)
txt = 'The rain in Spain'
x = re.search('\s', txt)
print(x.start())