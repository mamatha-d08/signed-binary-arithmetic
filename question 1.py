def to_binary(n):
    return format(n & 0xFF, '08b')

def signed_add(a, b):
    result = (a + b) & 0xFF

    # Check signed overflow
    overflow = (a >= 0 and b >= 0 and result >= 128) or \
               (a < 0 and b < 0 and result < 128)

    decimal_result = result if result < 128 else result - 256

    print("First operand :", to_binary(a))
    print("Second operand:", to_binary(b))
    print("Binary result :", format(result, '08b'))
    print("Decimal result:", decimal_result)
    print("Overflow      :", "Yes" if overflow else "No")
    print()

print("a) 25 + (+18)")
signed_add(25, 18)

print("b) (-25) + (-18)")
signed_add(-25, -18)