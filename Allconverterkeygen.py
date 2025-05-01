import platform
import sys

def vista_with_theme() -> bool:
    ver = platform.version().split('.')
    try:
        major = int(ver[0])
    except ValueError:
        major = 0
    return major >= 6

def generate_reg_key(reg_name: str, reg_email: str) -> str:
    ProductName = 'ALLConverterPRO'
    mask = 0xFFFFFFFF

    value1 = 1
    s1 = (ProductName + reg_name).upper()
    for ch in s1:
        temp = (ord(ch) * value1) & mask
        inc = temp // 10
        value1 = (value1 + inc) & mask

    value2 = 1
    s2 = (ProductName + reg_email).upper()
    for ch in s2:
        temp = (ord(ch) * value2) & mask
        inc = temp // 10
        value2 = (value2 + inc) & mask

    return f"{value1}{value2}"

def show_banner():
    print("=====================================")
    print("         Keygen by Redfed")
    print("=====================================\n")

def main():
    show_banner()

    if not vista_with_theme():
        print("This tool requires Windows Vista or later with themes enabled.")
        sys.exit(1)

    print("=== ALLConverterPRO Registration ===")
    name = input("Enter your registration name: ").strip()
    email = input("Enter your registration email: ").strip()

    if not name or not email:
        print("Error: Both name and email must be provided.", file=sys.stderr)
        sys.exit(1)

    key = generate_reg_key(name, email)

    print("\n=== Registration Key ===")
    print(key)

if __name__ == "__main__":
    main()
