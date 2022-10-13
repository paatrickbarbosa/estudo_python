import os;

os.getcwd();
os.chdir('C:\\Users\\AutoLogon\\Desktop\\teste');

data = open('sketch.txt');
print(data.readline(),end= '');
print(data.readline(),end='');

print('-----------///--------------');

data.seek(0);

for cada_linha in data:
    print(cada_linha, end='');

print('-----------///--------------');

data = open('sketch.txt');
for each_line  in data:
    if not each_line.find(':') == -1:
        (role, line_spoken) = cada_linha.split(':',1)
        print(role,end='')
        print('disse', end='')
        print(line_spoken, end='')


data.close();

