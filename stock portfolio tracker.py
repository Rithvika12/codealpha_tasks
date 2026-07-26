import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("portfolio_data.json")


def load_portfolio():
    if not DATA_FILE.exists():
        return {}
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_portfolio(portfolio):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(portfolio, file, indent=2)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def add_stock(portfolio):
    symbol = input("Enter stock symbol: ").strip().upper()
    if not symbol:
        print("Symbol cannot be empty.")
        return

    quantity = get_float("Enter quantity: ")
    buy_price = get_float("Enter buy price per share: ")
    current_price = get_float("Enter current price per share: ")

    if symbol in portfolio:
        portfolio[symbol]["quantity"] += quantity
        portfolio[symbol]["buy_price"] = ((portfolio[symbol]["quantity"] - quantity) * portfolio[symbol]["buy_price"] + quantity * buy_price) / portfolio[symbol]["quantity"]
        portfolio[symbol]["current_price"] = current_price
    else:
        portfolio[symbol] = {
            "quantity": quantity,
            "buy_price": buy_price,
            "current_price": current_price,
        }

    save_portfolio(portfolio)
    print(f"Added/updated {symbol}.")


def view_portfolio(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\nCurrent portfolio:")
    for symbol, data in portfolio.items():
        quantity = data["quantity"]
        buy_price = data["buy_price"]
        current_price = data["current_price"]
        invested = quantity * buy_price
        current_value = quantity * current_price
        gain_loss = current_value - invested
        print(
            f"{symbol}: Qty={quantity}, Buy={buy_price:.2f}, Current={current_price:.2f}, "
            f"Invested={invested:.2f}, Value={current_value:.2f}, Gain/Loss={gain_loss:.2f}"
        )


def update_stock(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
        return

    symbol = input("Enter stock symbol to update: ").strip().upper()
    if symbol not in portfolio:
        print("Stock not found.")
        return

    portfolio[symbol]["current_price"] = get_float("Enter new current price per share: ")
    save_portfolio(portfolio)
    print(f"Updated {symbol}.")


def remove_stock(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
        return

    symbol = input("Enter stock symbol to remove: ").strip().upper()
    if symbol in portfolio:
        del portfolio[symbol]
        save_portfolio(portfolio)
        print(f"Removed {symbol}.")
    else:
        print("Stock not found.")


def show_summary(portfolio):
    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_invested = 0
    total_value = 0
    for data in portfolio.values():
        total_invested += data["quantity"] * data["buy_price"]
        total_value += data["quantity"] * data["current_price"]

    print(f"\nTotal invested: {total_invested:.2f}")
    print(f"Total current value: {total_value:.2f}")
    print(f"Overall gain/loss: {total_value - total_invested:.2f}")


def main():
    portfolio = load_portfolio()
    print("Welcome to the Stock Portfolio Tracker!")

    while True:
        print("\n1. Add stock")
        print("2. View portfolio")
        print("3. Update current price")
        print("4. Remove stock")
        print("5. Show summary")
        print("6. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_stock(portfolio)
        elif choice == "2":
            view_portfolio(portfolio)
        elif choice == "3":
            update_stock(portfolio)
        elif choice == "4":
            remove_stock(portfolio)
        elif choice == "5":
            show_summary(portfolio)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
