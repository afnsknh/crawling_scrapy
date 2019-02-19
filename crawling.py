import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "bricket_spider"
    start_urls = ['https://brickset.com/sets/year-2016']
    
BrickSetSpider()
