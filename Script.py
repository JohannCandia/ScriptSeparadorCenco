import os

def process_file():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    files_in_directory = os.listdir(current_directory)
    source_file = [f for f in files_in_directory if f.endswith('.Out') and f != os.path.basename(__file__)][0]

    card_file_mapping = {
        'ACC VISA': 'clientes_VISA.txt',
        'ACC MC PLATINUM': 'clientes_MC_PLATINUM.txt',
        'ACC MC CLASSIC': 'clientes_MC_CLASSIC.txt',
        'ACC MC BLACK': 'clientes_MC_BLACK.txt'
    }

    buffer_data = {key: [] for key in card_file_mapping.values()}

    with open(source_file, 'r', encoding='latin-1') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line.startswith("CUS"):
            line = "CUS" + line
        
        if line.startswith("CUS"):
            client_data = [line]
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("CUS"):
                client_data.append(lines[i].strip())
                i += 1

            assigned = False
            for card_key, file_name in card_file_mapping.items():
                if any(card_key in data_line for data_line in client_data) and not assigned:
                    buffer_data[file_name].extend(client_data)
                    buffer_data[file_name].append("")  # Add an empty line for separation
                    assigned = True
        else:
            i += 1

    for file_name, data in buffer_data.items():
        if data:
            with open(file_name, 'a', encoding='latin-1') as out_f:
                out_f.write('\n'.join(data))

if __name__ == "__main__":
    process_file()
