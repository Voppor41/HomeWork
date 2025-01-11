def send_email(message, recipent: str, *, sender="university.help@gmail.com"):
    if ('@' in recipent) and ('.com' in recipent or '.ru' in recipent or '.net' in recipent):
        if sender == recipent:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipent}")
        else:
            if "@" in sender and (".com" in sender or ".ru" in sender or ".net" in sender):
                if sender == recipent:
                    print("Нельзя отправить письмо самому себе!")
                else:
                    print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipent}.")
            else:
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipent}")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipent}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
