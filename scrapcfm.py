#pip install selenium
#pip install webdriver-manager

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.implicitly_wait(10)
navegador.get("https://portal.cfm.org.br/busca-medicos/")


search_box = navegador.find_element(by=By.NAME, value="crm")
search_box.send_keys("4189")
print(search_box.text)




# navegador.find_element("btnPesquisar").click()

# wait = WebDriverWait(driver, timeout=2)
# wait.until(lambda d : revealed.is_displayed())

# revealed.send_keys("Displayed")



# navegador.find_element('xpath','//*[@id="buscaForm"]/div/div[1]/div[3]/div/input').send_keys("4189")
# button = navegador.find_element('xpath','//*[@id="buscaForm"]/div/div[4]/div[2]/button')
# navegador.execute_script('arguments[0].click()', button)

# wait = WebDriverWait(navegador, 10)