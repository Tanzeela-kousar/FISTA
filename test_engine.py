from core.ai_engine import InventoryPredictor

def test_predictor_basic():
    predictor = InventoryPredictor("nonexistent.pkl")
    assert predictor.predict_demand("Apple", 10) > 0
