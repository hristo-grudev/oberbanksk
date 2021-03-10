import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import OberbankskItem
from itemloaders.processors import TakeFirst


class OberbankskSpider(scrapy.Spider):
	name = 'oberbanksk'
	start_urls = ['https://www.oberbank.sk/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="accordion-wrapper"]/div[contains(@class, "dt-accordion")]')
		for post in post_links:
			title = post.xpath('.//h4//text()').get()
			description = post.xpath('./div[contains(@class, "dt-content")]//text()[normalize-space() and not(ancestor::a)]').getall()
			description = [remove_tags(p).strip() for p in description]
			description = ' '.join(description).strip()

			item = ItemLoader(item=OberbankskItem(), response=response)
			item.default_output_processor = TakeFirst()
			item.add_value('title', title)
			item.add_value('description', description)

			yield item.load_item()
