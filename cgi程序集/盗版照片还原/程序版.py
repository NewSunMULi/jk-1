import requests
import json
from tkinter import filedialog


def picture_fixxing():
    want = filedialog.askopenfilename()
    rt = requests.post("https://api.deepai.org/api/colorizer", files={'image': open(want,'rb')},headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'})
    html_content=rt.json()
    picture_path = html_content['output_url']
    picture=requests.get(picture_path)
    file=open('C:\\Users\\Administrator\\Desktop\\恢复彩色照片.jpg', 'wb')
    file.write(picture.content)
    file.close()
    print("彩色照片已生成！")


picture_fixxing()