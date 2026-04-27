def save_user(username, age):
    try:
        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")
    except Exception as e:
        print("Error saving data:", e)

def display_users():
    try:
        with open("users.txt", "r") as file:
            print("\nSaved Users:")
            print("----------------")
            print(file.read())
    except FileNotFoundError:
        print("No users found yet.")
    except Exception as e:
        print("Error reading file:", e)

def main():
    try:
        username = input("Enter username: ").strip()
        
        if not username:
            raise ValueError("Username cannot be empty.")

        age_input = input("Enter age: ")
        age = int(age_input)

        if age <= 0:
            raise ValueError("Age must be a positive number.")

        save_user(username, age)
        display_users()

    except ValueError as ve:
        print("Input Error:", ve)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        print("System complete.")

main()