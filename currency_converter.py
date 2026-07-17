import requests

def get_exchange_rates():
    """Fetches real-time exchange rates based on USD."""
    url = "https://open.er-api.com/v6/latest/USD"
    try:
        response = requests.get(url, timeout=5)
        # Raise an exception if the request was unsuccessful (e.g., 404 or 500 error)
        response.raise_for_status() 
        data = response.json()
        return data["rates"]
    except requests.exceptions.RequestException:
        print("Error: Unable to connect to the exchange rate service. Check your internet connection.")
        return None

def convert_currency():
    print("=== Real-Time Currency Converter ===")
    if else:
        print("Fetching exchange rates...")
    rates = get_exchange_rates()
    
    # If the API call failed, exit early
    if not rates:
        return

    while True:
        try:
            # 1. Handle Amount Input
            amount_input = input("\nEnter the amount to convert (or 'q' to quit): ").strip()
            if amount_input.lower() == 'q':
                print("Thank you for using the Currency Converter! Goodbye.")
                break
                
            amount = float(amount_input)
            if amount < 0:
                print("Amount cannot be negative. Please try again.")
                continue

            # 2. Handle Base Currency Input
            from_currency = input("From Currency (e.g., USD, EUR, GBP): ").strip().upper()
            if from_currency not in rates:
                raise KeyError("Invalid 'From' currency code.")

            # 3. Handle Target Currency Input
            to_currency = input("To Currency (e.g., USD, EUR, GBP): ").strip().upper()
            if to_currency not in rates:
                raise KeyError("Invalid 'To' currency code.")

            # 4. Math/Conversion Calculation
            # Convert the amount to USD first, then to the target currency
            amount_in_usd = amount / rates[from_currency]
            converted_amount = amount_in_usd * rates[to_currency]

            print(f"\n✨ Success: {amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}")
            
        except ValueError:
            print("❌ Input Error: Please enter a valid number for the amount.")
        except KeyError as e:
            print(f"❌ Currency Error: {e.args[0]} Please use valid 3-letter codes.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    convert_currency()