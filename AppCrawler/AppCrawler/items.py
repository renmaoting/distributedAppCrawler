# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class AppCrawlerItem(scrapy.Item):
    Name = scrapy.Field()
    URL = scrapy.Field()
    Price = scrapy.Field()
    Genre = scrapy.Field()
    Downloads = scrapy.Field()
    Rating = scrapy.Field()
    Review_number = scrapy.Field()
    Updated = scrapy.Field()
    Author = scrapy.Field()
    Version = scrapy.Field()

class ExampleLoader(ItemLoader):
    default_item_class = AppCrawlerItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()

