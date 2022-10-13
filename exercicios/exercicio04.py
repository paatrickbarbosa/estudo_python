import os;

os.chdir('D:\\teste');

#funcao pra passar os caracteres especiais para .
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
         return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins + '.' + secs);
#fim da função

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

james = get_coach_data('james.txt');
julie = get_coach_data('julie.txt');
mikey = get_coach_data('mikey.txt');
sarah = get_coach_data('sarah.txt');


print(sorted(set([sanitize(t) for t in james]))[0:3]);
print(sorted(set([sanitize(t) for t in julie]))[0:3]);
print(sorted(set([sanitize(t) for t in mikey]))[0:3]);
print(sorted(set([sanitize(t) for t in sarah]))[0:3]);


#essa de cima é a mesma coisa aque embaixo 
#porem está usando uma função para abrir os arquivos
#------------

# #funcao pra passar os caracteres especiais para .
# def sanitize(time_string):
#     if '-' in time_string:
#         splitter = '-'
#     elif ':' in time_string:
#         splitter = ':'
#     else:
#          return(time_string)
#     (mins,secs) = time_string.split(splitter)
#     return(mins + '.' + secs);
# #fim da função

# #caminho dos arquivos
 #os.chdir('D:\\teste'); 


# with open('james.txt') as jaf:
#     data = jaf.readline();
# james = data.strip().split(',');

# with open('julie.txt') as juf:
#     data = juf.readline();
# julie = data.strip().split(',');

# with open('mikey.txt') as mif:
#     data = mif.readline();
# mikey = data.strip().split(',');

# with open('sarah.txt') as saf:
#     data = saf.readline();
# sarah = data.strip().split(',');


# clean_james = [];
# clean_julie = [];
# clean_mikey = [];
# clean_sarah = [];

# for each_t in james:
#     clean_james.append(sanitize(each_t));

# for each_t in julie:
#     clean_julie.append(sanitize(each_t));

# for each_t in mikey:
#     clean_mikey.append(sanitize(each_t));

# for each_t in sarah:
#     clean_sarah.append(sanitize(each_t));

# print(sorted(clean_james))
# print(sorted(clean_julie));
# print(sorted(clean_mikey));
# print(sorted(clean_sarah));
