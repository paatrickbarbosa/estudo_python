import os;

# tem que ter barra dupla
os.chdir('D:\\teste'); 


#strip() tira os espaços em branco

with open('james.txt') as jaf:
    data = jaf.readline();
james = data.strip().split(',');

with open('julie.txt') as juf:
    data = juf.readline();
julie = data.strip().split(',');

with open('mikey.txt') as mif:
    data = mif.readline();
mikey = data.strip().split(',');

with open('sarah.txt') as saf:
    data = saf.readline();
sarah = data.strip().split(',');

print("James: " ,james);
print("Julie: " ,julie);
print("Mikey: " ,mikey);
print("Sarah: " ,sarah);
