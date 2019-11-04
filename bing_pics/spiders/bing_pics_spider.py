from scrapy.spiders import Spider
from bing_pics.items import BingPicsItem
from scrapy import Request


class BingPicsSpider(Spider):
    """
    自定义spider类
    必须继承 Spider
    负责对页面进行解析
    """
    name = 'bing_pics_spider'  # 用于区分不同spider，必须是唯一的
    start_urls = ['https://bing.ioliu.cn/']
    page = 1  # 初始页数

    def parse(self, response):
        item = BingPicsItem()
        urls = response.xpath('//div[@class="container"]/div/div/img/attribute::src')
        for url in urls:
            item['url'] = url.extract()
            yield item
        # 爬取5页
        if self.page < 5:
            self.page += 1
            # 生成后续url
            url = '%s?p=%d' % (self.start_urls[0], self.page)
            yield Request(url, callback=self.parse)
