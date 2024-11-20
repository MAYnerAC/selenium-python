from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Configurar el WebDriver
service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--log-level=3")  # Desactiva logs de error
chrome_options.add_argument("--start-maximized")  # Inicia el navegador maximizado
driver = webdriver.Chrome(service=service, options=chrome_options)

# Prueba para administrador
def test_admin_login():
    print("Iniciando prueba: Inicio de sesión como administrador")
    driver.get("https://localhost:44357/")  # URL base de la aplicación

    # Buscar y hacer clic en "Inicio de sesion"
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Inicio de sesion"))
    )
    login_link.click()
    time.sleep(2)

    # Completar el formulario de inicio de sesión para administrador
    driver.find_element(By.ID, "correo").send_keys("admin@example.com")
    driver.find_element(By.NAME, "contrasena").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    # Verificar que se redirige al panel del administrador
    WebDriverWait(driver, 10).until(
        EC.url_contains("Panel")
    )
    print("Inicio de sesión como administrador exitoso")

    # Cerrar sesión
    dropdown_toggle = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-toggle"))
    )
    dropdown_toggle.click()
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Cerrar Sesión"))
    )
    logout_link.click()
    print("Cierre de sesión como administrador exitoso")
    time.sleep(2)





# Prueba para proveedor
def test_provider_login():
    print("Iniciando prueba: Inicio de sesión como proveedor")
    driver.get("https://localhost:44357/")  # URL base de la aplicación

    # Buscar y hacer clic en "Inicio de sesion"
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Inicio de sesion"))
    )
    login_link.click()
    time.sleep(2)

    # Completar el formulario de inicio de sesión para proveedor
    driver.find_element(By.ID, "correo").send_keys("prov@example.com")
    driver.find_element(By.NAME, "contrasena").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    # Verificar que se redirige al panel del proveedor
    WebDriverWait(driver, 10).until(
        EC.url_contains("Panel")
    )
    print("Inicio de sesión como proveedor exitoso")

    # Cerrar sesión
    dropdown_toggle = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-toggle"))
    )
    dropdown_toggle.click()
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Cerrar Sesión"))
    )
    logout_link.click()
    print("Cierre de sesión como proveedor exitoso")
    time.sleep(2)

# Ejecutar ambas pruebas
try:
    test_admin_login()
    test_provider_login()
finally:
    driver.quit()
