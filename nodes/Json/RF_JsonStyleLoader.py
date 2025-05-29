import json
import os

def read_json_file(file_path):
    if not os.access(file_path, os.R_OK):
        print(f"Warning: No read permissions for file {file_path}")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = json.load(file)
            # Check if the content matches the expected format.
            if not all(['name' in item and 'prompt' in item and 'negative_prompt' in item for item in content]):
                print(f"Warning: Invalid content in file {file_path}")
                return None
            return content
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {str(e)}")
        return None

def get_all_json_files(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.json') and os.path.isfile(os.path.join(directory, file))]

def load_styles_from_directory(directory):
    json_files = get_all_json_files(directory)
    combined_data = []
    seen = set()

    for json_file in json_files:
        json_data = read_json_file(json_file)
        if json_data:
            for item in json_data:
                original_style = item['name']
                style = original_style
                suffix = 1
                while style in seen:
                    style = f"{original_style}_{suffix}"
                    suffix += 1
                item['name'] = style
                seen.add(style)
                combined_data.append(item)

    unique_style_names = [item['name'] for item in combined_data if isinstance(item, dict) and 'name' in item]

    return combined_data, unique_style_names

def validate_json_data(json_data):
    if not isinstance(json_data, list):
        return False
    for template in json_data:
        if 'name' not in template or 'prompt' not in template:
            return False
    return True

def find_template_by_name(json_data, template_name):
    for template in json_data:
        if template['name'] == template_name:
            return template
    return None

class RF_JsonStyleLoader:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        self.json_data, styles = load_styles_from_directory(current_directory)

        return {
            "required": {
                "style": ((styles), ),
                "prompt": ("STRING", { "default": "{prompt}" }),
                "negative_prompt": ("STRING", { "default": "{negative_prompt}" }),
            },
            "optional": {
                "positive": ("STRING", { "multiline": True }),
                "negative": ("STRING", { "multiline": True }),
            }
        }

    DISPLAY_NAME = "Style from JSON file"
    CATEGORY = "RF/json"

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive", "negative")

    FUNCTION = "NodeProcess"
    def NodeProcess(self, style, prompt, negative_prompt, positive, negative):
        template = find_template_by_name(self.json_data, style)

        p =  template.get('prompt', "")
        if(p.strip() != ""):
            positive = p.replace(prompt, positive)

        n =  template.get('negative_prompt', "")
        if(n.strip() != ""):
            negative = n.replace(negative_prompt, negative)

        return positive, negative
