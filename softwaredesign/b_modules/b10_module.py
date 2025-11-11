# b10 module 
# Convert Roman numerals to Arabic numbers (1–3999)

roman_values = {
    "M": 1000, "CM": 900, "D": 500, "CD": 400,
    "C": 100, "XC": 90, "L": 50, "XL": 40,
    "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
}

def roman_to_arabic(roman: str) -> int:
    """Translate a Roman numeral into an Arabic integer."""
    i = 0
    value = 0
    while i < len(roman):
        # Try to match two-letter symbols first (like 'IV', 'CM')
        if i + 1 < len(roman) and roman[i:i+2] in roman_values:
            value += roman_values[roman[i:i+2]]
            i += 2
        else:
            value += roman_values[roman[i]]
            i += 1
    return value


# Example usage
samples = ["MMMDCCXXIV", "MXCIV", "VIII", "XLII", "CDXLIV", "MMMCMXCIX"]
for s in samples:
    print(f"{s:10s} → {roman_to_arabic(s)}")