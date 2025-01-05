class TextLine:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "index": ("INT", { }),
                "value": ("STRING", {
                    "multiline": True,
                }),
            },
        }

    DISPLAY_NAME = "TextLine"
    CATEGORY = "RF"
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("line",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, index, value):
        lines = value.split("\n")
        return lines[index % len(lines)]
