from datetime import datetime
from core.utils import format_currency

class ReportService:
    def __init__(self, db, predictor):
        self.db = db
        self.predictor = predictor

    def generate_monthly_report(self, items):
        filename = f"report_{datetime.now().strftime('%Y_%m')}.txt"
        with open(filename, "w") as f:
            total_value = 0
            for _, name, qty, price in items:
                predicted = self.predictor.predict_demand(name, qty)
                f.write(f"{name:15} | Qty: {qty:3} | Price: {format_currency(price)} | Predicted Demand: {predicted}\n")
                total_value += price * qty
            f.write(f"\nTotal Inventory Value: {format_currency(total_value)}\n")
        print(f"✅ Report generated: {filename}")
