from scrapy.crawler import CrawlerProcess

from tpc_crawler.spiders.infocom_tpc_spider import InfocomTpcSpider
from conference_crawler.spiders.acm_spider import ACMSpider
from conference_crawler.spiders.dblp_spider import DblpSpider


# Unused, use scrapy crawl xxx instead


def main():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "acm.json": {"format": "json"},
        },
    })

    process.crawl(ACMSpider)
    process.start()


if __name__ == '__main__':
    main()
