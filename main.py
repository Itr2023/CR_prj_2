import smtplib
import json


def send_email(from_addr, to_addr, subject, text, encode="utf-8"):
    """
    Отправка электронного письма (email)
    """

    # оставшиеся настройки
    passwd = "**********"
    server = "smtp.yandex.ru"
    port = 587
    charset = f"Content-Type: text/plain; charset={encode}"
    mime = "MIME-Version: 1.0"
    # формируем тело письма
    body = "\r\n".join(
        (
            f"From: {from_addr}",
            f"To: {to_addr}",
            f"Subject: {subject}",
            mime,
            charset,
            "",
            text,
        )
    )

    try:
        # подключаемся к почтовому сервису
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(from_addr, passwd)
        # пробуем послать письмо
        smtp.sendmail(from_addr, to_addr, body.encode(encode))
    except smtplib.SMTPException as err:
        print("Что - то пошло не так...")
        raise err
    finally:
        smtp.quit()

    from_addr = "your-address@yandex.ru"
    to_addr = src["email"]
    subject = "Результаты тестов"
    text = "Привет", src["name"], "твой результат:", src["result"]
    send_email(from_addr, to_addr, subject, text)


with open("data.json", "r", encoding="utf8") as f:
    src = json.load(f)
