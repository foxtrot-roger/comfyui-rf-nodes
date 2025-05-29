from .nodes.Text.RF_TextMergeLines import *
from .nodes.Text.RF_TextLines import *
from .nodes.Text.RF_TextMergeLines import *
from .nodes.Time.RF_Timestamp import *

from .nodes.Text.TextLine import TextLine
from .nodes.Text.RF_TextInput import RF_TextInput
from .nodes.Text.RF_TextConcatenate import RF_TextConcatenate
from .nodes.Text.RF_TextReplace import RF_TextReplace
from .nodes.Text.RF_OptionsString import RF_OptionsString

from .nodes.ToString.RF_Vec3ToString import RF_Vec3ToString
from .nodes.ToString.RF_Vec2ToString import RF_Vec2ToString
from .nodes.ToString.RF_NumberToString import RF_NumberToString
from .nodes.ToString.RF_FloatToString import RF_FloatToString
from .nodes.ToString.RF_BoolToString import RF_BoolToString
from .nodes.ToString.RF_IntToString import RF_IntToString
from .nodes.ToString.RF_ToString import RF_ToString

from .nodes.Log.RF_LogString import RF_LogString
from .nodes.Log.RF_LogVec3 import RF_LogVec3
from .nodes.Log.RF_LogVec2 import RF_LogVec2
from .nodes.Log.RF_LogNumber import RF_LogNumber
from .nodes.Log.RF_LogFloat import RF_LogFloat
from .nodes.Log.RF_LogBool import RF_LogBool
from .nodes.Log.RF_LogInt import RF_LogInt

from .nodes.Json.RF_JsonStyleLoader import RF_JsonStyleLoader
from .nodes.File.RF_SavePromptInfo import RF_SavePromptInfo

from .nodes.Primitives.RF_FloatPrimitive import RF_FloatPrimitive
from .nodes.Primitives.Array.RF_RangeInt import RF_RangeInt
from .nodes.Primitives.Array.RF_RangeFloat import RF_RangeFloat
from .nodes.Primitives.Array.RF_RangeNumber import RF_RangeNumber
from .nodes.Primitives.Array.RF_AtIndexString import RF_AtIndexString

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {

    "RF_Timestamp": RF_Timestamp,
    "RF_SplitLines": RF_TextLines,
    "RF_MergeLines": RF_TextMergeLines,
    "RF_OptionsString": RF_OptionsString,

    "RF_TextInput": RF_TextInput,
    "TextLine": TextLine,
    "RF_TextReplace": RF_TextReplace,
    "RF_TextConcatenate": RF_TextConcatenate,

    # ToString
    "RF_ToString": RF_ToString,
    "RF_IntToString": RF_IntToString,
    "RF_BoolToString": RF_BoolToString,
    "RF_FloatToString": RF_FloatToString,
    "RF_NumberToString": RF_NumberToString,
    "RF_Vec2ToString": RF_Vec2ToString,
    "RF_Vec3ToString": RF_Vec3ToString,
    "LogString": RF_LogString,

    # primitives
    "RF_FloatPrimitive": RF_FloatPrimitive,
    "RF_RangeInt": RF_RangeInt,
    "RF_RangeFloat": RF_RangeFloat,
    "RF_RangeNumber": RF_RangeNumber,
    "RF_AtIndexString": RF_AtIndexString,

    # Log
    "LogString": RF_LogString,
    "LogInt": RF_LogInt,
    "LogBool": RF_LogBool,
    "LogFloat": RF_LogFloat,
    "LogNumber": RF_LogNumber,
    "LogVec2": RF_LogVec2,
    "LogVec3": RF_LogVec3,

    # Json
    "RF_JsonStyleLoader": RF_JsonStyleLoader,

    # File
    "RF_SavePromptInfo": RF_SavePromptInfo
}

# This magic will use a property DISPLAY_NAME on each node to get the display name of the node for the UI
# This removees the need to define display names for all nodes in this file.
NODE_DISPLAY_NAME_MAPPINGS = {key: getattr(value, 'DISPLAY_NAME', None) for key, value in NODE_CLASS_MAPPINGS.items()}
