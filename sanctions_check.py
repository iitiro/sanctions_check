
import pandas as pd

# Завантаження даних
df_individuals = pd.read_excel("./Code/!sanctions/04.03.2025 individual subjects.xlsx", sheet_name="Individual")
df_legal = pd.read_excel("./Code/!sanctions/04.03.2025 legal subjects.xlsx", sheet_name="Legal")

def search_individuals():
    while True:
        surname = input("Введіть прізвище: ").strip()
        name = input("Введіть ім’я: ").strip()
        filtered = df_individuals[df_individuals['name'].str.contains(surname, case=False, na=False)]
        filtered = filtered[filtered['name'].str.contains(name, case=False, na=False)]

        if filtered.empty:
            print("Осіб не знайдено.")
        else:
            print("\nЗнайдено:")
            print(filtered[['name', 'status', 'birthdate', 'citizenship', 'sanctions_term', 'sanctions_end_date', 'decree_date']].to_string(index=False))

        next_action = input("\nЩо далі? (1 — новий пошук, 2 — перейти до юридичних осіб, 3 — вихід): ").strip()
        if next_action == "1":
            continue
        elif next_action == "2":
            return "switch"
        elif next_action == "3":
            return "exit"
        else:
            print("Невірний вибір, вихід.")
            return "exit"

def search_legal():
    while True:
        keyword = input("Введіть ключове слово в назві юридичної особи: ").strip()
        matches = df_legal[df_legal['name'].str.contains(keyword, case=False, na=False)]

        if matches.empty:
            print("Юридичних осіб не знайдено.")
        elif len(matches) == 1:
            print("\nЗнайдено одну юридичну особу:")
            print(matches[['name', 'status', 'sanctions_term', 'sanctions_end_date', 'decree_date']].to_string(index=False))
        else:
            print("\nЗнайдено кілька варіантів:")
            for i, name in enumerate(matches['name'], start=1):
                print(f"{i}. {name}")
            choice = input("Оберіть номер потрібної організації: ")
            try:
                idx = int(choice) - 1
                selected = matches.iloc[idx]
                print("\nІнформація про вибрану юридичну особу:")
                print(selected[['name', 'status', 'sanctions_term', 'sanctions_end_date', 'decree_date']].to_string())
            except:
                print("Некоректний вибір.")

        next_action = input("\nЩо далі? (1 — новий пошук, 2 — перейти до фізичних осіб, 3 — вихід): ").strip()
        if next_action == "1":
            continue
        elif next_action == "2":
            return "switch"
        elif next_action == "3":
            return "exit"
        else:
            print("Невірний вибір, вихід.")
            return "exit"

def main():
    current_mode = None
    while current_mode not in ["1", "2"]:
        print("Оберіть тип перевірки:")
        print("1. Фізичні особи")
        print("2. Юридичні особи")
        current_mode = input("Ваш вибір (1 або 2): ").strip()

    while True:
        if current_mode == "1":
            result = search_individuals()
            if result == "switch":
                current_mode = "2"
            elif result == "exit":
                break
        elif current_mode == "2":
            result = search_legal()
            if result == "switch":
                current_mode = "1"
            elif result == "exit":
                break

if __name__ == "__main__":
    main()
