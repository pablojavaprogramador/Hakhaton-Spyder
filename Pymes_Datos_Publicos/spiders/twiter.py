from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter
import pandas as pd
import itertools
import scrapy

class twitter(scrapy.Spider):
    name = "twitter"


    def __init__(self):
        self.scrapy_twitter(word="telmex")
        print('Hola mundo ejecutado')
    
    FEEDS = {
    'data/%(name)s/%(name)s_batch_%(batch_id)d.csv': {
        'format': 'csv',
        'batch_item_count': 10,
        }
}

    def scrapy_twitter(self, word = "walmart", start = "2022-06-01", end = "2022-07-14", loc = '19.794185, -99.89653, 100km'):
        tqdm.pandas()
        data = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('{} since:{} until:{} geocode:"{}"'.format(word,start,end,loc)).get_items(), 500))
        return data[['content','date']]