str1 = 'apple-banana-orange'
print(str1.split('-'))


print(str1.split('-')[0])
print(str1.split('-')[1])
print(str1.split('-')[2])

list1 = ['apple', 'banana', 'orange']
print('$'.join(list1))

str = 'my jcd ji mo ji'
print(str.find('ji'))
print(str.replace('ji','mooo',1))

str = input('请输入名称:')
print(str[str.find('.')+1:])
