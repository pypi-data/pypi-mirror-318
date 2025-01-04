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

def move_to_image(imagem, click_on_final=False, tolerancia=1):
    """Move o mouse até o centro de uma imagem na tela e clica, se necessário.

    Args:
        imagem (str): Caminho da imagem a ser localizada.
        click_on_final (bool): Se True, realiza um clique ao final.

    Exemplo:
        caminho_imagem = 'C:\\User\\Caminho\\exemplo.png'
        move_to_image(caminho_imagem, click_on_final=True, tolerancia=0.9)

    Nota:
        Recomenda-se colocar a imagem na mesma pasta do arquivo MAIN para evitar problemas
        ao gerar o executável com pyinstaller e rodar em outras máquinas.
    """
    attempts = 0
    while attempts < 10:
        try:
            localizacao = pyautogui.locateOnScreen(imagem, confidence=tolerancia)
            if localizacao is not None:
                x = localizacao.left + round(localizacao.width / 2)
                y = localizacao.top + round(localizacao.height / 2)
                pyautogui.moveTo(x, y)

                if click_on_final:
                    pyautogui.click()
                return

        except Exception as e:
            attempts += 1
            ultima_excecao = e
            print(f"{attempts}° tentativa - {e}")
            time.sleep(1)

    # Se todas as tentativas falharem, levanta erro
    raise ValueError(f"Erro ao procurar a imagem '{imagem}' após 10 tentativas.") from ultima_excecao