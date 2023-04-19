import pandas as pd
import pyautogui
import time
from selenium import webdriver

mozilla = webdriver.Firefox()

tabela = pd.read_excel(r'C:\Users\p.barbosa\Desktop\excel\impressora\impressoras.xlsx')
arquivo = open("impressoras.txt", "w")
arquivo.write('Impressoras com menos de 10% de toner \n\n')

# funcao para fazer a compração se é menor que 10%
def condicao(status):
    if( status < 10):
        status = '{}' .format(status)
        arquivo.write('Impressora: {} \nIP: {} \nStatus: Toner Preto {}%\nN.Serie: {} \n---------------\n' .format(nome, ip, status, ns))
    # else:
    #     print('Impressora: {} \nIP: {} \nStatus: Toner Preto {}% \n---------------\n' .format(nome, ip, status))
    return status

for index, row in tabela.iterrows():

    nome = str(row['NOME'])
    ip = str(row['IPS'])
    ns = str(row['NUMERO_SERIE'])

    #Impressoras coloridas 
    if(ip == '192.168.1.39' or ip == '192.168.1.20'):
        mozilla.get('http://{}/cgi-bin/dynamic/printer/PrinterStatus.html'. format(ip))
        time.sleep(1)
        pyautogui.press('enter')
        status = {}

        for i in range(1,5):
            cor = mozilla.find_element('xpath', '/html/body/table[3]/tbody/tr/td[{}]/table/tbody/tr[1]/td/b'.format(i)).text
            percent_cor = mozilla.find_element('xpath', '/html/body/table[3]/tbody/tr/td[{}]/table/tbody/tr[2]/td/table/tbody/tr/td'.format(i)).get_property('title')
            percent_cor = percent_cor.replace("%", "").strip()  
            status[cor] = percent_cor[0:3]
            
        # print(status)   
        for key in status:
            if not status[key]:
                status[key] = 0

        for key, value in status.items(): 
            if int(value) < 10:
                arquivo.write('Impressora: {} \nIP: {} \nStatus: {} {}% \nN. Serie: {} \n---------------\n' .format(nome, ip, key, value, ns))


    # impressoras P&B
    else:    
        mozilla.get('http://{}/cgi-bin/dynamic/printer/PrinterStatus.html'.format(ip))
        time.sleep(1)
        pyautogui.press('enter')
        percentual = mozilla.find_element('xpath', '/html/body/table[1]/tbody/tr[3]/td/b').text

        status = percentual.replace("%", "").replace("~", "").strip()
        status = status[-3:].strip()
        if status == 'eto':
            status = 00

            condicao(status)
        
        else:
            status = int(status[-3:].strip())
            condicao(status)
arquivo.close()

mozilla.close()

print('----------FIM----------')