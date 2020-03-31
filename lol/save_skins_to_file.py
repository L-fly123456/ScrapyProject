import pymongo
import requests
import os

def get_skins():
    '''
    连接mongodb数据库，获取英雄名字和对应的皮肤
    :return:英雄名字和对应的皮肤
    '''
    client = pymongo.MongoClient('localhost', 27017)
    db = client['lol']
    # 得到lol数据库中所有集合的名字
    coll_list = db.collection_names ()
    # 遍历每个，连接集合找到数据
    for coll in coll_list:
        connect = db[coll]
        for i in connect.find():
            skins = i.get('skin_image')
            name = i.get('hero')
            yield {
                'skins':skins,
                'name':name
            }

def save_img():
    item = get_skins()

    for i in item:
        img_urls = i['skins']
        file_name = i['name']
        # 提取图片名字和地址，请求每个地址，写入图片的二进制数据
        for url in img_urls:
            img_url = url.split('---')[1]
            img_name = url.split('---')[0]
            if '/' in img_name:
                img_name = img_name.replace('/','')
            # 判断文件是否存在，如果不存在创建文件
            if not os.path.exists('lolskins\\'+file_name):
                os.makedirs('lolskins\\'+file_name)
            response = requests.get(img_url)
            with open('lolskins\\'+file_name+'\\'+img_name+'.jpg','wb') as f:
                f.write(response.content)
                print('成功写入 '+img_name)

if __name__=="__main__":
    save_img()
