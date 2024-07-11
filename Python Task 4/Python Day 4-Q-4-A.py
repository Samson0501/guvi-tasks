class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.on = False
#Specifying the TV brand and the channel and volume
    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
        self.print_status()
#printing to display the updated status of the TV
    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
        self.print_status()

    def set_channel(self, channel): #Setting the channel to the specified value within range of 1 to 50.
        if 1 <= channel <= 50:
            self.channel = channel
        self.print_status()

    def reset(self): #Resets the TV to default settings and channel set to 1 and volume set to 50.
        self.channel = 1
        self.volume = 50
        self.print_status()

    def print_status(self): #Prints the current status of the TV including brand, channel, volume, and power state
        on_status = "ON" if self.on else "OFF"
        print(f"{self.brand} at channel {self.channel}, volume {self.volume}, {on_status}")

    def toggle_power(self):
        self.on = not self.on
        if self.on:
            self.print_status()
        else:
            print(f"{self.brand} is now OFF")


# Example usage:
panasonic_tv = TV("Panasonic")

panasonic_tv.toggle_power()
panasonic_tv.increase_volume()
panasonic_tv.set_channel(8)
panasonic_tv.increase_volume()
panasonic_tv.decrease_volume()
panasonic_tv.set_channel(60)
panasonic_tv.reset()
panasonic_tv.toggle_power()
