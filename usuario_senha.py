import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from recolheInfo import entrada_dados

receiver_email = input("Digite o email do cliente: ")
sender_email = "contato@infopublicpb.com.br"
senha = "#info8116*"
srvSMTP = "smtp.gmail.com"
port = 465

message = MIMEMultipart("alternative")
message["Subject"] = 'Dados de acesso - INFOPublic'
message["From"] = sender_email
message["To"] = receiver_email

texto, html = entrada_dados()

part1 = MIMEText(texto, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(srvSMTP, port, context=context) as server:
  server.login(sender_email, senha)
  server.sendmail(
                  sender_email, receiver_email, message.as_string()
  )
  print("E-mail enviado com sucesso!")

