rock_samples = []

def add_rock_sample(samples):
    name = input("Enter name of the rock sample: ")
    age = int(input("Enter age of the rock sample: "))
    location = input("Enter location of the rock sample: ")
    rock_type = input("Enter rock type of the rock sample: ")
    sample = {
        'name': name,
        'age': age,
        'location': location,
        'rock_type': rock_type
    }
    rock_samples.append(sample)
    print(f"Rock sample '{name}' is added successfully.")

def view_all():
    if not rock_samples:
        print("No samples are found")
    else:
        print("\nPrint Rock Samples:")
        for sample in rock_samples:
            print(f"Name:{sample['name']} Age:{sample['age']} Location:{sample['location']} Rock Type:{sample['rock_type']}")

def search_sample(name):  # Add 'name' parameter
    found_samples = []
    for sample in rock_samples:
        if sample['name'] == name:
            found_samples.append(sample)

    if len(found_samples) > 0:
        print("\nFound Rock Samples:")
        for sample in found_samples:
            print(f"Name:{sample['name']} Age:{sample['age']} Location:{sample['location']} Rock Type:{ sample['rock_type']}")
    else:
        print("No samples found with that name.")

def edit_sample():
    global rock_samples
    new_samples = []
    sample_number = int(input("Enter the sample number to edit:"))
    sample_index = sample_number - 1
    for i in range(len(rock_samples)):
        if i == sample_index:
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_location = input("Enter new location: ")
            new_rock_type = input("Enter new rock type: ")
            new_samples.append({
                'name': new_name,
                'age': new_age,
                'location': new_location,
                'rock_type': new_rock_type
            })
        else:
            new_samples.append(rock_samples[i])

    if 0 <= sample_index < len(rock_samples):
        rock_samples = new_samples
        print(f"Rock sample at index {sample_number} updated.")
    else:
        print("Invalid index.")

def delete_sample():
    global rock_samples
    index = int(input("Enter the index of the sample to delete:"))
    if 0 <= index < len(rock_samples):
        deleted_sample = rock_samples.pop(index)
        print(f"Rock sample {deleted_sample['name']} is deleted")
    else:
        print("Invalid index")

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("\n--- Rock Sample Management System ---")
        print("1. Add Rock Sample")
        print("2. View All Rock Samples")
        print("3. Search Rock Sample by Name")
        print("4. Edit Rock Sample")
        print("5. Delete Rock Sample")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    add_rock_sample(rock_samples)
                case 2:
                    view_all()
                case 3:
                    name = input("Enter name of the rock sample to search: ") 
                    search_sample(name)
                case 4:
                    edit_sample()
                case 5:
                    delete_sample()
                case 6:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
if __name__=="__main__":
    main_menu()