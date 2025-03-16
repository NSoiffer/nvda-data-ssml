from NVDAObjects.IAccessible import IAccessible
import speech
from logHandler import log

class CustomSpanOverlay(IAccessible):
    """
    Custom overlay class for span elements with the data-ssml attribute.
    """

    def event_gainFocus(self):
        """
        Handle the gainFocus event for objects with the data-ssml attribute.
        """
        log.info("CustomSpanOverlay gainFocus")
        if self.HTMLAttributes and "data-ssml" in self.HTMLAttributes:
            # Announce a custom message
            speech.speak("I found data-ssml")
        else:
            # Call the default implementation
            super().event_gainFocus()

