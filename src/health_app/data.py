import json
import os
from collections import Counter
from .health import Health

def save_records(records: list[Health], filename="health_records.json"):
    data = [
        {"name": r.name, "weight_kg": r.weight_kg, "height_m": r.height_m, "bmi": r.bmi}
        for r in records
    ]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_records(filename="health_records.json") -> list[Health]:
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            # Zamieniamy dane z JSON z powrotem na obiekty klasy Health
            return [Health(d["name"], d["weight_kg"], d["height_m"]) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def get_statistics(filename="health_records.json") -> dict:
    records = load_records(filename)
    if not records:
        return {"total_records": 0, "avg_bmi": 0.0, "most_common_category": "None", "category_distribution": {}}
    
    bmis = [r.bmi for r in records]
    categories = [r.get_category() for r in records]
    
    return {
        "total_records": len(records),
        "avg_bmi": round(sum(bmis) / len(bmis), 2),
        "most_common_category": Counter(categories).most_common(1)[0][0],
        "category_distribution": dict(Counter(categories))
    }