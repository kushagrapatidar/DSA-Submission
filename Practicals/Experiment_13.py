sequence = "ABCDDCEFFEBGAG"
capacity = 3

def find(seq, cap):
    size = 0
    cafe = []

    no_computer = []

    for customer in seq:
        if size<cap and customer not in cafe:
            cafe.append(customer)
            size += 1
        
        elif customer in cafe:
            cafe.remove(customer)
            size -= 1

        else:
            if customer not in no_computer:
                no_computer.append(customer)    

    return no_computer

no_computer = find(sequence, capacity)

print(len(no_computer), end=" ") 

for customers in no_computer:
    print(f"{customers} and ", end="")

print("left unattended")