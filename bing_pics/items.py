import scrapy


class BingPicsItem(scrapy.Item):
    """
    保存抓取数据的容器
    必须继承 Item
    """
    url = scrapy.Field()  # 图片url
