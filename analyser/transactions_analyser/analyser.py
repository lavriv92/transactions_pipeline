def is_fake(transaction):
    amount = transaction.get('amount')

    return amount > -5000 and amount < 5000