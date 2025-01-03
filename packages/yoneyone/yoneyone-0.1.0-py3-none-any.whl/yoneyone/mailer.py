import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, sender_email, sender_password, smtp_server="smtp.gmail.com", smtp_port=587):
    """
    シンプルなメール送信モジュール
    """
    # メール作成
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # SMTPサーバーに接続してメールを送信
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("メール送信成功")
    except Exception as e:
        print(f"メール送信に失敗しました: {e}")
