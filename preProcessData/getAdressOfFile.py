import csv
import argparse

def find_address_by_id(csv_file, search_id):
    """
    Searches for an ID in a CSV file and returns the corresponding address.
    
    Parameters:
    csv_file (str): The path to the CSV file.
    search_id (str or int): The ID to search for.
    
    Returns:
    dict or None: A dictionary representing the row of the found ID, or None if not found.
    """
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['building_id'] == str(search_id):  # Convert search_id to string for comparison
                return row
    
    return None

def main():
    parser = argparse.ArgumentParser(description="Search for an ID in a CSV file and return the corresponding address.")
    parser.add_argument('csv_file', type=str, help='The path to the CSV file.')
    parser.add_argument('search_id', type=str, help='The ID to search for.')

    args = parser.parse_args()
    
    address = find_address_by_id(args.csv_file, args.search_id)
    if address:
        print("Address found:", address["Straße"], address["HNr"], "0" + str(int(address["PLZ"][:-2])), args.search_id)
    else:
        print("ID not found in the CSV file.")

if __name__ == "__main__":
    main()
