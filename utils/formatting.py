def format_string(string: str) -> str:
    return string.strip() \
                .replace(" ", "") \
                .replace("\n","") \
                .replace("\r","") \
                .lower()


