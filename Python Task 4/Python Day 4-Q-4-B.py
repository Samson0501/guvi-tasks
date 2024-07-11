class TV:
    def __init__(self, brand):
        # Initialize basic TV attributes
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.on = False

    def increase_volume(self):
        # Increase volume by 1, max limit is 100
        if self.volume < 100:
            self.volume += 1
        self.print_status()

    def decrease_volume(self):
        # Decrease volume by 1, min limit is 0
        if self.volume > 0:
            self.volume -= 1
        self.print_status()

    def set_channel(self, channel):
        # Set channel within range 1 to 50
        if 1 <= channel <= 50:
            self.channel = channel
        self.print_status()

    def reset(self):
        # Reset channel to 1 and volume to 50
        self.channel = 1
        self.volume = 50
        self.print_status()

    def print_status(self):
        # Print current status of the TV
        on_status = "ON" if self.on else "OFF"
        print(f"{self.brand} at channel {self.channel}, volume {self.volume}, {on_status}")

    def toggle_power(self):
        # Toggle power state of the TV
        self.on = not self.on
        if self.on:
            self.print_status()
        else:
            print(f"{self.brand} is now OFF")


class SmartTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        # Initialize SmartTV attributes and inherit from TV
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = None
        self.backlight = None
        self.display_details = None

    def set_viewing_angle(self, angle):
        # Set viewing angle of the TV
        self.viewing_angle = angle

    def set_backlight(self, backlight_type):
        # Set backlight type of the TV
        self.backlight = backlight_type

    def set_display_details(self, resolution):
        # Set display details of the TV
        self.display_details = resolution

    def print_details(self):
        # Print detailed information about the SmartTV
        self.print_status()
        print(f"Screen Thickness: {self.screen_thickness} mm")
        print(f"Energy Usage: {self.energy_usage}")
        print(f"Lifespan: {self.lifespan} years")
        print(f"Refresh Rate: {self.refresh_rate} Hz")
        if self.viewing_angle:
            print(f"Viewing Angle: {self.viewing_angle} degrees")
        if self.backlight:
            print(f"Backlight: {self.backlight}")
        if self.display_details:
            print(f"Display Details: {self.display_details}")


# Example usage:
samsung_smart_tv = SmartTV("Samsung", 10, "A++", 10, 120)
samsung_smart_tv.toggle_power()
samsung_smart_tv.increase_volume()
samsung_smart_tv.set_channel(8)
samsung_smart_tv.set_viewing_angle(178)
samsung_smart_tv.set_backlight("LED")
samsung_smart_tv.set_display_details("4K Ultra HD")
samsung_smart_tv.print_details()
