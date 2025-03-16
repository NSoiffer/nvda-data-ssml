import globalPluginHandler                  # we are a global plugin
import speech
from logHandler import log  # logging
from NVDAObjects.IAccessible import IAccessible
import addonHandler


# Import the _ function for translation
# _ = wx.GetTranslation
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        log.info("Data SSML Handler initialized")
        # Register the event listener when the plugin is loaded
        # self.registerEventListener("gainFocus", self.on_gainFocus)

    # Register the overlay class with NVDA
    def chooseNVDAObjectOverlayClass(self, obj, clsList):
        """
        Automatically choose the CustomSpanOverlay for objects with the data-ssml attribute.
        """
        log.info("Applying CustomSpanOverlay to object with data-ssml attribute")
        if isinstance(obj, IAccessible) and obj.HTMLAttributes and "data-ssml" in obj.HTMLAttributes:
            clsList.insert(0, CustomSpanOverlay)

    def on_gainFocus(self, obj):
        """
        Custom handler for the gainFocus event.
        """
        if isinstance(obj, IAccessible):
            # Check if the HTML attributes contain 'data-ssml'
            try:
                attributes = obj.HTMLAttributes
                if attributes and "data-ssml" in attributes:
                    # Announce the custom message
                    speech.speak("I found data-ssml")
            except Exception:
                # Handle any potential errors gracefully
                pass

    def terminate(self):
        # Clean up resources
        pass
