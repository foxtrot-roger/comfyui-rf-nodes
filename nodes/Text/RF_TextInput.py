class RF_TextInput:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": ("STRING", {
                    "multiline": True,
                }),
            },
        }

    DISPLAY_NAME = "Input (STRING)"
    CATEGORY = "RF/text"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, value):
        return value,
