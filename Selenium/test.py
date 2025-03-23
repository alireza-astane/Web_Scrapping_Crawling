# # Python program to demonstrate
# # selenium

# # import webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# from webdriver_manager.chrome import ChromeDriverManager

# # create webdriver object
# driver = webdriver.Chrome
# # get google.co.in
# service = Service(ChromeDriverManager().install())
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

# try:
#     # Open Google
#     a = driver.get("https://www.google.com")
#     print(a)
# finally:
#     # Close the browser
#     driver.quit()


# Interacting with Webpage using Python Selenium


# element = driver.find_element(By.ID, "passwd-id")
# element = driver.find_element(By.NAME, "passwd")
# element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
# # If you need to find multiple elements, use:

# elements = driver.find_elements(By.NAME, "passwd")
# # To find a link by its text, ensure the text is an exact match:

# element = driver.find_element(By.LINK_TEXT, "Link Text")


# Import the necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Added import for Keys

# Create a webdriver object. Here we use Firefox, but you can choose other browsers like Chrome, Edge, etc.
driver = webdriver.Firefox()

# Navigate to the GeeksforGeeks website
driver.get("https://www.geeksforgeeks.org/")

# Maximize the browser window
driver.maximize_window()

# Locate the search icon element using XPath
searchIcon = driver.find_element(By.XPATH, "//span[@class='flexR gs-toggle-icon']")

# Click on the Search Icon to activate the search field
searchIcon.click()

# Locate the input field for search text using XPath
enterText = driver.find_element(By.XPATH, "//input[@class='gs-input']")

# Enter the search query "Data Structure" into the input field
enterText.send_keys("Data Structure")

# Send the RETURN key to submit the search query
enterText.send_keys(Keys.RETURN)


## wait
## explicit wait
# # import webdriver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # create webdriver object
# driver = webdriver.Firefox()

# # get geeksforgeeks.org
# driver.get(&quot;https://www.geeksforgeeks.org/&quot;)

# # get element  after explicitly waiting for 10 seconds
# element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.link_text, &quot;Courses&quot;))
#     )
# # click the element
# element.click()


# implicit wait


# # import webdriver
# from selenium import webdriver

# driver = webdriver.Firefox()

# # set implicit wait time
# driver.implicitly_wait(10) # seconds

# # get url
# driver.get("http://somedomain / url_that_delays_loading")

# # get element after 10 seconds
# myDynamicElement = driver.find_element_by_id("myDynamicElement")


## action chains

# # import webdriver
# from selenium import webdriver

# # import Action chains
# from selenium.webdriver.common.action_chains import ActionChains

# # create webdriver object
# driver = webdriver.Firefox()

# # get geeksforgeeks.org
# driver.get(&quot;https://www.geeksforgeeks.org/&quot;)

# # get element
# element = driver.find_element_by_link_text(&quot;Courses&quot;)

# # create action chain object
# action = ActionChains(driver)

# # click the item
# action.click(on_element = element)

# # perform the operation
# action.perform()
