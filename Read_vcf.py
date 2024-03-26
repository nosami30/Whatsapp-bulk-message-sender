import re
def read_vcf(file_path):
    contacts = []

    with open(file_path, 'r') as file:
        contact_data = {}

        for line in file:
            name_match = re.match('FN:(.*)', line)
            if name_match:
                contact_data['name'] = name_match.group(1).strip()

            tel_match = re.match('TEL:(.*)', line)
            if tel_match:
                contact_data.setdefault('phone', []).append(tel_match.group(1).strip())

            if line.strip() == 'END:VCARD':
                contacts.append(contact_data.copy())
                contact_data.clear()
    Names = []
    for contact in contacts:
        Names.append(contact.get('name', 'No Name'))
    return  Names

# Example usage:

