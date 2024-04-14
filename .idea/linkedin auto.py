
'''

/Boole.eletronica@gmail.com
Lendario623!


'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Configuração do driver e navegação inicial
service = Service(r'C:\path\to\edgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get("https://www.linkedin.com/login")

# Utilizando variáveis de ambiente para as credenciais
email = os.getenv('Boole.eletronica@gmail.com')  # Substitua pelo seu e-mail real
password = os.getenv('Lendario623!')  # Substitua pela sua senha real

# Espera pela presença do campo de e-mail
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#username'))
)
email_field.send_keys(email)

# Espera pelo campo de senha e insere a senha
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#password'))
)
password_field.send_keys(password)

# Clica no botão de login
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
)
login_button.click()

# Aguarda até que a página de feed esteja carregada
WebDriverWait(driver, 10).until(
    EC.url_contains("https://www.linkedin.com/feed/")
)

# Encontra o campo de postagem e insere o texto
post_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-ql-editor-contenteditable="true"]'))
)
post_field.click()
post_field.send_keys('Aqui vai o seu texto')

# Espera até que o botão de publicar esteja clicável
publish_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.share-box-feed-entry__trigger'))
)
publish_button.click()

# Fecha o navegador após a ação
driver.quit()
