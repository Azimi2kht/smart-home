import os

# Function to check if a MAC address is already saved in the file
def is_mac_address_saved(mac_address, file_path):
    if not os.path.exists(file_path):
        return False

    with open(file_path, 'r') as file:
        for line in file:
            saved_mac = line.split(',')[0]
            if saved_mac == mac_address:
                return True
    return False

# Function to save data to the file
def save_data(mac_address, temperature, brightness, file_path):
    with open(file_path, 'a') as file:
        file.write(f"{mac_address},{temperature},{brightness}\n")

# Main code
mac_address = "00:11:22:33:44:55"  # Replace with the actual MAC address
temperature = 25.5  # Replace with the actual temperature value
brightness = 90  # Replace with the actual brightness value
file_path = "data.txt"  # Path to the file where data will be stored

if not is_mac_address_saved(mac_address, file_path):
    save_data(mac_address, temperature, brightness, file_path)
    print("Data saved successfully.")
else:
    print("MAC address already exists in the file. Skipping...")