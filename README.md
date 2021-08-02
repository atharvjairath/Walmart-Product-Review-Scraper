
<h1 align="center">Welcome to Walmart Product Review Scraper 👋</h1>

## 🚀 Libraries
- Selenium
- Dateutil Parser
- Pandas

## What it does
It scrapes the product review data from Walmart Website using Selenium.

## How I built it

1. I used Selenium and Python to vist the specified link and scroll down to product review section.
2. From there we head over to the reviews page by clicking on the **'See all reviews'** Button.
3. Since we need the reviews from today till *December 2020*. We sort reviews by Newest to Oldest.
4. Then we start scraping the data from each 'review block' and after that we head over to the next page.
5. I have also added _Verified_ column in this data since it can be used to sort out Verified data for correct analysis.
6. After reaching December 2020 the code stops and saves the data into a 'output.csv' file.

## Problem Faced 
1. The date was in string format for example *May 13, 2021*.
> To make the date in clean format. I used [dateutil](https://dateutil.readthedocs.io/en/stable/) to parse the date into required format.
~~~~py
 date_in_num = parse(review.find_element_by_class_name("review-date-submissionTime").get_attribute("content"))
~~~~

2. Walmart also has a bot detection, which we need to take care of. To reduce the chance of bot detection we can implement some tricks such as:
* Increasing the size of our driver window.
```py
driver.maximize_window()
```
* Use of randomize with sleep functions to mimic human behaviour with additional surfing.
* Use of VPN to change to new VPN address or proxy to avoid detection.
* Further we can Implement [this](https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver/41220267) process to further avoid the detection.



## What's next?
1. Since Selenium is designed to automate test for Web Applications. We can use other libarires such as **Scrapy** which is faster or **BeautifulSoup** which is much easier.
2. To improve the scraper we can move forward and use other libarires as mentioned above to improve speed and efficenty.
3. We can further improve the code usablity by adding option to find reviews of the similar product.
4. This code can be altered (change all the find elements) to work with other retailers,while the logic almost remains the same.


## Resources Used
* [Selenium Docs](https://www.selenium.dev/documentation/en/)
* [How to avoid bot Detection](http://php8legs.com/en/php-web-scraper/51-how-to-avoid-selenium-webdriver-from-being-detected-as-bot-or-web-spider)

## Author

👤 **Atharv Jairath**

* Email: atharv.jairath@gmail.com
* Github: [@atharvjairath](https://github.com/atharvjairath)
* LinkedIn: [@Atharvjairath](https://www.linkedin.com/in/atharv-jairath-99aa78118/)

