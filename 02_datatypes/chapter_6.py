# LECTURE 15 — Strings: Indexing, Slicing and Encoding in Python


# Strings are sequences of characters
chai_type = "Ginger chai"
customer_name = "Priya"

# f-string allows inserting variables directly inside strings
print(f"Order for {customer_name} : {chai_type} please!")


# String slicing examples
chai_description = "Aromatic and bold"

# Slice syntax: [start : end]
# start index included, end index excluded
print(f"First word: {chai_description[:8]}")  # from start up to index 8

# If start index is given but end is omitted → slice until the end
print(f"Last word: {chai_description[12:]}")

# Step slicing: [start:end:step]
# -1 step reverses the string
print(f"Reverse words: {chai_description[::-1]}")


# Encoding and decoding strings
# Encoding → converting text (string) into bytes
# Decoding → converting bytes back into text

label_text = "Chai Spécial"

# Encode string using UTF-8 (common text encoding standard)
encoded_label = label_text.encode("utf-8")

print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")

# Decode bytes back into readable string
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")