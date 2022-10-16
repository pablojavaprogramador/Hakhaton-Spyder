# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PymesDatosPublicosItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    pass

class LinkedinItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class PersonProfileItem(Item):
    _id = Field()
    url = Field()
    name = Field()
    also_view = Field()
    education = Field()
    locality = Field()
    industry = Field()
    summary = Field()
    specilities = Field()
    skills = Field()
    interests = Field()
    group = Field()
    honors = Field()
    education = Field()
    experience = Field()
    overview_html = Field()
    homepage = Field()
    