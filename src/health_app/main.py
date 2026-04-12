from .health import Health
from .data import save_records, load_records, get_statistics

def main():
    records = load_records()
    while True:
        print("\n--- Health App Menu ---")
        print("1. Add Health Record")
        print("2. View All Records")
        print("3. View Statistics")
        print("4. Save & Quit")
        
        choice = input("Select option: ")
        
        if choice == "1":
            try:
                name = input("Enter name: ")
                weight = float(input("Enter weight (kg): "))
                height = float(input("Enter height (m): "))
                r = Health(name, weight, height)
                records.append(r)
                save_records(records) 
                print(f"Added {r.name}: BMI {r.bmi} ({r.get_category()}) | Ideal: {r.get_ideal_weight()}kg | Advice: {r.get_health_advice()}")
            except ValueError:
                print("Invalid input, please try again")

        elif choice == "2":
            if not records:
                print("No records found.")
            for r in records:
                diff = round(r.weight_kg - r.get_ideal_weight(), 1)
                print(f"{r.name}: BMI {r.bmi} ({r.get_category()}) | Ideal Diff: {diff}kg")

        elif choice == "3":
            stats = get_statistics()
            print("\n--- Statistics ---")
            for key, value in stats.items():
                print(f"{key.replace('_', ' ').title()}: {value}")

        elif choice == "4":
            save_records(records)
            print("Final save complete. Goodbye!")
            break

if __name__ == "__main__":
    main()
