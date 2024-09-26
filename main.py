def welcome_user():
  print("Welcome to the chatbot!")

def get_user_info():
  name = input("What is your name? ")
  age = input("How old are you? ")
  return name, age

def show_menu():
  print("\nHow can I assist you today?")
  print("1. Option 1 (Placeholder)")
  print("2. Option 2 (Placeholder)")
  print("3. Exit")

def handle_choice(choice):
  if choice == '1':
      print("You chose Option 1 (Placeholder).")
  elif choice == '2':
      print("You chose Option 2 (Placeholder).")
  elif choice == '3':
      print("Goodbye! Thank you for using the chatbot.")
      return True
  else:
      print("Invalid choice. Please try again.")
  return False

def chatbot():
  welcome_user()
  name, age = get_user_info()
  print(f"\nNice to meet you, {name} who is {age} years old!")

  while True:
      show_menu()
      choice = input("\nPlease enter the number of your choice: ")
      if handle_choice(choice):
          break

# Start the chatbot
chatbot()
