class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        
    def calculate_bmi(self):
        return (self.weight) / (self.height**2) * 703
        
def main():
    x = int(input("How much do you weigh, in pounds "))
    y = int(input("What is your height in inches? "))
    
    my_bmi = BMI(x, y)
    bmi = my_bmi.calculate_bmi()
    print(bmi)
    
main()