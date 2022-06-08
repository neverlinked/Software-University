username = str(input())
password = str(input())
data = str(input())

while data != password:
    data = str(input())

if data == password:
    print(f'Welcome {username}!')