class Quark:
    allowed_colors = ['red', 'blue', 'green']
    allowed_flavors = ['up', 'down', 'strange', 'charm', 'top', 'bottom']
    baryon_number = 1 / 3

    def __init__(self, color, flavor):
        if color not in Quark.allowed_colors:
            raise ValueError(f"Invalid color: {color}. Allowed colors: {Quark.allowed_colors}")
        if flavor not in Quark.allowed_flavors:
            raise ValueError(f"Invalid flavor: {flavor}. Allowed flavors: {Quark.allowed_flavors}")
        self.color = color
        self.flavor = flavor

    def interact(self, other_quark):
        if not isinstance(other_quark, Quark):
            raise TypeError("Can only interact with another Quark object.")
        self.color, other_quark.color = other_quark.color, self.color

q1 = Quark("red", "up")
print(q1.color)
print(q1.flavor)
q2 = Quark("blue", "strange")
print(q2.color)
print(q2.baryon_number)
q1.interact(q2)
print(q1.color)
print(q2.color)
