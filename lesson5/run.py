"""
    Classes...


Operation :=  OPERAND_A OPERATOR OPERAND_B -> RESULT
Opeartion :=   int(4)      *        int(2) ->  16
"""

from typing import Any

CURRENCY_RATES = {
    "USD": 1.0,
    "CHF": 0.9,
    "EUR": 1.1,
}

class Price:
    def __init__(self, value: int, currency: str):
        if currency not in CURRENCY_RATES:
            raise ValueError(f"Unsupported currency: {currency}")
        self.value: int = value
        self.currency: str = currency

    def __str__(self) -> str:
        return f"Price: {self.value} {self.currency}"

    def convert(self, to: str) -> "Price":
        if to not in CURRENCY_RATES:
            raise ValueError(f"Unsupported currency: {to}")
        value_in_chf = self.value / CURRENCY_RATES[self.currency]
        converted_value = value_in_chf * CURRENCY_RATES[to]
        return Price(value=int(round(converted_value)), currency=to)

    def __add__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operation only with Price objects")
        if self.currency != other.currency:
            other_converted = other.convert(to=self.currency)
        else:
            other_converted = other
        return Price(value=self.value + other_converted.value, currency=self.currency)

    def __sub__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operation only with Price objects")
        if self.currency != other.currency:
            other_converted = other.convert(to=self.currency)
        else:
            other_converted = other
        return Price(value=self.value - other_converted.value, currency=self.currency)

phone = Price(value=200, currency="USD")
tablet = Price(value=400, currency="USD")

total: Price = phone + tablet
print(total)

watch = Price(value=500, currency="EUR")
print(phone + watch)

from functools import wraps

users = {
    "admin": "1234",
    "user1": "password",
}

auth_cache = {}

def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = None
        if "authorized_user" in auth_cache:
            username = auth_cache["authorized_user"]
        else:
            while True:
                username = input("Enter username: ")
                password = input("Enter password: ")
                if username in users and users[username] == password:
                    print("Authorization successful!")
                    auth_cache["authorized_user"] = username
                    break
                else:
                    print("Invalid username or password. Try again.")

        return func(*args, **kwargs)
    return wrapper

@auth
def function1():
    print("Executing command...")

if __name__ == "__main__":
    function1()
