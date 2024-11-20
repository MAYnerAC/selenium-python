import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time # (Opcional)

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")  # Desactiva logs de error
    chrome_options.add_argument("--start-maximized")  # Inicia el navegador maximizado
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_admin_login(driver):
    driver.get("https://localhost:44357/")
    time.sleep(2)

    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Inicio de sesion"))
    )
    login_link.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "correo"))
    )
    driver.find_element(By.ID, "correo").send_keys("admin@example.com")
    driver.find_element(By.NAME, "contrasena").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.url_contains("Panel"))
    print("Inicio de sesión como administrador exitoso")

    dropdown_toggle = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-toggle"))
    )
    dropdown_toggle.click()
    time.sleep(2)

    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Cerrar Sesión"))
    )
    logout_link.click()
    time.sleep(2)
    print("Cierre de sesión como administrador exitoso")

def test_provider_login(driver):
    driver.get("https://localhost:44357/")
    time.sleep(2)

    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Inicio de sesion"))
    )
    login_link.click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "correo"))
    )
    driver.find_element(By.ID, "correo").send_keys("prov@example.com")
    driver.find_element(By.NAME, "contrasena").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(EC.url_contains("Panel"))
    print("Inicio de sesión como proveedor exitoso")

    dropdown_toggle = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "dropdown-toggle"))
    )
    dropdown_toggle.click()
    time.sleep(2)

    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Cerrar Sesión"))
    )
    logout_link.click()
    time.sleep(2)
    print("Cierre de sesión como proveedor exitoso")
