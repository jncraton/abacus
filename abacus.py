class Rod:
    """
    A single rod on an  abacus representing a base 10 digit

    The upper bead represents 5 if the bead is **down**.

    Lower beads are worth one for each bead that is up.
    """
    def __init__(self, upperBeadsUp=1, lowerBeadsUp=0):
        self.upperBeadsUp = upperBeadsUp
        self.lowerBeadsUp = lowerBeadsUp

    def __repr__(self):
        return str((self.upperBeadsUp, self.lowerBeadsUp))

class Abacus:
    """
    An abacus

    An abacus is list of `Rod` entities accessible as the `rods` property
    
    >>> Abacus()
    [(1, 0), (1, 0), (1, 0), (1, 0), (1, 0)]
    
    >>> Abacus([Rod(1, 1)]).rods[-1]
    (1, 1)
    """
    def __init__(self, rods = [], size=5):
        """
        Instantiate an abacus

        @param rods: A list of as initial abacus state, pushed right
        @param size: The total width of the abaucs
        """
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