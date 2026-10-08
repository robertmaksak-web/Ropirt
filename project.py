import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from collections import defaultdict


DATA_FILE = "data.json"


# Завантаження даних
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return {
        "income": [],
        "expenses": []
    }


# Збереження даних
def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


data = load_data()


# Оновлення інформації на екрані
def update_info():
    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    balance = total_income - total_expenses

    income_label.config(text=f"Зароблено: {total_income:.2f} грн")
    expenses_label.config(text=f"Витрачено: {total_expenses:.2f} грн")
    balance_label.config(text=f"Залишок: {balance:.2f} грн")


# Додавання доходу
def add_income():
    amount = simpledialog.askfloat(
        "Новий дохід",
        "Введіть суму доходу:"
    )

    if amount is None:
        return

    if amount <= 0:
        messagebox.showerror("Помилка", "Сума повинна бути більшою за 0.")
        return

    source = simpledialog.askstring(
        "Джерело доходу",
        "Звідки отримані гроші?"
    )

    if not source:
        source = "Інше"

    data["income"].append({
        "amount": amount,
        "source": source
    })

    save_data()
    update_info()

    messagebox.showinfo(
        "Успішно",
        f"Додано дохід: {amount:.2f} грн"
    )


# Додавання витрати
def add_expense():
    amount = simpledialog.askfloat(
        "Нова витрата",
        "Введіть суму витрати:"
    )

    if amount is None:
        return

    if amount <= 0:
        messagebox.showerror("Помилка", "Сума повинна бути більшою за 0.")
        return

    category = simpledialog.askstring(
        "Категорія",
        "На що витратили гроші?\n"
        "Наприклад: їжа, транспорт, ігри, одяг"
    )

    if not category:
        category = "Інше"

    data["expenses"].append({
        "amount": amount,
        "category": category
    })

    save_data()
    update_info()

    messagebox.showinfo(
        "Успішно",
        f"Додано витрату: {amount:.2f} грн"
    )


# Історія операцій
def show_history():
    window = tk.Toplevel(root)
    window.title("Історія операцій")
    window.geometry("500x450")

    text = tk.Text(window, font=("Arial", 12))
    text.pack(fill="both", expand=True, padx=10, pady=10)

    text.insert("end", "========== ДОХОДИ ==========\n\n")

    if data["income"]:
        for item in data["income"]:
            text.insert(
                "end",
                f"+ {item['amount']:.2f} грн — {item['source']}\n"
            )
    else:
        text.insert("end", "Доходів поки немає.\n")

    text.insert("end", "\n========== ВИТРАТИ ==========\n\n")

    if data["expenses"]:
        for item in data["expenses"]:
            text.insert(
                "end",
                f"- {item['amount']:.2f} грн — {item['category']}\n"
            )
    else:
        text.insert("end", "Витрат поки немає.\n")

    text.config(state="disabled")


# Статистика
def show_statistics():
    expenses_by_category = defaultdict(float)

    for item in data["expenses"]:
        expenses_by_category[item["category"]] += item["amount"]

    window = tk.Toplevel(root)
    window.title("Статистика")
    window.geometry("500x400")

    title = tk.Label(
        window,
        text="📊 Статистика витрат",
        font=("Arial", 18, "bold")
    )
    title.pack(pady=15)

    if not expenses_by_category:
        tk.Label(
            window,
            text="Витрат поки немає.",
            font=("Arial", 13)
        ).pack(pady=20)
        return

    for category, amount in sorted(
        expenses_by_category.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        tk.Label(
            window,
            text=f"{category}: {amount:.2f} грн",
            font=("Arial", 13)
        ).pack(pady=5)


# Головне вікно
root = tk.Tk()
root.title("💰 Мій фінансовий менеджер")
root.geometry("600x550")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="💰 МІЙ ФІНАНСОВИЙ МЕНЕДЖЕР",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=25)


income_label = tk.Label(
    root,
    text="Зароблено: 0.00 грн",
    font=("Arial", 16)
)
income_label.pack(pady=10)


expenses_label = tk.Label(
    root,
    text="Витрачено: 0.00 грн",
    font=("Arial", 16)
)
expenses_label.pack(pady=10)


balance_label = tk.Label(
    root,
    text="Залишок: 0.00 грн",
    font=("Arial", 18, "bold")
)
balance_label.pack(pady=15)


button_frame = tk.Frame(root)
button_frame.pack(pady=20)


income_button = tk.Button(
    button_frame,
    text="💵 Додати дохід",
    font=("Arial", 13),
    width=20,
    command=add_income
)
income_button.grid(row=0, column=0, padx=10, pady=10)


expense_button = tk.Button(
    button_frame,
    text="💸 Додати витрату",
    font=("Arial", 13),
    width=20,
    command=add_expense
)
expense_button.grid(row=1, column=0, padx=10, pady=10)


history_button = tk.Button(
    button_frame,
    text="📋 Історія операцій",
    font=("Arial", 13),
    width=20,
    command=show_history
)
history_button.grid(row=2, column=0, padx=10, pady=10)


statistics_button = tk.Button(
    button_frame,
    text="📊 Статистика",
    font=("Arial", 13),
    width=20,
    command=show_statistics
)
statistics_button.grid(row=3, column=0, padx=10, pady=10)


update_info()

root.mainloop()