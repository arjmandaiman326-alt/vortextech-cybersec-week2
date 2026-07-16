# Password Strength Checker

password = input("Enter your password: ")

length = len(password)

has_upper = False
has_number = False
has_symbol = False

symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.isdigit():
        has_number = True
    elif ch in symbols:
        has_symbol = True

score = 0

if length >= 8:
    score += 1

if has_upper:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1

print("\nPassword Analysis")
print("-----------------")
print("Length:", length)
print("Contains Uppercase:", has_upper)
print("Contains Number:", has_number)
print("Contains Symbol:", has_symbol)

if score <= 1:
    print("\nPassword Strength: Weak")
elif score <= 3:
    print("\nPassword Strength: Medium")
else:
    print("\nPassword Strength: Strong")