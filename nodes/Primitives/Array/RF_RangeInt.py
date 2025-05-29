class RF_RangeInt:

    def INPUT_TYPES():
        return {
            "required": {
                "start": ("INT", { "default": 0 }),
                "step": ("INT", { "default": 1 }),
                "count": ("INT", { "default": 10 }),
            },
        }

    DISPLAY_NAME = "Repeat (INT)"
    CATEGORY = "RF/primitives/array"

    RETURN_NAMES = ("values",)
    RETURN_TYPES = ("INT",)
    OUTPUT_IS_LIST =(True,)

    def VALIDATE_INPUTS(step):
        if step == 0:
            return "Value cannot be 0."
        return True

    FUNCTION = "NodeProcess"
    def NodeProcess(self, start, step, count):
        return (range(start, start + count * step, step), )
