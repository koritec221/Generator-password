import random

symbols='lksfnjkdsknljsnopljgnvmzbeu1234567890@:"{}?>!":><+_-#%WKLJNQOLPMN '
password = ''
for i in range(12):
    password += random.choice(symbols)
print (password)
