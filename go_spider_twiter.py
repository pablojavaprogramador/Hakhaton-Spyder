from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Pymes_Datos_Publicos.spiders.twiter import twitter



process = CrawlerProcess(get_project_settings())
process.crawl(twitter)
process.start()