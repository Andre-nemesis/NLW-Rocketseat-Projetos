import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_address, body):
    from_addr = "zha2nb3qlzvuovxu@ethereal.email"
    login = "zha2nb3qlzvuovxu@ethereal.email"
    password = "7kqXCakDTURCGewJrT"

    msg = MIMEMultipart()
    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = ", ".join(to_address)
    msg["Subject"] = "Confirmação de Viagem!"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(user=login, password=password)
    text = msg.as_string()

    for email in to_address:
        server.sendmail(from_addr, email, text)

    server.quit()
