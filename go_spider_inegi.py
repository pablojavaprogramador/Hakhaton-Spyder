from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Pymes_Datos_Publicos.spiders.gobierno import SpiderGobierno



process = CrawlerProcess(get_project_settings())
process.crawl(SpiderGobierno)
process.start()