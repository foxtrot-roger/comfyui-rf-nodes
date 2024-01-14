from datetime import datetime

class RF_Timestamp:
    @classmethod
    def INPUT_TYPES(cls):
        return { 
            "required": { }
        }

    # We use this to indicate that the output of the node changes outside of the UI
    @classmethod
    def IS_CHANGED(cls):
        return datetime.now()

    DISPLAY_NAME = "Timestamp (STRING)"
    CATEGORY = "RF"

    RETURN_NAMES = ("time",)
    RETURN_TYPES = ("STRING",)

    FUNCTION = "NodeProcess"
    def NodeProcess(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
