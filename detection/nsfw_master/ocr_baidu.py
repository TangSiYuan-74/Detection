

# encoding:utf-8

import requests
import base64
import json

'''
网络图片文字识别
'''


#输入图片地址
#返回文本列表
def ocr(image_path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"
    # 二进制方式打开图片文件
    f = open(image_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = '24.edb7c86bb6750685f3fbb8187306da73.2592000.1680236619.282335-30849076'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
    #将字典中所要的值转换成列表
    dict = response.json()
    list = dict.get('words_result')
    newlist = []
    for item in list:
        newlist.append(item['words'])
    #print(newlist)
    return newlist


if  __name__ == '__main__':
    image = 'C:/Users/汤思源/Desktop/IMG_5177(20230220-232409).JPG'
    ocr(image)
