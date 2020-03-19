import os
from selenium import webdriver
from cachetools import cached, TTLCache

# enables use of selenium on heroku
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

url = "https://coronavirus.1point3acres.com/en"
states = ["New York", "Washington", "California", "Massachusetts",
          "Florida", "New Jersey", "Louisiana", "Colorado ", "Georgia",
          "Illinois", "Texas", "Pennsylvania", "Maryland", "Michigan",
          "Minnesota", "Tennessee", "Virginia", "Oregon", "Ohio",
          "Wisconsin", "Nevada", "Utah", "Connecticut", "North Carolina",
          "South Carolina", "Indiana", "Alabama", "Kentucky", "Iowa",
          "Arkansas", "Rhode Island", "New Mexico", "Arizona",
          "Nebraska", "New Hampshire", "Maine", "Vermont", "Mississippi",
          "Kansas", "Oklahoma", "Hawaii", "South Dakota", "Wyoming",
          "Missouri", "Montana", "Delaware", "Idaho", "Alaska", "North Dakota", "West Virginia"]

@cached(cache=TTLCache(maxsize=3, ttl=86400))
def retrieve_data():
    data = {}
    driver.get(url)
    for state in states:
        data[state] = {}
        try:
            span = driver.find_element_by_xpath("//span[text()='{}']".format(state))
        except:
            continue
        driver.execute_script("arguments[0].click();", span)
        counties = driver.find_element_by_class_name("counties")
        text = counties.text
        d = text.split("\n")

        for i in range(0, len(d), 4):
            county = d[i]
            confirmed = d[i + 1].split("+")[0]
            deaths = d[i + 2].split("+")[0]
            data[state][county] = {}
            data[state][county]['confirmed'] = int(confirmed)
            data[state][county]['deaths'] = deaths

        driver.execute_script("arguments[0].click();", span)
    return data