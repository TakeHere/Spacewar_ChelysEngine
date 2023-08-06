class Color:
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def get_array(self):
        return {self.r, self.g, self.b, self.a}

    def get_hex(self):
        hex_code = "#{:02x}{:02x}{:02x}".format(self.r, self.g, self.b)
        return hex_code

    def get_hex_with_alpha(self):
        hex_code = "#{:02x}{:02x}{:02x}{:02x}".format(self.r, self.g, self.b, self.a)
        return hex_code
