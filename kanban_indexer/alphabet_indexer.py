class AlphabetIndexer:
    """
    A class that provides indexing functionality for a given alphabet.

    This class creates a bidirectional mapping between characters in the alphabet
    and their corresponding integer indices. It also provides utility methods
    for converting between characters and indices, and properties for accessing
    special characters in the alphabet.

    The alphabet is expected to be a sorted string of unique characters.
    """

    def __init__(self, alphabet: str):
        """
        Initialize the AlphabetIndexer with a given alphabet.

        Args:
            alphabet (str): A sorted string of unique characters representing the alphabet.

        Raises:
            ValueError: If the provided alphabet is not sorted or contains duplicate characters.
        """
        # Verify that the alphabet is sorted and contains unique characters
        if list(alphabet) != sorted(set(alphabet)):
            raise ValueError(
                "The provided alphabet must be sorted and contain unique characters."
            )

        # Create bidirectional mappings between characters and their indices
        self.char_to_int = {char: i for i, char in enumerate(alphabet)}
        self.int_to_char = {i: char for i, char in enumerate(alphabet)}
        self.alphabet = alphabet

    def to_int(self, char) -> int:
        return self.char_to_int[char]

    def to_char(self, i) -> str:
        return self.int_to_char[i]

    @property
    def start(self) -> str:
        return self.alphabet[0]

    @property
    def end(self) -> str:
        return self.alphabet[-1]

    @property
    def midpoint(self) -> str:
        """
        Get the middle character of the alphabet.

        For even-length alphabets, returns the character to the left of the midpoint.
        For odd-length alphabets, returns the exact midpoint character.

        Returns:
            str: The middle character of the alphabet.
        """
        mid_index = (len(self.alphabet) - 1) // 2
        return self.alphabet[mid_index]
