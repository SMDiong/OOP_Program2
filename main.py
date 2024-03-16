# Name: Diong, Shan Marc C.
# Section: BSCpE 1-2
# Program #2: Write a program that will ask you to input your name and your dream job. Print them in a fancy way

# Fancy Word Functions
blue = "\033[0;34m"
purple = "\033[0;35m"
green = "\033[0;32m"
bold = "\033[1m"
def fancy_print(name, job):
    print("\n")
    print(purple + "=" * 71)
    print(blue + bold + f"\tHello, {name}! Your dream job is {job}!")
    print(purple + "=" * 71)
    print("\n")

# Main Function, Input and Output
def main():
    user_name = input(green + bold + "Please enter your name: ")
    dream_job = input(green + bold + "Please enter your dream job: ")
    fancy_print(user_name, dream_job)

main()

#end
