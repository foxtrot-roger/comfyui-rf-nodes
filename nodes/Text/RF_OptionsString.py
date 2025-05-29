class RF_OptionsString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "index": ("INT", { "default": 0 }),
                "text": ("STRING", { "default": "", "multiline": True }),
            },
        }

    DISPLAY_NAME = "One of (STRING)"
    CATEGORY = "RF/text"

    RETURN_NAMES = ("text",)
    RETURN_TYPES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, text, index):
        lines = text.splitlines()
        return ( lines[index % len(lines)],)
