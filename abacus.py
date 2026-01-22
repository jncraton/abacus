class Rod:
    def __init__(self, upperBeadsUp=1, lowerBeadsUp=0):
        self.upperBeadsUp = upperBeadsUp
        self.lowerBeadsUp = lowerBeadsUp

    def __repr__(self):
        return str((self.upperBeadsUp, self.lowerBeadsUp))

class Abacus:
    """
    >>> Abacus()
    [(1, 0), (1, 0), (1, 0), (1, 0), (1, 0)]
    
    >>> Abacus([Rod(1, 1)]).rods[-1]
    (1, 1)
    """
    def __init__(self, rods = [], size=5):
        size = max(size, len(rods))
    
        # `size` Rods from left (0) to right (size)
        self.rods = [Rod() for _ in range(size)]

        # Set any provided rods pushing to the right
        for i, rod in enumerate(rods[::-1]):
            self.rods[-(i+1)] = rod

    def __repr__(self):
        return str(self.rods)



if __name__ == "__main__":
    import doctest
    doctest.testmod()