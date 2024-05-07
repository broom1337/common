


class CardDeck:

    def __init__(self, rank: list = ['2','3','4','5',
        '6','7','8','9','10','Валет','Дама', 'Король','Туз'], 
        suit: list = ['Пик','Треф','Бубен','Черви'], number: int = 1):
        self.number = number
        self.suit = suit
        self.rank = rank
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number > 52:
            raise StopIteration
        card = f"{self.rank[(self.number - 1) % 13]} {self.suit[(self.number - 1) // 13]}"
        self.number += 1
        return card

cd = CardDeck()

try:
    while True:
        print(next(cd))
except StopIteration:
    pass