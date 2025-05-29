from datetime import datetime

class RF_Timestamp:
    @classmethod
    def INPUT_TYPES(cls):
        return { 
            "required": { 
                "format": ("STRING", { "default": "%Y-%m-%d_%H%M%S" }),
            }
        }

    # We use this to indicate that the output of the node changes outside of the UI
    @classmethod
    def IS_CHANGED(cls):
        return datetime.now()

    DISPLAY_NAME = "Timestamp (STRING)"
    CATEGORY = "RF/time"

    RETURN_NAMES = ("time",)
    RETURN_TYPES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self, format):
        return datetime.now().strftime(format),
