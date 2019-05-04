import sys
from webcrawler import FirefoxCrawler

url = sys.argv[1]
cssselector = sys.argv[2]
attribute = sys.argv[3]

crawler = FirefoxCrawler(headless = False)
driver = crawler.load_page(url)
videos = driver.find_element_by_css_selector(cssselector)
print(videos.get_attribute(attribute))
