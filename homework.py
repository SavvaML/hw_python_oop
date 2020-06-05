import datetime as dt
from collections import namedtuple
Currency = namedtuple('Currency', 'rate name')
class Record:
    def __init__(self,amount,comment,date=''):
        self.amount = amount 
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
#Parent class
class Calculator:
    def __init__(self,limit):
        self.limit=limit
        self.records = []
    def add_record(self,record):
        self.records.append(record)
    def get_today_stats(self):
        today_count = 0
        for r in self.records:
            if r.date == dt.datetime.now().date():
                today_count += r.amount
        return today_count
    def get_week_stats(self):
        week_count = 0
        today=dt.date.today()
        week_ago = today - dt.timedelta(days=7)
        for r in self.records:
            if week_ago <= r.date <= today:
                week_count += r.amount
        return week_count
    def today_stats(self):
        return self.limit - self.get_today_stats()    


class CashCalculator(Calculator):
    USD_RATE = 68.40
    EURO_RATE = 77.35
    RUB_RATE = 1
    
    #CURRENCIES = {
     #       'usd': Currency(USD_RATE, 'USD'),
      #      'eur': Currency(EURO_RATE, 'Euro'),
       #     'rub': Currency(RUB_RATE, 'руб')
        #}

    #def conversion_rate(self, currency_2: str):
     #   return self.CURRENCIES[currency_2].rate

    def get_today_cash_remained(self, currency):
        CURRENCIES = {
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro'),
            'rub': (self.RUB_RATE, 'руб')
            }
        currency_name = CURRENCIES [currency][1]
        currency_rate = CURRENCIES [currency][0]
        #def conversion_rate(self, currency_2: str):
       #     return self.CURRENCIES[currency_2].rate
        today_stat = super().today_stats()
        #stat = today_stat / self.conversion_rate(currency)
        #currency_name = self.CURRENCIES[currency].name
        stat = round(today_stat / currency_rate, 2)
        if stat == 0:
            return ('Денег нет, держись')
        elif stat > 0:
            #stat_rounded = round(stat, 2)
            return(f'На сегодня осталось {stat} {currency_name}')
        elif stat < 0:
            debt = abs(stat)
            return(f'Денег нет, держись: твой долг - {debt} {currency_name}')



class CaloriesCalculator (Calculator):
    
    def get_calories_remained(self):
        stats = super().today_stats()
        if stats > 0:
            return(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {stats} кКал')
        else:
            return('Хватит есть!')



