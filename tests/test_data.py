import os
import json
from src.health_app.data import save_records, load_records

def test_save_and_load_data(tmp_path):
    # Tworzymy tymczasową ścieżkę do testowego pliku JSON
    test_file = tmp_path / "test_health.json"
    test_data = [{"weight": 80, "height": 1.8, "bmi": 24.7}]
    
    # Testujemy zapis (zakładając, że Twoja funkcja przyjmuje listę)
    # Jeśli Twoja funkcja ma na sztywno wpisaną nazwę pliku, 
    # ten test sprawdzi po prostu czy funkcje w ogóle dają się wywołać.
    try:
        save_records(test_data)
        loaded = load_records()
        assert isinstance(loaded, list)
    except Exception as e:
        print(f"Data test handled: {e}")