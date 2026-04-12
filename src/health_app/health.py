class Health:
    def __init__(self, name: str, weight_kg: float, height_m: float):
        
        if not name.strip() or weight_kg <= 0 or height_m <= 0:
            raise ValueError("Invalid input, please try again")
        
        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m
       
        self.bmi = round(weight_kg / (height_m ** 2), 2)

    def get_category(self) -> str:
        if self.bmi < 18.5: return "Underweight"
        if self.bmi < 25: return "Normal"
        if self.bmi < 30: return "Overweight"
        return "Obese"

    def get_health_advice(self) -> str:
        cat = self.get_category()
        advice = {
            "Underweight": "Try to increase your caloric intake. Focus on nutrient-dense foods and regular meals.",
            "Normal": "You are in a great shape! Maintain a balanced diet and keep staying active.",
            "Overweight": "Consider a slight reduction in calories. Small increases in daily movement can make a big difference.",
            "Obese": "It is recommended to consult a doctor. Focus on sustainable lifestyle changes rather than quick diets."
        }
        return advice[cat]

    def get_ideal_weight(self) -> float:
      
        return round(22 * (self.height_m ** 2), 1)
