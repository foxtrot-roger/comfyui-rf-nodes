class RF_AtIndexString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lines": ("STRING", { "default": "", "multiline": True }),
                "index": ("INT", { "default": 0 }),
            },
        }

    DISPLAY_NAME = "At index (STRING)"
    CATEGORY = "RF/primitives/array"

    # This lets us get inputs as an array so that we can join it
    INPUT_IS_LIST = True

    RETURN_NAMES = ("text",)
    RETURN_TYPES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, lines, index):
        return (lines[index[0] % len(lines)],)
