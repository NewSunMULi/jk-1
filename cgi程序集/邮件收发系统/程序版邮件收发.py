import smtplib as sp  # 邮件发送
from email.header import Header  # 邮件内容构造--发给谁
import email.mime.text as tx  # 邮件内容构造--发什么

接收者 = ["3029599103@qq.com", "1323615748@qq.com", "2100318425@qq.com"]
html代码 = "<h1>hello gays</h1>\n<p>祝你学习快乐</p>"
msg1 = tx.MIMEText(html代码, "html", "utf-8")  # 第二个参数plain为纯文本,html发送网站, 第三个参数是编码
msg1["From"] = Header("蔡徐坤")  # 发送人名字
msg1["To"] = Header("帅哥")  # 接收人名字
msg1["Subject"] = Header("来自python的祝福", "utf-8")
St = sp.SMTP()  # 创建smtp对象
St.connect("smtp.qq.com", 587)  # host--邮箱smtp服务器地址, port--端口号,465或587(qq)
St.login("2802912710@qq.com", "kcjiqgpvcunmdfia")  # 第二个参数是smtp授权码
St.send_message(msg1, "2802912710@qq.com", 接收者)  # 第三个要mime对象.as_string()才能发出去
St.quit()
print("success")
