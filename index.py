import re

def password_strength_function (password):
    user_score = 0

# =================lenght of password=================

    if len(password) >= 8:
        user_score +=1
    else :
        print("Password must be at least 8 characters long")

# ==================check for uppercase=================

    if re.search ( r"[A-Z]", password ) and re.search ( r"[a-z]", password ) :
        user_score +=1
    else:
        print("Password must contain at least one uppercase and one lowercase letter")

# ==================check for special characters=================

    if re.search (r"[!@#$%^&]", password):
        user_score +=1
    else:
        print("Password must contain at least one special character (!@#$%^&)")

# ==================check for numbers=================

    if re.search(r"\d", password):
        user_score +=1
    else:
        print("Password must contain at least one number")



# ================Calculating Points ===============

    if user_score == 4:
        print ("\nYour Password is strong ✔️👏🙌\n")
    elif user_score == 3:
        print ("\nYour Password is fine but it needs more improvement 👍👍\n")
    else :
        print ("\nYour Password is weak 🥱😓☹\n")


   

password = input ("Enter Your Password: ")
password_strength_function(password)