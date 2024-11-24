## Main to gather user input the string, substring, and if the user wants to edit the string, and prints new string

def main():    
    print("This is a program that searches for a substring within a user given string!")
    main_string = get_string_input("Enter the main string: ")
    substring = get_string_input("Enter the substring to search for: ")
    index = contains_substring(main_string, substring)
    if index != -1:    
        replace = input("Do you want to replace the substring? (y/n): ")
        while replace.lower() not in ["y", "n"]:    
            replace = input("Invalid entry. Please enter 'y' or 'n': ")
        if replace.lower() == "y":    
            new_string = get_string_input("Enter the new string: ")
            main_string = replace_substring(main_string, substring, new_string)
            print(f"Updated new string: {main_string}")
        else:    
            print("No replacement was made.")
            
    print("Thank you for using my program!")
    print("Completed by, Gage Yandle")

##  using prompt over input, functions for string input, substring input, and replacing substring.

def get_string_input(prompt): 
    return input(prompt)

def contains_substring(main_string, substring):    
    index = main_string.find(substring)
    if index != -1:
        print(f"'{substring}' was found at index {index}.")
        return index
    else:
        print(f"'{substring}' was not found.")
    return -1

def replace_substring(main_string, substring, new_string):    
    return main_string.replace(substring,new_string)

if __name__ == "__main__":    
    main()
