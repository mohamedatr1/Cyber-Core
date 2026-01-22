# فك تشفير ملف مارشال

import marshal


with open("new.bin", "rb") as file:
    
    de_code = marshal.loads(file.read())

with open("new2.py","a") as file:
    file.write(str(de_code))    