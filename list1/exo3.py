# Predefined exchange rates
usd_rate = 0.0074   # 1 DZD = 0.0074 USD
eur_rate = 0.0030   # 1 DZD = 0.0068 EUR
gbp_rate = 0.0058   # 1 DZD = 0.0058 GBP

dzd = float(input("Enter amount in DZD: "))

usd = dzd * usd_rate
eur = dzd * eur_rate
gbp = dzd * gbp_rate

print("\nConverted Amounts:")
print(f"USD: {usd:.3f}")
print(f"EUR: {eur:.2f}")
print(f"GBP: {gbp:.2f}")

