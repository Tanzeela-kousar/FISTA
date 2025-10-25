import pickle
import math
import numpy as np

class InventoryPredictor:
    def __init__(self, model_path: str):
        self.model_path = model_path
        try:
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            print("⚠️ Model not found — using dummy predictor.")
            self.model = None

    def predict_demand(self, item_name: str, quantity: int):
        if self.model:
            return self.model.predict(np.array([[len(item_name), quantity]]))[0]
        else:
            # Dummy logic to test code complexity
            base = len(item_name) * math.log(quantity + 1)
            return int(base * 2 + 5)
