def policz():
    try:
        return 1 / 0
    finally:
        return 42

# print(policz())

try:
    int("abc")
except ValueError, TypeError:
    print("złapany")
