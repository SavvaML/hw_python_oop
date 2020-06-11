import datetime as dt
DATE = dt.date.today()
class Record:
    
    def __init__(self,amount,comment,date=None):
        self.amount = amount 
        self.comment = comment
        if date == None:
            self.date = DATE
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class Calculator:
    
    def __init__(self,limit):
        self.limit=limit
        self.records = []
    
    def add_record(self,record):
        self.records.append(record)
    
    def get_today_stats(self):
        return sum(record.amount 
            for record in self.records 
                if record.date == DATE
            )
        
    
    def get_week_stats(self):
        week_ago = DATE - dt.timedelta(days=7)
        return sum(record.amount
            for record in self.records
                if week_ago <= record.date <= DATE
            )
        
    def today_stats(self):
        return self.limit - self.get_today_stats()    


class CashCalculator(Calculator):
    USD_RATE = 68.40
    EURO_RATE = 77.35
    RUB_RATE = 1
    

    def get_today_cash_remained(self, currency=None):
        today_stat = self.today_stats()
        if today_stat == 0:
            return ('Денег нет, держись')
        CURRENCIES = {
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro'),
            'rub': (self.RUB_RATE, 'руб')
            }
        if currency not in CURRENCIES:
            raise ValueError ('Хозяин,таких денег нет в нашем царстве')     
        currency=CURRENCIES[currency]        
        first_currency,second_currency=currency
        stat = round(today_stat / first_currency, 2)
        if stat > 0:
            return(f'На сегодня осталось {stat} {second_currency}')
        if stat < 0:
            debt = abs(stat)
            return(f'Денег нет, держись: твой долг - {debt} {second_currency}')



class CaloriesCalculator (Calculator):
    
    def get_calories_remained(self):
        stats = self.today_stats()
        if stats <= 0:
            return('Хватит есть!')
        return("Сегодня можно съесть что-нибудь ещё, "
            f"но с общей калорийностью не более {stats} кКал"
          )
        
            
cash_calculator = CashCalculator(1000)
        
