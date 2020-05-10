def is_fake(transaction: dict) -> bool:
    amount = transaction.get('amount')

    return amount < -5000 or amount > 5000