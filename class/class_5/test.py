import re

html='''%abc%%def%python(ghi)'''
print(re.subn(r'%[\s\S]*%','&',html))

