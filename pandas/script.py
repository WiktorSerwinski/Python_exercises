import pandas as pd
import sqlite3

try:
    #  Połączenie z bazą SQLite
    conn = sqlite3.connect("pandas/exchange_rates.db")
    exchange_rates = pd.read_sql("SELECT * FROM exchange_rates", conn)
    transactions = pd.read_csv("pandas/transactions.csv")
    conn.close()

    if transactions.empty:
        raise ValueError("Brak danych w tabeli transactions!")
    if exchange_rates.empty:
        raise ValueError("Brak danych w tabeli exchange_rates!")

    #  Połączenie danych - SQL JOIN (odpowiednik LEFT JOIN)
    df = transactions.merge(
        exchange_rates, on=["currency", "date"], how="left")

    #  Uzupełnianie brakujących kursów walut (najbliższy wcześniejszy kurs)
    df["rate_to_PLN"] = df.groupby("currency")["rate_to_PLN"].ffill()

    #  Sprawdzenie, czy nadal są brakujące wartości kursów walut
    missing_rates = df[df["rate_to_PLN"].isna()]
    if not missing_rates.empty:
        print("Ostrzeżenie! Nie znaleziono kursu wymiany dla następujących transakcji:")
        print(missing_rates)

    #  Obliczenie wartości transakcji w PLN
    df["amount_PLN"] = df["amount"] * df["rate_to_PLN"]

    #  Grupowanie po klientach i sumowanie transakcji
    df_grouped = df.groupby("customer_id")["amount_PLN"].sum().reset_index()

    print(df)

    #  Zaokrąglenie wartości do 2 miejsc po przecinku
    df_grouped["amount_PLN"] = df_grouped["amount_PLN"].round(2)

    #  Znalezienie klienta z największą sumą transakcji
    max_customer = df_grouped.loc[df_grouped["amount_PLN"].idxmax()]

    print(df_grouped)
    print(
        f"Najlepszy klient: {max_customer['customer_id']} z sumą {max_customer['amount_PLN']} PLN")

    #  Zapis wyników do pliku CSV
    df_grouped.to_csv("pandas/customer_sums.csv", index=False)
    print("Wyniki zostały zapisane do customer_sums.csv'.")

except Exception as e:
    print(f"Wystąpił błąd: {e}")
