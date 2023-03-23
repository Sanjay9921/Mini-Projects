#Functions
def welcome_msg():
    print("Welcome to TIP Calculator Project!")


def ask_questions():
    total_bill = float(input("What is your total bill ? $"))
    tip = float(input("Write the percentage of tip you'd like to give? 10/12/15 ?"))
    n_people = float(input("How many people to split the bill? "))

    return (total_bill, tip, n_people)


def tip_calculator():
    welcome_msg()

    total_bill, tip, n_people = ask_questions()
    total_tip = (total_bill / n_people) * (1 + tip / 100)
    total_tip = round(total_tip, 2)

    print(f"Each person can pay ${total_tip}.")

#Testing
tip_calculator()