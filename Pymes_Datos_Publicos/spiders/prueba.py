import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
import pandas as pd
import os
import pandas
import csv


class DmozSpider(scrapy.Spider):
    name = "pruebas"
    start_urls = [
        "https://omega-sun-rise.negocio.site"
    ]

    def parse(self, response):
      cwd = os.getcwd()  # Get the current working directory (cwd)
      files = os.listdir(cwd)  # Get all the files in that directory
      print("Files in %r: %s" % (cwd, files))
      path= os.getcwd()+'\Pymes_Datos_Publicos\spiders\Final_Data_Hackathon_2022.csv'
      print(str(path))
      with open(str(path), newline='') as File:  
          reader = csv.DictReader(File)
         # self.link()
          for row in reader:
              print(row['Nombre1'])
              
