from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    
    return driver

def login(driver,email,password):
    driver.get("https://www.linkedin.com/login")

    username_elmt = driver.find_element_by_name("session_key")
    username_elmt.send_keys(email)

    password_elmt = driver.find_element_by_name("session_password")
    password_elmt.send_keys(password)

    password_elmt.submit()

    return driver

def scrape_profiles(configs):
    #initialize web driver
    driver = get_driver()
    #login to LinkedIn
    driver = login(driver,**configs.linkedin_credentials)