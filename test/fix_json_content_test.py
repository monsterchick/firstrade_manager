with open('test.json','w') as f:
    f.write('this is test)')

with open('test.json','r') as f:
    old_content = f.read()

print(old_content)

# 删除最后一个字符
old_content = old_content[:-1]
print(old_content)

with open('test.json','w')as f:
    f.write(old_content)