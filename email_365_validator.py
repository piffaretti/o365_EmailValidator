#script created by Diego Piffaretti
import os
import re
import subprocess

def get_status_code(url):
    try:
        result = subprocess.run(["curl", "-I", url], capture_output=True, text=True, check=True)
        http_response = result.stdout
        status_code = http_response.split()[1]
        return status_code
    except subprocess.CalledProcessError:
        return "Error"

def main():
    # Read the tenant name
    tenant_name = input("Enter the tenant name: ")

    # Read the email or file with multiple emails
    email_input = input("Enter an email or the path to a file with multiple emails: ")

    # If the input is a file, read emails from the file
    if os.path.isfile(email_input):
        with open(email_input, "r") as file:
            emails = file.read().splitlines()
    else:
        emails = [email_input]

    for email in emails:
        # Clean the email (replace dots and at symbols with underscores)
        email_cleaned = re.sub(r'[.@]', '_', email)

        # Construct the URL
        url = f"https://{tenant_name}-my.sharepoint.com/personal/{email_cleaned}/_layouts/15/onedrive.aspx"

        # Get the status code
        status_code = get_status_code(url)

        if status_code == "403":
            print(f"Email: {email} is VALID")
        elif status_code == "404":
            print(f"Email: {email} is invalid")
        else:
            print(f"Email: {email} Status Code: {status_code}")

if __name__ == "__main__":
    main()
