#importações das libs
import pyautogui
import time 


# pressiona botao do windows
pyautogui.press('win')
#tempo de espera
time.sleep(2)
#vai até essas coordenadas e da um click
pyautogui.click(394,466)
#tempo de espera
time.sleep(5)
#digita o link do site na barra de url
pyautogui.write('LINK-DO-SITE')
#pressiona o botao enter
pyautogui.press('enter')
#tempo de espera
time.sleep(5)
#digita o login
pyautogui.write('SEU-EMAIL')
#tempo de espera
time.sleep(3)
#pressiona o tab
pyautogui.press('tab')
#digita a senha
pyautogui.write('SUA SENHA')
#tempo de espera
time.sleep(3)
#pressiona o tab
pyautogui.press('tab')
#pressiona o botao enter
pyautogui.press('enter')

