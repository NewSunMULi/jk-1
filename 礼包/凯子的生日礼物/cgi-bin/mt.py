import requests as rt
import cgi
from bs4 import BeautifulSoup

data_cgi = cgi.FieldStorage()
words = data_cgi.getvalue("words")
op = []
结果 = []
位置索引 = 2
词性缩写 = ["n.", 'v.', 'adj.', "pron.", 'num.', 'det.', 'adv.', 'vt.', 'vi.', 's.', 'int.', 'art.', 'interj.', 'prep.',
        'conj.']
词性缩写2 = ['名词', '动词', '形容词', '人称代词', '数字', '序数', '副词', '及物动词', '不及物动词', '主词', '感叹词', '冠词', '感叹词', '介词', '连词']
词性缩写3 = dict(zip(词性缩写, 词性缩写2))
header = {'Referer': 'https://www.youdao.com/',
          'Host': 'foundation.youdao.com',
          'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

at = rt.get(url=f"https://www.youdao.com/w/{words}")
data2 = BeautifulSoup(at.text, "lxml")
if " " in words:
    print(data2.find_all("li")[6].text)
else:
    for i in data2.find_all("li"):
        try:
            位置索引 = i.text.index(".")
        except ValueError:
            pass
        if i.text[0:位置索引 + 1] in 词性缩写 and (i.text[0:位置索引 + 1] not in op or "人名" in i.text):
            op.append(i.text[0:位置索引 + 1])
            pp = "<font color='red'>" + i.text[0:位置索引 + 1] + 词性缩写3[i.text[0:位置索引 + 1]] + "</font>" + i.text[位置索引 + 1:]
            结果.append(pp)
    单词变形 = data2.find_all("p", class_="additional")
    ac = True if len(单词变形) != 0 else False  # 三元表达式
    if ac:
        if "span" not in str(单词变形[0]):
            ap = 单词变形[0].text.split(" ")
            while "" in ap[0] or "[\n" in ap[0] or "]" in ap[0]:
                if "[\n" in ap:
                    ap.remove("[\n")
                elif "]" in ap:
                    ap.remove("]")
                elif "" in ap:
                    ap.remove('')
                else:
                    break
            for j in ap:
                结果.append(j.split("\n")[0])
        else:
            pass
    else:
        pass

html2 = f"<h2>{words}</h2>"
for dh in 结果:
    html2 += f"{dh}<br>"

html2 += "<a href=../index.html>返回</a>"

html代码 = f'''<html>
<head>
<title>查询结果 英->中</title>
</head>
<body>
<h2>结果</h2>
{html2}
</body>
</html>'''

print("Content-type:text/html\n\n")
print(html代码)
