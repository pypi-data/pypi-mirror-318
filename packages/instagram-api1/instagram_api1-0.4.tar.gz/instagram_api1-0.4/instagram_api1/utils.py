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

    return "\n".join(processed_lines)
