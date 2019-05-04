# webcrawler
Crawl web page to find your content using selenium and web driver.

#requirement
Framework: Python3.7 and Django
Memoery: Your local, docker or server should have 2+GB memory as required by firefox that I am currently using.

#installation of required packages
```
bash packages.sh
```

#run
```
python3 webcrawl.py [url] [cssselector]
```

#usage
```
from webcrawler import FirefoxCrawler

driver = FirefoxCrawler.loadPage(url)
videos = driver.find_element_by_css_selector('video')
video_srcs = [ video.get_attribute('src') for video in videos ]
```
