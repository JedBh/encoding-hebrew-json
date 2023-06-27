import json
import codecs

# Function to decode text
def decode_text(text):
    try:
        decoded_text = text.encode('iso-8859-1').decode('iso-8859-8')
        return codecs.decode(decoded_text, 'unicode_escape').encode('iso-8859-1').decode('utf-8')
    except Exception as e:
        print(f"Error decoding text: {e}")
        return text

# Read the JSON file
try:
    with open('ramatgan.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Iterate through the JSON content and decode the relevant fields
try:
    for feature in data.get('features', []):
        properties = feature.get('properties', {})
        
        if 'Name' in properties:
            print(decode_text(properties['Name']))
            properties['Name'] = decode_text(properties['Name'])
        if 'City' in properties:
            print(decode_text(properties['City']))
            properties['City'] = decode_text(properties['City'])
except Exception as e:
    print(f"Error processing JSON: {e}")
    exit()

# Write the converted content back to a new JSON file
try:
    with open('output.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"Error writing file: {e}")
    exit()
