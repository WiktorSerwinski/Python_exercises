import sqlite3

# Połączenie z bazą danych (lub utworzenie nowej, jeśli nie istnieje)
conn = sqlite3.connect("exchange_rates.db")
cursor = conn.cursor()

# Tworzenie tabeli exchange_rates
cursor.execute('''
    CREATE TABLE IF NOT EXISTS exchange_rates (
        date TEXT,
        currency TEXT,
        rate_to_PLN REAL
    )
''')

# Wstawianie przykładowych danych do exchange_rates
cursor.executemany('''
    INSERT INTO exchange_rates (date, currency, rate_to_PLN)
    VALUES (?, ?, ?)
''', [
    ("2024-02-26", "EUR", 4.50),
    ("2024-02-25", "USD", 4.20),
    ("2024-02-24", "GBP", 5.00)
])

# Zapisanie zmian i zamknięcie połączenia
conn.commit()
conn.close()

print("Baza danych exchange_rates.db została utworzona i wypełniona danymi!")
