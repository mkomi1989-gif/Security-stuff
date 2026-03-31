failed_attempts = {}
threshold = 5

def check_login(username, is_failed):
    if username not in failed_attempts:
        failed_attempts[username] = 0
    
    if is_failed:
        failed_attempts[username] += 1
    else:
        failed_attempts[username] = 0
    
    if failed_attempts[username] >= threshold:
        return f"Too many failed login attempts. Your account is temporarily locked with {failed_attempts[username]} login attempts. Please try again later"
    elif failed_attempts[username] >= 3:
        return f"Warning. {failed_attempts[username]} login attempts detected"
    else:
        return f"Safe. {failed_attempts[username]} login attempts"
    
with open("logins.txt") as file:
    for line in file:
        cleaned_line = line.strip()
        part = cleaned_line.split()
        if len(part) != 2:
            print(f"Skipping invalid line: {cleaned_line}")
            continue
        username = part[0]
        status = part[1]

        if status not in ["FAILED", "SUCCESS"]:
            print(f"Skipping invalid status: {status}")
            continue

        if status == "FAILED":
            is_failed = True
        else:
            is_failed = False
        
        result = check_login(username, is_failed)
        print(f"{username}: {result}")