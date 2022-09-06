#  URL http://localhost:5000/data1?id=666&data=123456
from linecache import getline

aaa = []
z = ""
with open("data.txt", 'r') as f:
    a = f.read().split('\n')
    myString = ','.join(a)
    print(myString)
