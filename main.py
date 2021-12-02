import random

str_abc = 'qwertyuioplkjhgfdsazxcvbnm'
set_symbols = list(str_abc)
random.shuffle(set_symbols)
name = ''.join(set_symbols)
index = random.choice(range(3, 20))
email_item = ['@gmail.com', '@ukr.net', '@mail.com']
new_email = name[:index] + random.choice(email_item)
print(new_email)
