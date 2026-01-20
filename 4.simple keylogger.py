print("Simple Keylogger (Ethical Version)")
print("This program logs ONLY what you type here.")
print("Type EXIT to stop logging.\n")

with open("keystrokes.log", "a") as log_file:
    while True:
        user_input = input("Type something: ")

        if user_input.upper() == "EXIT":
            print("Keylogging stopped.")
            break

        log_file.write(user_input + "\n")
