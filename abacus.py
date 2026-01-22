class Rod:
    """
    A single rod on an  abacus representing a base 10 digit

    The upper bead represents 5 if the bead is **down**.

    Lower beads are worth one for each bead that is up.

    >>> Rod(0, 1)
    (0, 1)

    >>> Rod(1, 3)
    (1, 3)

    >>> Rod(2, 1)
    Traceback (most recent call last):
    ...
    ValueError: upperBeadsUp must be 0 or 1

    >>> Rod(-1, 1)
    Traceback (most recent call last):
    ...
    ValueError: upperBeadsUp must be 0 or 1

    >>> Rod(0, 5)
    Traceback (most recent call last):
    ...
    ValueError: lowerBeadsUp must be between 0 and 4

    >>> Rod(0, -1)
    Traceback (most recent call last):
    ...
    ValueError: lowerBeadsUp must be between 0 and 4
    """
    def __init__(self, upperBeadsUp=1, lowerBeadsUp=0):
        self.upperBeadsUp = upperBeadsUp
        self.lowerBeadsUp = lowerBeadsUp

    @property
    def upperBeadsUp(self):
        return self._upperBeadsUp

    @upperBeadsUp.setter
    def upperBeadsUp(self, value):
        if value not in (0, 1):
            raise ValueError("upperBeadsUp must be 0 or 1")
        self._upperBeadsUp = value

    @property
    def lowerBeadsUp(self):
        return self._lowerBeadsUp

    @lowerBeadsUp.setter
    def lowerBeadsUp(self, value):
        if not (0 <= value <= 4):
            raise ValueError("lowerBeadsUp must be between 0 and 4")
        self._lowerBeadsUp = value
        
    def __repr__(self):
        return str((self.upperBeadsUp, self.lowerBeadsUp))

    def __int__(self):
        """
        Convert this rod to an int

        >>> int(Rod())
        0

        >>> int(Rod(1, 0))
        0

        >>> int(Rod(1, 1))
        1

        >>> int(Rod(0, 3))
        8

        >>> int(Rod(1, 4))
        4
        """

class Abacus:
    """
    A soroban abacus

    An abacus is list of `Rod` entities accessible as the `rods` property
    
    >>> Abacus()
    [(1, 0), (1, 0), (1, 0), (1, 0), (1, 0)]
    
    >>> Abacus([Rod(1, 1)]).rods[-1]
    (1, 1)
    
    >>> print(Abacus())
    O O O O O
    | | | | |
    ---------
    | | | | |
    O O O O O
    O O O O O
    O O O O O
    O O O O O

    >>> print(Abacus([Rod(1, 1)]))
    O O O O O
    | | | | |
    ---------
    | | | | O
    O O O O |
    O O O O O
    O O O O O
    O O O O O

    >>> print(Abacus([Rod(0, 1), Rod(1, 3)]))
    O O O | O
    | | | O |
    ---------
    | | | O O
    O O O | O
    O O O O O
    O O O O |
    O O O O O
    
    >>> print(Abacus([Rod(0, 1), Rod(1, 4)]))
    O O O | O
    | | | O |
    ---------
    | | | O O
    O O O | O
    O O O O O
    O O O O O
    O O O O |
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

    def __str__(self):
        """
        Returns an ASCII representation of the current state
        """
        return "\n".join([
            " ".join("O" if r.upperBeadsUp == 1 else "|" for r in self.rods),
            " ".join("|" if r.upperBeadsUp == 1 else "O" for r in self.rods),
            "-" * (len(self.rods) * 2 - 1),
        ] + [
            " ".join('|' if i == r.lowerBeadsUp else 'O' for r in self.rods) for i in range(5)
        ])

    def __repr__(self):
        return str(self.rods)



if __name__ == "__main__":
    import doctest
    doctest.testmod()