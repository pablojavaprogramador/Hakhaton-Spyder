import os
import requests
import json
import pandas as pd

from itemadapter import ItemAdapter
from . import sentiment


class PymesDatosPublicosPipeline:
    def process_item(self, item, spider):
        return item

class PymeCrawlerScraperPipeline(object):

    def open_spider(self, spider):
        spider.crawler.stats.set_value('total_articles_added', 0)

    def process_item(self, item, spider):

      #  s = sentiment.get_polarity(sentiment.clean_text(item['body']))

       # item['score'], item['magnitude'] = s.polarity, s.subjectivity

        #if item['score']>0 and item['score']<0.2:
     #       item['sentiment_classification'] = 'neutral'
      #  if item['score']>=-1 and item['score']<=0:
      #      item['sentiment_classification'] = 'negative'
      #  if item['score']>=0.2 and  item['score']<=1:
      #      item['sentiment_classification'] = 'positive'

       # api_url = os.environ['API_URL']
        api_url = 'http://127.0.0.1:3000/api/v1/'
        #response = requests.post(api_url+'articles/', data = json.dumps(ItemAdapter(item).asdict()))
       # response = requests.post(api_url+'articles/', data = json.dumps(ItemAdapter(item).asdict()))
        response = 'respuesta'
        print(response)
       # response_dict = json.loads(response.text)

        #try:
        #    if response_dict['article_url']:
         #       response_dict['detail'] = 'No detail at all'
        #except KeyError:
         #   print('KeyError with detail\n')

        #try:
         #   total = int(spider.crawler.stats.get_stats()['total_articles_added'])
         #   if response_dict['detail'] != 'Article already registered':
         #       spider.crawler.stats.set_value('total_articles_added', total+1)
        #except KeyError:
        #    print('KeyError in the add to the counter\n')

        #return item

    #def close_spider(self, spider):
    #    stats_body = spider.crawler.stats.get_stats()

      #  stats_dict = {
      #      'id': 0,
      #      'response_count': stats_body['downloader/response_count'],
      #      'start_time': str(pd.to_datetime(str(stats_body['start_time'])).tz_localize('UTC').tz_convert('America/Bogota'))[:-6],
      #      'finish_time': str(pd.to_datetime('today')),
           # 'memory_usage_max': stats_body['memusage/max'],
      #      'total_articles_added': stats_body['total_articles_added'],
      #      'scraping_date': str(pd.to_datetime('today')),
      #      'spider': str(spider.name)
      #  }

       # api_url = os.environ['API_URL']
       # api_url = 'http://127.0.0.1:3000/api/v1/'
       # print(api_url)
       # requests.post(api_url+'scraper_stats/', data = json.dumps(ItemAdapter(stats_dict).asdict()))
        

