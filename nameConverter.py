import re

def converter(name: str, suffix: str) -> str:
    # Extract question number and title
    match = re.match(r'(\d+)\.\s+(.*)', name)
    if not match:
        raise ValueError("Input string must be in the format '1234. Title Here'")
    
    number = match.group(1)
    title = match.group(2)
    
    # Remove special characters and split into words
    words = re.findall(r'\w+', title)
    if not words:
        raise ValueError("Title contains no valid words")

    # CamelCase the title: first word lowercase, others capitalized
    camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
    # Construct final filename
    filename = f"Qn{number}_{camel_case}.{suffix}"
    return filename

if __name__ == "__main__":
    print(converter(
        name = '27. Remove Element',
        suffix = "c"
    ))