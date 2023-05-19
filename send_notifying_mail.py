import os
import smtplib
from email.message import EmailMessage

mail_user = os.getenv('USER_GMAIL')
mail_password = os.getenv('PASSWORD_GMAIL')

def send_notifying_mail(mail_user: str = "", mail_password: str = "") -> None:

  msg = EmailMessage()
  # Contenido
  msg['From']= mail_user
  msg['To']= mail_user
  msg['Subject']= "Probando mandar mails!"
  cuerpo_del_mail = 'Este es un mail enviado con Python en la clase! =D'
  msg.set_content(cuerpo_del_mail)

  
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()


  server.login(mail_user, mail_password)

  # enviar
  server.send_message(msg)
  server.quit();
  

if __name__ == "__main__":
  send_notifying_mail(mail_user, mail_password)

