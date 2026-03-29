failed_attempts = {}
threshold = 5

def check_login(username, login_fail):
    global failed_attempts

    if username not in failed_attempts:
        failed_attempts[username] = 0
    
    if login_fail:
        failed_attempts[username] += 1
    else:
        failed_attempts[username] = 0
        return "Login Successful. Attempts reset to 0"
    
    if failed_attempts[username] >= threshold:
        return f"Your account has been locked. Failed Attempts: {failed_attempts[username]}"
    elif failed_attempts == 3:
        return f"Warning. {failed_attempts[username]} failed login attempts detected"
    else:
        return f"Safe. Failed attempts: {failed_attempts[username]}"


print(check_login("Melly23", True))
print(check_login("Melly23", True))
print(check_login("Melly23", True))
print(check_login("Melly23", True))
print(check_login("Melly23", True))
print(check_login("Melly23", False))


