def serve_chai():
    chai_type = "Masala"  # local scope — only lives inside this function i.e. serve_chai
    print(f"Inside function i.e. chai_type aka local scope {chai_type}")

serve_chai()

chai_type = "Lemon"  # global scope
print(f"Outside function i.e. chai_type aka global scope {chai_type}")


def chai_counter():
    chai_order = "Lemon"  # enclosing scope — lives inside chai_counter

    def print_order():
        chai_order = "Ginger"  # local scope — brand new variable, enclosing untouched
        print(f"Inner i.e. chai_order aka local scope {chai_order}") #Ginger

    print_order()
    print(f"Outer i.e. chai_order aka enclosing scope {chai_order}")

chai_counter()  
   
chai_order = "Tulsi"  # global scope
print(f"Global i.e. chai_order aka global scope {chai_order}")
