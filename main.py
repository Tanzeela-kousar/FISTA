from core.database import Database
from core.ai_engine import InventoryPredictor
from services.report_service import ReportService

def main():
    db = Database("sqlite:///inventory.db")
    model = InventoryPredictor("models/inventory_model.pkl")
    report_service = ReportService(db, model)

    print("🔄 Loading inventory data...")
    items = db.fetch_items()
    print(f"Loaded {len(items)} items.")

    print("📈 Generating report...")
    report_service.generate_monthly_report(items)

if __name__ == "__main__":
    main()
