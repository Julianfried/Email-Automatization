import os
import smtplib
from email.message import EmailMessage


def send_notifying_mail(mail_user: str = "", mail_password: str = "") -> None:
  msg = EmailMessage()
  user_gmail = os.getenv(USER_GMAIL)
  password_gmail = os.getenv(PASSWORD_GMAIL)

  # Contenido
  msg['From']= user_gmail
  msg['To']= user_gmail
  msg['Subject']= "Probando mandar mails!"
  cuerpo_del_mail = 'Este es un mail enviado con Python en la clase! =D'
  msg.set_content(cuerpo_del_mail)

  
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()


  server.login(user_gmail, password_gmail)

  # enviar
  server.send_message(msg)
  server.quit();
  
send_notifying_mail(user_gmail, password_gmail)

if __name__ == "__main__":
  send_notifying_mail(user_gmail, password_gmail)
