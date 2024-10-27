

def save_data(temperature, brightness, file_path):
    with open(file_path, 'w') as file:
        file.write(f"{temperature},{brightness}\n")


save_data(2, 3, "preferred.txt")

