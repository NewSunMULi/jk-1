import smtplib as sp  # 邮件发送
from email.header import Header  # 邮件内容构造--发给谁
import email.mime.text as tx  # 邮件内容构造--发什么
import email.mime.multipart as mm  # 发多种文件
from typing import List

接收者 = ["3029599103@qq.com", "1323615748@qq.com", "2100318425@qq.com", "3619682441@qq.com"]
html代码 = "<h1>hello gays</h1>\n<p>祝你学习快乐</p>"
玄氏授权码 = ["kcjiqgpvcunmdfia", "daspbogkdbqddjbe"]
发送者 = {"陈玄": "2802912710@qq.com", "蔡徐坤": "VRt-21_Cw@qq.com"}


def html_send(j):
    msg1 = tx.MIMEText("", "plain", "utf-8")  # 第二个参数plain为纯文本,html发送网站, 第三个参数是编码
    msg1["From"] = Header("蔡徐坤")  # 发送人名字
    msg1["To"] = Header("帅哥")  # 接收人名字
    msg1["Subject"] = Header("来自python的祝福", "utf-8")
    St = sp.SMTP()  # 创建smtp对象
    St.connect("smtp.qq.com", 587)  # host--邮箱smtp服务器地址, port--端口号,465(可能被舍弃了用不了)或587(qq)
    St.login("2100318425@qq.com", 玄氏授权码[1])  # 第二个参数是smtp授权码
    aq = St.send_message(msg1, "2100318425@qq.com", j)  # 第三个要mime对象.as_string()才能发出去
    St.quit()
    return aq


def 正式发送(附件: List[str] = None, 发件人: List[str] = None, 收件人: List[str] = None, 统一收件人名: str = None, title=None,
         text=None, 格式="纯文本", 授权码=None):
    jk_msg = mm.MIMEMultipart()
    jk_msg['From'] = Header(发件人[0])
    jk_msg['To'] = Header(统一收件人名)
    jk_msg["Subject"] = Header(title, "utf-8")
    if 格式 == "纯文本":
        格式 = "plain"
    elif 格式 == "html文本":
        格式 = "html"
    else:
        raise TypeError("你的格式我好像不认得，请您重新修改下谢谢!")
    jk_msg.attach(tx.MIMEText(text, 格式))  # 添加邮件部件，例如文字网页等
    if 附件 is not None:
        for jk in 附件:
            att = tx.MIMEText(open(jk, 'rb').read(), 'base64', 'utf-8')  # 附件文件打开格式
            att["Content-Type"] = 'application/octet-stream'  # 类型声明，死背下来
            att["Content-Disposition"] = f'attachment; filename="{jk}"'  # 文件名自己写
            jk_msg.attach(att)
    try:
        St = sp.SMTP()  # 创建smtp对象
        St.connect("smtp.qq.com", 587)  # host--邮箱smtp服务器地址, port--端口号,465(可能被舍弃了用不了)或587(qq)
        St.login(发件人[1], 授权码)  # 第二个参数是smtp授权码
        St.send_message(jk_msg, 发件人[1], 收件人)  # 第三个要mime对象.as_string()才能发出去
        St.quit()
        print(f"发送成功，信息如下:\n发件人:{发件人[0]}-{发件人[1]}\n统一收件人:{统一收件人名}-{收件人}\n使用Python发送")
    except Exception as E:
        print(f"发送失败，原因{E}")


if __name__ == "__main__":
    file1 = ['D:/提交/jk-1/礼包/凯子的生日礼物/生日礼物.exe']
    file2 = ['F:/DCIM/104_PANA/P1040182.jpg', 'F:/DCIM/104_PANA/P1040273.jpg']
    化名 = input("给自己取个名字")
    给谁 = input("收件人名字")
    title = input("题目")
    text = input("正文")
    st = input(f"确认发送?")
    if st == "y":
        正式发送(file1, [化名, 发送者["陈玄"]], [接收者[-2]], 给谁, title, text, 授权码=玄氏授权码[0])
        jk = False
