class RF_TextMergeLines:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", { "default": "", "multiline": True }),
            },
        }

    DISPLAY_NAME = "Merge lines (STRING)"
    CATEGORY = "RF/text"

    # This lets us get inputs as an array so that we can join it
    INPUT_IS_LIST = True

    RETURN_NAMES = ("lines",)
    RETURN_TYPES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, text):
        return ("\n".join(text),)
