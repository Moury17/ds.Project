filename= "Rocks.txt"
def load_data(filename):
    data=[]
    with open(filename, 'r') as file:
        for line in file:
            rock_data=line.strip().split(',')
            data.append(rock_data)
    return data
def save_data(data,filename):
    with open(filename,'w') as file:
        for rock in data:
            line=','.join(rock)
            file.write(line+'\n')
def display_menu():
    print("1. Add a rock sample")
    print("2. View all rock samples")
    print("3. Search for a rock sample")
    print("4. Edit a rock sample")
    print("5. Delete a rock sample")
    print("6. Exit")
def add_rock(data):
    rock_name=input("Enter rock name:")
    rock_type=input("Enter rock type:")
    collection_date=input("Enter collection date(YYYY-MM-DD):")
    new_rock=[rock_name,rock_type,collection_date]
    data.append(new_rock)
    save_data(data,"Rocks.txt")
    print("Rock added successfully.")
def view_all(data):
    index=1
    for rock in data:
        print(f"Rock {index}:{rock[0]},{rock[1]},{rock[2]}")
        index += 1
def search_rock(data):
    search_term=input("Enter search term:")
    found= False
    for rock in data:
        if search_term in rock:
            print(rock)
            found=True
    if not found:
        print("Rock is not found!")
def edit_rock(data):
    index=int(input("Enter the index of the rock to edit:"))-1
    if 0<=index<len(data):
        rock=data[index]
        print(f"Current data for rock{index+1}:{rock}")
        rock[0]=input("Enter new name:")
        rock[1] =input("Enter new type:")
        rock[2]= input("Enter new collection date:")
        save_data(data,"Rocks.txt")
        print("Rock updated successfully.")
    else:
        print("Invalid index!")

def delete_rock(data):
    index=int(input("Enter the index of the rock to delete:"))-1
    if 0<=index<len(data):
        data.pop(index)
        save_data(data,"Rocks.txt")
        print("Rock deleted successfully.")
    else:
        print("Invalid index!")
if __name__=="__main__":
    data= load_data(filename)
    while True:
        display_menu()
        choice= input("Enter your Choice:")
        if choice == '1':
            add_rock(data)
        elif choice == '2':
            view_all(data)
        elif choice == '3':
            search_rock(data)
        elif choice == '4':
            edit_rock(data)
        elif choice == '5':
            delete_rock(data)
        elif choice == '6':
            break
