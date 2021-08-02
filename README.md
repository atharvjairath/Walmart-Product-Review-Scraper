
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
5. After reaching December 2020 the code stops and saves the data into a 'output.csv' file.

## Problem Faced 
1. The date was in string format for example *May 13, 2021*.
> To make the date in clean format. I used [dateutil](https://dateutil.readthedocs.io/en/stable/) to parse the date into required format.
~~~~py
 date_in_num = parse(review.find_element_by_class_name("review-date-submissionTime").get_attribute("content"))
~~~~

2. Walmart also has a bot detection, which we need to take care of. To reduce the chance of bot detection we can implement some tricks such as:
> 1. Increasing the size of our driver window.
```python
driver.maximize_window()
```




## What's next?
1. Since Selenium is designed to automate test for Web Applications. We can use other libarires such as **Scrapy** which is faster or **BeautifulSoup** which is much easier.
2. To improve the scraper we can move forward and use other libarires as mentioned above to improve speed and efficenty.



## Author

👤 **Atharv Jairath**

* Email: atharv.jairath@gmail.com
* Github: [@atharvjairath](https://github.com/atharvjairath)
* LinkedIn: [@Atharvjairath](https://www.linkedin.com/in/atharv-jairath-99aa78118/)

