import os
import folder_paths
import json


class RF_SavePromptInfo:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "filename_prefix": ("STRING", {"default": "ComfyUI"}),
                "indent": ("INT", {"default": 20})
                },
            "hidden": {
                "prompt": "PROMPT",
                },
            }

    RETURN_TYPES = ()
    FUNCTION = "save_prompt"

    OUTPUT_NODE = True

    DISPLAY_NAME = "Save prompt to file"
    CATEGORY = "RF/file"

    def save_prompt(self, filename_prefix, indent, prompt):
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir, 0, 0)
        fileName = f"{filename}_{counter:05}_.json"
        file = open(os.path.join(full_output_folder, fileName), "w")
        file.write(json.dumps(prompt, indent=indent))
        file.close()
        return ()
