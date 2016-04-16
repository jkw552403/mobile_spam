from collections import defaultdict
import json
import sys
from time import sleep

from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://www.eprice.com.cn/mobile/buyerguide/?class=1&manu='
BRANDS = ['Samsung', 'HTC', 'SONY', 'ASUS', 'Apple', 'LG', 'OPPO', 'HUAWEI',
          'InFocus', 'Xiaomi', 'Acer', 'Benq', 'Coolpad', 'FET', 'Gionee',
          'GSmart', 'Letv', 'Meitu', 'Meizu', 'Microsoft', 'Motorola',
          'Nextbit', 'Nokia', 'OnePlus', 'Panasonic', 'TWM', 'ZTE']


def main(out_file):
    result = defaultdict(list)

    for brand in BRANDS:
        url = BASE_URL + brand
        text = requests.get(url).text
        soup = BeautifulSoup(text)
        print("Scrap all models of {}!!!".format(brand))
        products = soup.findAll(attrs={'class': 'prod-detail'})
        print("There are {} {} models".format(len(products), brand))
        for prod in products:
            title = None
            for content in prod.contents:
                try:
                    title = content.attrs['title']
                    break
                except AttributeError:
                    continue
            if title is None:
                raise ValueError("Empty Title in {}".format(brand))
            result[brand].append(title)
        json.dump(result, out_file)
        sleep(3)


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Please type the output file!!!")
        exit(1)
    with open(argv[1], 'w') as out_file:
        main(out_file)
