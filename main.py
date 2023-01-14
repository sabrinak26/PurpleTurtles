# Team: PurpleTurtles
# Contributors: Sabrina Ke, Mya Naja Zahra, Hailey Mitsubata, Sara Lahourpour
# Shehacks+ 7 Hacker Olympics 2023 Python Challenge #2
# Basic Budgeting 


## Program start
total_Food_Spending = 0
total_Entertainment_Spending = 0
total_Transportation_Spending = 0
total_Spending = 0

# Functions to prompt user for budget and purchase 
def addBudget():
  while True:
      budget_category = input("What category is the budget for? (Food, Transportation, Entertainment, Q) There are four valid inputs for you to choose from. Entering 'Food' will create a food budget for you. Entering 'Entertainment' will create an entertainment budget for you. Entering 'Transportation' will create a transportation budget for you.")
    
      budget_category = budget_category.capitalize()
      if budget_category == "Q":
        break
      elif (budget_category == "Food"):
        food_budget = int(input("Please set a budget for Food spending: "))
                    
      elif (budget_category == "Entertainment"):
        entertainment_budget = int(input("Please set a budget for Entertainment spending: "))
      elif (budget_category == "Transportation"):
        transportation_budget = int(input("Please set a budget for Transportation spending: "))
      else:
        print("Invalid input.")

def addPurchase():
    while True:
        purchase_category = input("What category is this purchase? (Food, Transportation, Entertainment, Q - if you have entered all purchase) ")
        if (purchase_category == "Food"):
            food_purchase = input("Please input a purchase amount for Food spending: ")
            total_Food_Spending = total_Food_Spending + food_puchase
            
            
        elif (purchase_category == "Entertainment"):
            entertainment_purchase = input("Please input a purchase amount for Entertainment spending: ")
            total_Entertainment_Spending + total_Entertainment_Spending + entertainment_purchase
            
        elif (purchase_category == "Transportation"):
            transportation_purchase = input("Please a purchase amount for Transportaion spending: ")
            total_Transportation_Spending = total_Transportation_Spending + transportation_purchase 
        elif (purchase_category == "Q"):
            break
        
        else:
            print("Invalid input.")


print("Hello user! This program will allow you to create a budget and track your spending. \nThere are four predetermined budgeting options set up for you. \n\nTyping ‘q’ will terminate your budget.\n\nTyping ‘h’ will prompt you with help options.\n\n")

while True:
    command = input("What would you like to do? (B -add a budget, Q - quit program, H - learn how to use the program, P - add purchase amount, C- calculate spending) ")
    command = command.capitalize()
  
    if command == "B":
        addBudget()
        
    elif command == "P":
        addPurchase()
    
    elif command == "H":
        print("There are four valid inputs for you to choose from. Entering 'q' will terminate your budget. You need to create your categories first and ")
        
    elif command == "Q":
        break
        
    elif command == "C":
        print("Welcome to your Budget Breakdown")
        total_Spending = total_Food_Spending + total_Entertainment_Spending + total_Transportation_Spending
        print("Total spending = $" + str(total_Spending))
        print("Total Food Spending = " + str(total_Food_Spending))
        if total_Food_Spending < food_budget:
          food_diff = food_budget - total_Food_Spending
          print("Food spending was under budget by " + str(food_diff))
          
        else:
          food_diff = total_Food_Spending - food_budget
          print("Food spending was over budget by " + str(food_diff))
            
        print("Total Entertainment Spending = " + total_Entertainment_Spending)
        if total_Entertainment_Spending < entertainment_budget:
          entertainment_diff = entertainment_budget - total_Entertainment_Spending
          print("Entertainment spending was under budget by " + str(entertainment_diff))
          
        else:
          entertainment_diff = total_Entertainment_Spending - entertainment_budget
          print("Entertainment spending was over budget by " + str(entertainment_diff))
            
        print("Total Transportation Spending = " + str(total_Transportation_Spending))
        if total_Transportation_Spending < transportation_budget:
          transportation_diff = transportation_budget - total_Transportation_Spending
          print("Transportation spending was under budget by " + str(transportation_diff))
          
        else:
          transportation_diff = total_Transportation_Spending - transportation_budget
          print("Transportation spending was over budget by " + str(transportation_diff))

exit()
