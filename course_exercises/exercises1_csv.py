import pandas as pd
import os
try:
    # Pobranie katalogu, w którym jest skrypt
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(BASE_DIR,"transactions.csv")
     
    
    # Próba wczytania pliku
    
    df = pd.read_csv(filename)
    
    print("Plik został poprawnie wczytany!")
    # Sumowanie wartości transakcji dla każdego klienta
    df_grouped = df.groupby("customer_id")["amount"].sum().reset_index()

    # Wyświetlenie wyników w terminalu
    print(df_grouped)

    max_ammount_row = df_grouped[df_grouped["amount"] == df_grouped["amount"].max()]

    max_customer_id = max_ammount_row["customer_id"].values[0]

    max_customer_amount = max_ammount_row["amount"].values[0]


    print(f"Top customer: {max_customer_id} with total {max_customer_amount}")

    df_grouped.rename(columns={"amount": "total_amount"}, inplace=True)

    df_grouped.to_csv("course_exercises\\customer_sums.csv",index=False)



except FileNotFoundError:
    # Obsługa braku pliku
    print(f"Błąd: Plik '{filename}' nie istnieje. Sprawdź ścieżkę lub utwórz plik.")
    df = pd.DataFrame()  # Tworzymy pusty DataFrame, aby uniknąć dalszych błędów