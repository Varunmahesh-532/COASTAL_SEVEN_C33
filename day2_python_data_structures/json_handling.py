import json
import os

def process_json_file():
    input_file = "sample.json"
    output_file = "output.json"
    # Check if the input file exists
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
            print("==========Original Data==========")
            print(data)

        # Modify the data (for demonstration, let's add a new key-value pair)
        data['status'] = 'Completed'
        data['team_members'].append("David")

        # Write the modified data back to a new JSON file
        with open(output_file, 'w') as file:
            json.dump(data, file, indent = 2)
        print(f"\nModified data has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file {input_file} does not contain valid JSON.")

if __name__ == "__main__":
    process_json_file()

