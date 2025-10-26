import logging
from core.database import Database
from core.ai_engine import InventoryPredictor
from services.report_service import ReportService

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main() -> None:
    logging.info("Starting main application...")
    db = Database("sqlite:///inventory.db")
    model = InventoryPredictor("models/inventory_model.pkl")
    report_service = ReportService(db, model)

    logging.info("Loading inventory data...")
    items = db.fetch_items()
    logging.info(f"Loaded {len(items)} items.")

    logging.info("Generating report...")
    report_service.generate_monthly_report(items)
    logging.info("Report generation completed.")

if __name__ == "__main__":
    main()