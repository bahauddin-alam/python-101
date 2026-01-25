#LECTURE -- 15. String - Index, Slice and Encoding

chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please!") #Good e.g. of string

chai_description = "Aromatic and bold"
print(f"First word: {chai_description [:8]}") #Can include 0 in starting
print(f"Last word: {chai_description [12:]}") #No need of adding number later in ratio perhaps you want specific word
print(f"Reverse words: {chai_description [::-1]}") #Makes strings in reverse order



#HERE I HAVE PROBLEM IN ENCODING AND DECODING THING WILL REVISE THIS CONCEPT TIME STAMP-- FROM 8:48-12:00
label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")