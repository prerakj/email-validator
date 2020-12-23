import string

x=input('enter your mail id')
b= len(x)
z=x.find('@')
p=x.count('@')
q=x[0:z]
t=x.find('.com')
if(p==1 and q.isalnum() and x[z+1:t-1].isalpha() and x[-4:]=='.com'):
    print(x)
else:
    print('enter correct mail')