#  تشفير كود بايثون على شكل نص داخل سكربت وفك تشفيره 
import marshal

code = "print('Hello World')"
en_code = marshal.dumps(compile(code,"<string>","exec"))
print(en_code)
#فك التشفير
de_code = marshal.loads(en_code)
exec(de_code)
