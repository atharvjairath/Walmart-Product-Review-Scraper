# Imports
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from dateutil.parser import parse
import time
import pandas as pd

# Dataframe to store our data
df = pd.DataFrame(columns = ['Date', 'Reviewer_Name', 'Review_title', 'Review_description', 'Rating','Verified'])

# Intializing Chrome Driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('C:\chromedriver.exe',options=options)

# Opens the Walmart Product Link
driver.get('https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365')
driver.implicitly_wait(2)
# Scroll down to Reviews
scroll_to_reviews = driver.find_element_by_id('product-reviews')
driver.execute_script("arguments[0].scrollIntoView();",scroll_to_reviews)
# All reviews
all_reviews_button = driver.find_element_by_class_name("ReviewsHeaderWYR-seeAll").click()
driver.implicitly_wait(2)
# Selecting Newest to Oldest
select = Select(driver.find_element_by_class_name("field-input--compact"))
select.select_by_visible_text("newest to oldest")
time.sleep(2)

flag  = False
pagenum = 1

# Loop for pages
print("Extracting Reviews...")
while True:
    time.sleep(1)
    all_reviews = driver.find_elements_by_class_name("review")
    print("Scraping Page No.",pagenum)
    for review in all_reviews:
        # Converting the string date into int datatime format 
        date_in_num = parse(review.find_element_by_class_name("review-date-submissionTime").get_attribute("content"))

        if date_in_num.year == 2020 and date_in_num.month == 12:
            # if this condition is true we will come out of the loop
            flag = True
            print("Review of December 2020 reached! Ending Program....")
            break
        # Name
        reviewer_name = review.find_element_by_class_name("review-footer-userNickname").text
        # Rating
        rating = int(float(review.find_element_by_class_name("seo-avg-rating").text))
        # Verified or not? (Optional)
        try:
            review_verified = review.find_element_by_class_name("verified").text
            review_verified = True
        except: 
            review_verified = False
        # Title
        try:
            review_title = review.find_element_by_class_name("review-title").text
        except: 
            # Filling it witn NaN
            review_title= None
        # Description
        review_desc = review.find_element_by_class_name("review-text").text
        df.loc[len(df.index)] = [date_in_num,reviewer_name,review_title,review_desc,rating,review_verified]

    if flag:
         break
    driver.find_element_by_class_name("paginator-btn-next").click()
    pagenum+=1

driver.quit()
print("Saving reviews")
df.to_csv("output.csv")
print("Done")
