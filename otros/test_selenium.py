from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://example.com")

print("Título de la página:", driver.title)

driver.quit()

# El WebDriver se descarga en:
# C:\Users\MyUsuario\.wdm
