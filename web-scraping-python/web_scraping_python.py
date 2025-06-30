import os
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:\proyectos\python\web-scraping-python\chromedriver-win64" # Add the path to the ChromeDriver executable to the system PATH
driver = webdriver.Chrome() # Initialize the Chrome driver, opens a new browser window

driver.get("https://www.selenium.dev/selenium/web/click_tests/html5_submit_buttons.html")

driver.implicitly_wait(10) # Espero a que cargue la página

my_driver =  driver.find_element("id", "external_explicit_submit")
my_driver.click() 

# confirmation_submit = driver.find_element(By.TAG_NAME, "h1")
# print(f"{confirmation_submit.text == 'Submitted Successfully!'}") #Devuelve true si el texto "submitted successfully" matchea en la página pero no funciona si el h1 cambia (primero dice submitting por lo que siempre devuelve false)

WebDriverWait(driver, 30).until(  #espera 30s hasta el h1 cambia 
    EC.text_to_be_present_in_element(  #EC significa Expected Condition
        (By.TAGNAME, "h1" ),
        "Submitted Successfully!"  #Filtro para que espere hasta que el texto del h1 sea "Submitted Successfully!"
        )
)


