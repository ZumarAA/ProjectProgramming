# validation functions return either True or False
# this module has different general validation checks
# for simplicity  I included only few for this demo

# when any function called returns eith True or False.
def validuser(user):  # length check for username
    if len(user)>=4 and len(user)<20:
        return True
    else:
        return False


def validpass(password):  # password length check
    if len(password)>= 8:
        return True
    else:
        return False