# cell.py
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_wet = False
        self.is_sunny = False

    def dry_off(self):
        """Sets the cell to be dry."""
        self.is_wet = False

    def set_sun(self, is_sunny):
        """Sets the cell's sun state."""
        self.is_sunny = is_sunny

    def become_wet(self):
        """Sets the cell to be wet."""
        self.is_wet = True

    def get_char(self):
        """Returns the character for the cell's current state."""
        if self.is_sunny and self.is_wet:
            return "♨ "  # Steaming
        elif self.is_sunny:
            return "☀ "  # Sunny
        elif self.is_wet:
            return "🌧 "  # Wet and cloudy
        else:
            return "☁ "  # Dry and cloudy
        # else: 
            # retrun apocalypse, meteor, or smth