# webcrawler
Crawl web page to find your content using selenium and web driver.

#requirement
Framework: Python3.7, selenium
Memoery: Your local, docker or server should have 2+GB memory as required by firefox that I am currently using.

#installation of required packages
```
bash packages.sh
```

#run
```
python3 crawl.py [url] [cssselector]
```

#usage
```
from webcrawler import FirefoxCrawler

crawler = FirefoxCrawler()
driver = crawler.load_page(url)
video = driver.find_element_by_css_selector('video')
print(video.get_attribute('src'))
```
