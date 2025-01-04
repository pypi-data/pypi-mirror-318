from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui
import time

def find_element_with_wait_backcode(driver, by, value, timeout, parent):
    if parent is None:
        parent = driver  # Usa o driver principal se nenhum elemento pai for passado
    return WebDriverWait(parent, timeout).until(
        EC.presence_of_element_located((by, value))
    )

def find_elements_with_wait_backcode(driver, by, value, timeout, parent):
    if parent is None:
        parent = driver  # Usa o driver principal se nenhum elemento pai for passado
    return WebDriverWait(parent, timeout).until(
        EC.presence_of_all_elements_located((by, value))
    )

def move_to_image(imagem, click_on_final=False):
    """ Primeiro parâmetro é o caminho da imagem, segundo é se tem clique no final ou não.
        Exemplo:

            caminho_imagem = 'C:\\Users\\eliezer.gimenes\\Pictures\\Screenshots\\exemplo.png'
            bc.move_to_image(caminho_imagem, click_on_final=True)

        Obs: Recomenda-se colocar print localizada na mesma pasta do arquivo MAIN para gerar junto com pyinstaller e não dar defeito em outras máquinas
    """
    attempts = 0
    while attempts != 10:
        try:
            localizacao = pyautogui.locateOnScreen(imagem)
            print("1")

            x = localizacao.left + round(localizacao.width/2)
            y = localizacao.top + round(localizacao.height/2)
            print("2")

            pyautogui.moveTo(x, y)
            print("3")

            if click_on_final == True:
                pyautogui.click()
            break
            print("4")

        except:
            print(f" {attempts}° - Erro ao achar a imagem na tela ")
            time.sleep(1)
