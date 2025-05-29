class RF_TextReplace:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "Template {text} to replace!",
                    "defaultInput": True,
                }),
                "search": ("STRING", {
                    "default": "{text}"
                }),
                "replace": ("STRING", {
                    "multiline": True,
                    "default": "value"
                }),
            },
        }

    DISPLAY_NAME = "Replace text"
    CATEGORY = "RF/text"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, text, search, replace):
        result = text.replace(search, replace)
        return (result,)
