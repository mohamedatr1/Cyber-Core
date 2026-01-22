# ـحليل الكود والحصول على الكود الاصلي
import marshal
import dis
with open("new_script.pyc","rb") as file:
    file.seek(16)
    de_code = marshal.loads(file.read())
    # exec(de_code)
code_str = dis.code_info(de_code,)
print(code_str)