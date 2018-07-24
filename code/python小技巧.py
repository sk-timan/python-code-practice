text='hello!\nmy name is Lisa.\nwelcome!'
file_1=open('test file.txt','w')
file_1.write(text)
file_1.close()



append_text='\nThis is an appended file'
file_2=open('test file.txt','a')
file_2.write(append_text)
file_2.close()



file_3=open('test file.txt','r')
content=file_3.readline()
print(content)
all_read=file_3.readlines()
print(all_read)



def fun1(x,y):
    return x+y

a=map(fun1,[1],[2])
print(a)
print(list(a))
b=list(map(fun1,[1,2],[3,4]))
print(b)




char_list=['a','b','c','c','d','d','d']

print(set(char_list))
print(type(set(char_list)))

sentence='Welcome Back to This Tutorial'
print(set(sentence))

unique_char=set(char_list)
unique_char.add('x')
print(unique_char)

#unique_char.remove('e')
#print(unique_char)

unique_char.discard('f')
print(unique_char)


set1=unique_char
set2={'a','e','i'}
print(set1.difference(set2))

print(set1.intersection(set2))


