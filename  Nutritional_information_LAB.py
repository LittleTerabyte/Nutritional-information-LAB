class FoodItem:
    def __init__(self, name = None, fat = 0.0, carbs = 0.0, protein = 0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
       
    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories
       
    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'   Fat: {self.fat:.2f} g')
        print(f'   Carbohydrates: {self.carbs:.2f} g')
        print(f'   Protein: {self.protein:.2f} g')

def page_brake():
    print()
    print("=" * 50)
    print()

if __name__ == "__main__":
    
    page_brake()
    # Shows a blank food item
    food_item1 = FoodItem()
   
    item_name = input("Enter food item name:\n").lower()
    amount_fat = float(input("Enter amount of fat (in grams):\n"))
    amount_carbs = float(input("Enter amount of carbohydrates (in grams):\n"))
    amount_protein = float(input("Enter amount of protein (in grams):\n"))
   
    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
    # Creates a food item with the given information
      
    num_servings = int(input("Enter number of servings:\n"))
    page_brake()
      
    food_item1.print_info()
    print(f'Number of calories for {num_servings} serving(s): {food_item1.get_calories(num_servings):.2f}')
                           
    print()
                           
    food_item2.print_info()
    print(f'Number of calories for {num_servings} serving(s): {food_item2.get_calories(num_servings):.2f}')
    page_brake()
    print("\nGoodbye\n")
