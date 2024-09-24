message = input('Введите сообщение: ')
recipient = input('Введите адрес получателя: ')
def send_email(message, recipient, sender="university.help@gmail.com"):
    # print(message,recipient,sender)
    z =['.com','.ru','.net']
    for i in z:
        sim_1=recipient.find(i)
        if sim_1==-1:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
            break
        elif '@' not in recipient or '@' not in sender:
            print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
            break
        else:
            if recipient==sender:
                print('Невозможно отправить письмо самому себе')
                break
            elif sender == 'university.help@gmail.com':
                print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
                break
            elif sender != 'university.help@gmail.com':
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
                break
    else:
        print(message,recipient,sender)
send_email (message,recipient)

# send_email (message, recipient,sender='aisa@land.ru')
