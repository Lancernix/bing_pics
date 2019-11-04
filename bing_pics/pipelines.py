from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import re
from scrapy.exceptions import DropItem


class MyImagesPipeline(ImagesPipeline):
    """
    自定义的pipeline类
    需要继承相应的类
    负责对数据进行保存/输出等一系列操作
    """
    def get_media_requests(self, item, info):
        yield Request(item['url'])

    def file_path(self, request, response=None, info=None):
        url = request.url
        image_name = '%s.jpg' % re.match('^.*?bing/(.*?)_ZH', url).group(1)
        return image_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Download Failed')
        return item
