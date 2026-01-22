# تشفير ملف كامل وحفظه في ملف جديد


import marshal


with open('script.py','r',encoding="utf-8") as file:
    code = file.read()

en_code = marshal.dumps(compile(code,"<string>","exec"))

with open("new.bin","wb") as file:
    file.write(en_code)