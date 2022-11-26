import cgi, urllib
import requests as 请求
import json as 加瓦

data = cgi.FieldStorage()
歌曲名 = data.getvalue("mc")
歌手 = data.getvalue("sm")

if 歌曲名 is not None:
    keyword = urllib.parse.quote(歌曲名)
else:
    歌曲名 = "与他/她相关的歌曲"
    keyword = urllib.parse.quote(歌手)
url = [
        'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1'.format(
            keyword)]
referer = ['https://www.kuwo.cn/search/list?key={}'.format(keyword)]
head = {'Cookie': '_ga=GA1.2.337131840.1656857132; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1656857131,1658635516; _gid=GA1.2.992504106.1658635516; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1658636222; kw_token=KUUKU45TJK',
        'csrf': 'KUUKU45TJK',
        'Referer': '{}'.format(referer[0]),
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        }
a = 请求.get(url=url[0], headers=head)
list2 = 加瓦.loads(a.text)["data"]["list"]
歌曲列表1 = []
结果2 = []
for name in list2:
    歌曲列表1.append({"歌曲名": name['name'], "歌手": name['artist'], "rid识别号": name['rid']})  # 爬数据
    if name['artist'] == 歌手:
        结果2.append({"歌曲名": name['name'], "歌手": name['artist'], "rid识别号": name['rid']})
    else:
        pass
if 歌手 == "" or 歌手 is None:
    结果2 = 歌曲列表1
    歌手 = "任意歌手"

html2 = ""
for a in range(len(结果2)):
    html2 += f"{a+1}." + 结果2[a]["歌曲名"] + "----" + 结果2[a]["歌手"] + "<br>"
    try:
        f = 请求.get(f"http://www.kuwo.cn/api/v1/www/music/playUrl?mid={结果2[a]['rid识别号']}", headers=head)
        p = 加瓦.loads(f.text)
        html2 += f"<a href={f'''{p['data']['url']}'''}>乐曲链接-音频</a><br>"
    except KeyError:
        html2 += "VIP歌曲不敢偷，怕坐牢<br>"
    try:
        f = 请求.get(f"http://www.kuwo.cn/api/v1/www/music/playUrl?mid={结果2[a]['rid识别号']}&type=mv", headers=head)
        p = 加瓦.loads(f.text)
        html2 += f"<a href={f'''{p['data']['url']}'''}>乐曲链接-视频</a><br><br>"
    except KeyError:
        html2 += "没有视频可以给你放<br><br>"


题目 = "搜索结果"

html代码 = f'''<html>
<head>
<title>{题目}</title>
</head>
<body>
<h2>结果：{歌曲名}---{歌手}</h2>
{html2}
</body>
</html>'''

print("Content-type:text/html\n\n")
print(html代码)