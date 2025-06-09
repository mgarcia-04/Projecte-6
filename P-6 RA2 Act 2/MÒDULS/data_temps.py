from datetime import datetime

ara = datetime.now()
print("Data actual:", ara.strftime("%d/%m/%Y %H:%M"))

futur = datetime(2025, 12, 25)
dies_restants = (futur - ara).days
print(f"Dies fins Nadal: {dies_restants}")
