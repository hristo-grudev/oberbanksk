import scrapy


class OberbankskItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
