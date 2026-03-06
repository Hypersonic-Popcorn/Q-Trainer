# register_plwidgets.py
#
# Qt Designer plugin registration for pl-widgets 0.1.1
#
# IMPORTANT: This file MUST start with "register" for pyside6-designer to find it.
#
# Place this file in:
#   /home/aria/projects/python/Q-Trainer/designer_plugins/
#
# Removed from registration (not suitable for Designer):
#   - PlDialog        : base class, broken backgroundColor property metacall
#   - PlOverlayDialog : requires a real parent at __init__ time; crashes with None
#
# Fixed:
#   - PLSlider casing (it's PLSlider, not PlSlider, in the actual source)

from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection

try:
    from plwidgets import PlWidgets
except ImportError as e:
    raise ImportError(
        "Could not import plwidgets. Make sure your venv is active and "
        "plwidgets 0.1.1 is installed:\n"
        "  pip install plwidgets==0.1.1\n"
        f"Original error: {e}"
    )

_GROUP  = "PL Widgets"
_MODULE = "plwidgets.PlWidgets"

def _xml(class_name, tooltip=""):
    instance = class_name[0].lower() + class_name[1:]
    return (
        f'<ui language="c++">'
        f'<widget class="{class_name}" name="{instance}">'
        f'<property name="toolTip"><string>{tooltip}</string></property>'
        f'</widget></ui>'
    )

# 1. PlCheckBox
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlCheckBox,
    xml=_xml("PlCheckBox", "Custom checkbox with styling"),
    tool_tip="Custom checkbox with styling",
    group=_GROUP,
    module=_MODULE,
)

# 2. PlCheckButtonGroup
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlCheckButtonGroup,
    xml=_xml("PlCheckButtonGroup", "Group of toggle buttons (single or multi-select)"),
    tool_tip="Group of toggle buttons (single or multi-select)",
    group=_GROUP,
    module=_MODULE,
)

# 3. PlComboBox
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlComboBox,
    xml=_xml("PlComboBox", "Styled dropdown selector"),
    tool_tip="Styled dropdown selector",
    group=_GROUP,
    module=_MODULE,
)

# 4. PlFlag (container)
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlFlag,
    xml=_xml("PlFlag", "Titled content container with a styled header"),
    tool_tip="Titled content container with a styled header",
    group=_GROUP,
    module=_MODULE,
    container=True,
)

# 5. PlFormWidget (container)
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlFormWidget,
    xml=_xml("PlFormWidget", "Labeled horizontal layout for form elements"),
    tool_tip="Labeled horizontal layout for form elements",
    group=_GROUP,
    module=_MODULE,
    container=True,
)

# 6. PlLineEdit
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlLineEdit,
    xml=_xml("PlLineEdit", "Styled single-line text input"),
    tool_tip="Styled single-line text input",
    group=_GROUP,
    module=_MODULE,
)

# 7. PlLoadingIndicator
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlLoadingIndicator,
    xml=_xml("PlLoadingIndicator", "Animated loading spinner"),
    tool_tip="Animated loading spinner",
    group=_GROUP,
    module=_MODULE,
)

# 8. PlProgressCircle
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlProgressCircle,
    xml=_xml("PlProgressCircle", "Circular progress indicator with text"),
    tool_tip="Circular progress indicator with text",
    group=_GROUP,
    module=_MODULE,
)

# 9. PlPushButton
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlPushButton,
    xml=_xml("PlPushButton", "Custom push button with hover and press effects"),
    tool_tip="Custom push button with hover and press effects",
    group=_GROUP,
    module=_MODULE,
)

# 10. PlRoundCheckButton
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlRoundCheckButton,
    xml=_xml("PlRoundCheckButton", "Rounded toggle button (styled checkbox)"),
    tool_tip="Rounded toggle button (styled checkbox)",
    group=_GROUP,
    module=_MODULE,
)

# 11. PlSearchBar
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlSearchBar,
    xml=_xml("PlSearchBar", "Input with icon for search actions"),
    tool_tip="Input with icon for search actions",
    group=_GROUP,
    module=_MODULE,
)

# 12. PLSlider (note: all-caps PL, confirmed from source)
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PLSlider,
    xml=_xml("PLSlider", "Custom horizontal slider"),
    tool_tip="Custom horizontal slider",
    group=_GROUP,
    module=_MODULE,
)

# 13. PlTabWidget (container)
QPyDesignerCustomWidgetCollection.registerCustomWidget(
    PlWidgets.PlTabWidget,
    xml=_xml("PlTabWidget", "Custom tab navigation with painted tabs"),
    tool_tip="Custom tab navigation with painted tabs",
    group=_GROUP,
    module=_MODULE,
    container=True,
)
