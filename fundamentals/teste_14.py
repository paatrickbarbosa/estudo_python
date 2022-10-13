import os;

os.chdir('C:\\Users\\AutoLogon\\Desktop\\teste')
data = open('sketch.txt')
try:
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            print(role,end='')
            print('disse', end='')
            print(line_spoken, end='')
        except:
            pass

    data.close()

except:
    print('O arquivo de dado não esta na pasta')
