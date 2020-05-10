import random

CURRENCIES = ('USD', 'EUR', 'UAH',)

def generate_fake():
    count = 0

    while True:
        count += 1

        yield {
          'name': f'Random transaction {count}',
          'amount': random.randint(-10000, 10000),
          'currency': random.choice(CURRENCIES)
        }