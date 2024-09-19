from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración del driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL a scrapear
url = 'https://www.bumeran.com.pe/empleos-busqueda-ingeniero-de-datos.html'
driver.get(url)

# Esperar a que la página cargue
time.sleep(3)

# Encontrar todas las etiquetas <h3> dentro de #listado-avisos
h3_elements = driver.find_elements(By.XPATH, '//*[@id="listado-avisos"]//h3')
# Encontrar todos los enlaces <a> dentro de #listado-avisos
a_elements = driver.find_elements(By.XPATH, '//*[@id="listado-avisos"]//a')

# Imprimir el texto de cada elemento <h3>
print("Elementos <h3> dentro de #listado-avisos:\n" + "="*40)
for h3 in h3_elements:
    print(f"- {h3.text}")

# Imprimir los enlaces y sus textos
print("\nEnlaces <a> dentro de #listado-avisos:\n" + "="*40)
for a in a_elements:
    link_text = a.text.strip()
    link_url = a.get_attribute("href")
    if link_text:  # Solo imprime si hay texto
        print(f"Texto: {link_text}\nURL: {link_url}\n")

# Cerrar el navegador
driver.quit()
