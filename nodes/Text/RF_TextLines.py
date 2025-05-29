class RF_TextLines:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", { "default": "", "multiline": True }),
            },
        }

    DISPLAY_NAME = "Options (STRING)"
    CATEGORY = "RF/text"

    RETURN_NAMES = ("lines",)
    RETURN_TYPES = ("STRING",)

    # We use this to indicate that we will return a list in the first parameter
    OUTPUT_IS_LIST = (True,)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, text):
        return (text.splitlines(),)
