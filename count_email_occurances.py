✅ Python Code to Count Email Occurrences in a File

import re
from collections import Counter

def count_emails(filename):
    # Regular expression for email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_counter = Counter()

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Find all email addresses in the current line
            emails = re.findall(email_pattern, line)
            # Update the counter with the found emails
            email_counter.update(emails)

    return email_counter

# Example usage
if __name__ == "__main__":
    file_path = 'input.txt'  # Replace with your file path
    counts = count_emails(file_path)
    
    print("Email Address Counts:")
    for email, count in counts.most_common():
        print(f"{email}: {count}")


📌 Sample Input (input.txt)
Hi there, contact me at alice@example.com.
You can also CC bob123@work.net and info@company.co.in.
alice@example.com is my primary address.


  
🧾 Sample Output
Email Address Counts:
alice@example.com: 2
bob123@work.net: 1
info@company.co.in: 1
