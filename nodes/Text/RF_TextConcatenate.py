class RF_TextConcatenate:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "first": ("STRING", {
                    "defaultInput": True,
                }),
                "second": ("STRING", {
                    "defaultInput": True,
                }),
                "third": ("STRING", {
                    "default": ""
                }),
                "fourth": ("STRING", {
                    "default": ""
                }),
                "fifth": ("STRING", {
                    "default": ""
                }),
            },
        }

    DISPLAY_NAME = "Concatenate"
    CATEGORY = "RF/text"

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, first, second, third, fourth, fifth):
        result = first + second + third + fourth + fifth
        return (result,)
