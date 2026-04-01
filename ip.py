failed_attempts = {}
threshold = 5
total_failed_attempts = 0


def check_ip_logins(ip_address, is_failed): 

    if ip_address not in failed_attempts:
        failed_attempts[ip_address] = 0

    
    if is_failed:
        failed_attempts[ip_address] += 1
    else:
        failed_attempts[ip_address] = 0
    
    if failed_attempts[ip_address] >= threshold:
        return f"Too many attempts. Your account has been locked after {failed_attempts[ip_address]} failed entries. Please contact customer service."
    elif failed_attempts[ip_address] >= 3:
        return f"Warning. {failed_attempts[ip_address]} attempts out of {threshold}"
         
    else:
        return f"Safe. You have {failed_attempts[ip_address]} attempts."
    
with open("ips.txt") as file:
    for line in file:
        cleaned_line = line.strip()
        parts = cleaned_line.split()
        if len(parts) != 2:
            print(f"Skipping invalid line..: {cleaned_line}")
            continue
        
        ip_address = parts[0]
        status = parts[1]


        if status not in ["FAILED", "SUCCESS"]:
            print(f"Skipping invalid status: {status}")
            continue

        if status == "FAILED":
            is_failed = True
        else:
            is_failed = False

        if is_failed:
            total_failed_attempts += 1
            
        result = check_ip_logins(ip_address, is_failed)
        print(f"{ip_address}: {result}")
        print(f"Total failed attempts: {total_failed_attempts}")

    
    
