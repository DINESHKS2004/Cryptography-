
import math

# Playfair uses 25 letters (I and J combined)

n = 25

# Total possible keys = 25!
total_keys = math.factorial(n)

# Approximate power of 2
power_total = math.log2(total_keys)

print("Total possible keys =", total_keys)
print("Approximate power of 2 = 2^", round(power_total, 2))

# Effectively unique keys
# 25! / (25 * 24) = 23!
unique_keys = math.factorial(23)
power_unique = math.log2(unique_keys)

print("Effectively unique keys =", unique_keys)
print("Approximate power of 2 = 2^", round(power_unique, 2))
