def mail_check(mail):
    for i in mail:
        if i != "@":
            at = False
            continue
        else:
            at = True
    lst = mail.split(".")
    for j in lst:
        if j == "com" or j == "ru" or j == "net":
            at = True
            break
        else:
            at = False
    return at


def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if mail_check(recipient) == False or mail_check(sender) == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи',
           'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')


