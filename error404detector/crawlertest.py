from webcrawler.crawler import *

def crawlingCallback(data, browser=None):
    print(data)

crawler = Crawler\
(
    ["https://github.com/hayj/WebCrawler"],
    crawlingCallback=crawlingCallback,
    browsersDriverType=DRIVER_TYPE.chrome,
    proxies=getAllProxies(),
    browserCount=10,
    stopCrawlerAfterSeconds=10000000,
    banditRoundDuration=10000000,
    browserParams=\
    {
        "chromeDriverPath": "/home/hayj/Programs/browserdrivers/chromedriver",
        "phantomjsPath": "/home/hayj/Programs/headlessbrowsers/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",
    },
)
crawler.start()

