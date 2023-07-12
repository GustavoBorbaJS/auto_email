import smtplib

def enviar_email(destinatario, assunto, corpo):
    remetente = 'seu_email@gmail.com'
    senha = 'sua_senha'

    mensagem = f'Subject: {assunto}\n\n{corpo}'

    with smtplib.SMTP('smtp.gmail.com', 587) as servidor_smtp:
        servidor_smtp.starttls()
        servidor_smtp.login(remetente, senha)
        servidor_smtp.sendmail(remetente, destinatario, mensagem)

# Exemplo de uso
destinatario = 'destinatario@email.com'
assunto = 'Assunto do email'
corpo = 'Corpo do email'

enviar_email(destinatario, assunto, corpo)
