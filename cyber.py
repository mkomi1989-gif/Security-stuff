failed_attempts = {}
threshold = 5


def check_login(username, is_failed):
    global failed_attempts

    if username not in failed_attempts:
        failed_attempts[username] = 0
    
    if is_failed:
        failed_attempts[username] += 1
    else:
        failed_attempts[username] = 0
    
    if failed_attempts[username] >= threshold:
        return f"Your account is currently locked. Failed Attempts: {failed_attempts[username]}"
    elif failed_attempts[username] == 3:
        return f"Warning. {failed_attempts[username]} number of attempts"
    else:
        return "Safe"
    
print(check_login("Melly12", True))
print(check_login("Melly12", True))
print(check_login("Melly12", True))
print(check_login("Melly12", True))
print(check_login("Melly12", True))
print(check_login("Melly12", True))
print(check_login("Melly12", False))



