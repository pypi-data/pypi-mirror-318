### Usage
Function: convert_email_to_userpass
```python
def convert_email_to_userpass(file_content):
    """
    تحويل محتوى ملف TXT إلى تنسيق user:pass.
    
    Args:
        file_content (str): محتوى الملف كنص.
    
    Returns:
        str: نص بتنسيق user:pass بدون تكرار.
    """
    lines = file_content.splitlines()
    processed_lines = set()

    for line in lines:
        if ":" in line:
            email, password = line.split(":", 1)
            username = email.split("@")[0]
            processed_lines.add(f"{username}:{password}")

    return "\\n".join(processed_lines)
### Example: Convert Email-Password File
from instagram_api1 import convert_email_to_userpass


file_content = """
davidlains@gmail.com:gfgarage
anthony.groult@aliceadsl.fr:esclave1
"""


result = convert_email_to_userpass(file_content)
print(result)
### Example: Try Instagram Login
from instagram_api1 import try_login
username = input("أدخل اسم المستخدم (username): ").strip()
password = input("أدخل كلمة المرور (password): ").strip()
session_id = try_login(username, password)
if session_id:
    print(f"Session ID: {session_id}")
else:
    print("فشل تسجيل الدخول.")
###Example: Reset Instagram Password
from instagram_api1 import InstagramAPI
instagram_api = InstagramAPI()


email = input("Enter the email to reset password: ")


result = instagram_api.send_password_reset(email)


if "error" in result:
    print(f"Error: {result['error']}")
else:
    print("Password reset request sent successfully!")