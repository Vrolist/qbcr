# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import requests

file_dir = "C:/Users/Hus/Desktop/qiubai_pic/{}"

class QbcrPipeline(object):
    def process_item(self, item, spider):
        for i in item['img_urls']:
            fname = i.split('/')[-1]
            file_content = requests.get(i)
            if file_content.status_code != 200:
                print('无法访问链接', i)
            else:
                with open(file_dir.format(fname), 'wb') as file:
                    file.write(file_content.content)
                file.close()
        return item
