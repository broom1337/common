
class Wallet:

    def __init__(self, currency: str, name: str, payment_system: str, balance: int):
        self.balance = balance
        self.currency = currency
        self.name = name
        self.payment_system = payment_system
        if self.currency not in ("USD", "EUR", "RUB", "BTC", "ETH"):
            raise ValueError("Несуществующая валюта")

    def info_user(self):
        print(f"Кошелек: {self.name}")
        print(f"Текущий счет: {self.balance} {self.currency}")

    def get_money(self):
        print('Пополнение баланса:')
        add = int(input("Сумма пополнения: "))
        self.balance += add
        print('Успешное пополнение счета')
    
    def spend_money(self):
        print('Оплата')
        throw = int(input("Сумма платежа: "))
        if throw < self.balance:
            self.balance -= throw
            print('Успешная оплата')
        else:
            print('Недостаточно средств для оплаты')

    def delete_accaunt(self):
        print('Вы уверены, что хотите удалить счет? (д/н)')
        answer = input()
        if answer == 'д':
            del self.balance
            del self.currency
            del self.name
            del self.payment_system
            print('Счет удален.')
            exit()
        elif answer == 'н':
            pass
        else:
            print ('Vallue Error')

class CryptWallet(Wallet):
    def __init__(self, coin: str, currency: str, name: str, payment_system: str, balance: int):
        self.coin = coin
        super().__init__(currency, name, payment_system, balance)

    def info_dollars(self):
        print('Баланс в долларах:')
        if self.currency == 'BTC':
            print(f'{self.coin*72000} USD')
        else:
            print(f'{self.coin*3500} USD')
    
    def get_money(self):
        print('Пополнение баланса:')
        add = int(input("Сумма пополнения: "))
        self.coin += add
        print('Успешное пополнение счета')

    def info_user(self):
        print(f"Кошелек: {self.name}")
        print(f"Счет: {self.balance} USD")
        print(f"{self.coin} {self.currency}")

    def delete_accaunt(self):
        print('Вы уверены, что хотите удалить счет? (д/н)')
        answer = input()
        if answer == 'д':
            del self.balance
            del self.currency
            del self.name
            del self.payment_system
            del self.coin
            print('Счет удален.')
            exit()
        elif answer == 'н':
            pass
        else:
            print ('Vallue Error')

    def transaction(self):
        if self.currency == 'BTC':
            self.balance = self.coin*72000
            self.coin = 0
        else:
            self.balance = self.coin*3500
            self.coin = 0
        print("Перевод успешно выполнен")


def wallet_menu():
    print("""
          1. Пополнение баланса
          2. Оплата
          3. Инфо
          4. Удаление счета

          Выберите операцию(введите число)
          """)
    act = int(input())
    if act == 1:
        w.get_money()
    elif act == 2:
        w.spend_money()
    elif act == 3:
        w.info_user()
    elif act == 4:
        w.delete_accaunt()
    else:
        print('ValueError')
    print("Вернуться в меню (д/н)")
    r = input()
    if r == 'д':
        wallet_menu()
    elif r == 'н':
        exit()
    else:
        print('ValueError')
        exit()

def cwallet_menu():
    print("""
          1. Пополнение баланса
          2. Оплата
          3. Инфо
          4. Удаление счета
          5. Баланс в долларах
          6. Перевод с одного кошелька на другой

          Выберите операцию(введите число)
          """)
    act = int(input())
    if act == 1:
        cw.get_money()
    elif act == 2:
        cw.spend_money()
    elif act == 3:
        cw.info_user()
    elif act == 4:
        cw.delete_accaunt()
    elif act == 5:
        cw.info_dollars()
    elif act == 6:
        cw.transaction()
    else:
        print('ValueError')
    print("Вернуться в меню (д/н)")
    r = input()
    if r == 'д':
        cwallet_menu()
    elif r == 'н':
        exit()
    else:
        print('ValueError')
        exit()



name = (input('Введите название кошелька: '))
cur = (input('Введите используемую валюту: '))
ps = (input('Выберите платежную систему: '))

w = Wallet(cur, name, ps, balance=0)
cw = CryptWallet(0,cur,name,ps,balance=0)

print(f""" 
        Кошелек {w.name}

        Используемая платежная система: {w.payment_system}
          """)
if cur != 'BTC' and cur != 'ETH':
    wallet_menu()
else:
    cwallet_menu()
    