import requests
from bs4 import BeautifulSoup
import time

counter=0
#清空文件
f = open("D:\Desktop\shishuai.yan\Desktop\我的坚果云\CODE\Python\Python爬虫\my_crawler/chapter3_xiaozhuzufang.txt","w")
f.close()

#请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

def judgment_sex(class_name):
  if class_name == ['member_ico1']:
      return '女'
  else:
      return  '男'

def get_links(url):
    time.sleep(2)
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get("href")
        get_info(href)

def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('div.pho_info > h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('#pricePart > div.day_l > span')
    imgs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for title, address, price, img, name, sex in zip(titles,addresses,prices,imgs,names,sexs):
        info = {
            'url':url,
            'title':title.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text(),
            'img':img.get("src"),
            'name':name.get_text(),
            'sex':judgment_sex(sex.get("class"))
        }
        f = open("D:\Desktop\shishuai.yan\Desktop\我的坚果云\CODE\Python\Python爬虫\my_crawler/chapter3_xiaozhuzufang.txt","a+")
        try:
            global counter
            counter +=1
            f.write('Counter: '+str(counter)+'\n')
            f.write('url: '+info['url']+'\n')
            f.write('title: '+info['title']+'\n')
            f.write('address: '+info['address']+'\n')
            f.write('price: '+info['price']+'\n')
            f.write('img: '+info['img']+'\n')
            f.write('name: '+info['name']+'\n')
            f.write('sex: '+info['sex']+'\n\n')
            f.close()
        except UnicodeEncodeError:
            pass

#if __name__ == '__main__':
def main():
    urls = ['http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,14)]
    counter = 0
    for single_url in urls:
        get_links(single_url)
        time.sleep(10)


main()