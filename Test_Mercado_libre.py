from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Buscar elementos 
from selenium.webdriver.common.keys import Keys #Mandar una tecla en especifico EJ Enter
from selenium.webdriver.support.ui import WebDriverWait #Esperar por un elemento y detenr el programa si no lo encuentra
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path="chromedriver.exe") #si se quiere usar Mozilla se tendria que cambiar este executable por uno que funcione con el navegador
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.mercadolibre.com") 

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/nav/ul/li[11]/a"))
    ).click() #Selecciona el pais (México)

input_element = driver.find_element(By.NAME, "as_word" ) #Selecciona la barra de busqueda 
input_element.clear() #limpia el campo
input_element.send_keys(Keys.CONTROL + "a")  # Selecciona todo
input_element.send_keys(Keys.DELETE)         # Elimina todo el texto
input_element.send_keys("Playstation 5" + Keys.ENTER) #introducir texto y dar clic 


try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cookie-consent-banner-opt-out__action"))
    ).click()
except:
    pass  
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/aside/section[2]/div[5]/ul/li[1]/a/span[1]"))).click() #Nuevo

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/aside/section[2]/div[11]/ul/li[1]/a/span[2]"))).click() #Local


sort_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/section/div[2]/div/div/div/div[2]/div/div/button/span"))) #Selecciona el menu desplegable de las opciones 
sort_button.click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/section/div[2]/div/div/div/div[2]/div/div/div/div/div/ul/li[3]/div/div/span"))).click() #Seleccionar la opcio de  Mayor a menor precio 


WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.poly-card"))) 

products = driver.find_elements(By.CSS_SELECTOR, "div.poly-card")[:5]
###/////////////////////////////////////////////////////////////###
print("\n Los primeros 5 productos: \n")
for i, product in enumerate(products, 1):
    try:
        name = product.find_element(By.CSS_SELECTOR, "a.poly-component__title").text
        price = product.find_element(By.CSS_SELECTOR, ".poly-price__current .andes-money-amount__fraction").text
        print(f"{i}. {name} - ${price}")
    except:
        print(f"{i}. No se encontraron productos")
time.sleep(30)
driver.quit()