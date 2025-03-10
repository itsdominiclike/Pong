class KeyPresses:
    """Handles key press and release states for paddle movement."""

    def __init__(self):
        """Initializes the key press states for movement."""
        self.up_pressed = False   # Tracks whether the up key is currently held
        self.down_pressed = False # Tracks whether the down key is currently held

    def up_press(self):
        """Sets up_pressed to True when the up key is pressed."""
        self.up_pressed = True

    def up_release(self):
        """Sets up_pressed to False when the up key is released."""
        self.up_pressed = False

    def down_press(self):
        """Sets down_pressed to True when the down key is pressed."""
        self.down_pressed = True

    def down_release(self):
        """Sets down_pressed to False when the down key is released."""
        self.down_pressed = False