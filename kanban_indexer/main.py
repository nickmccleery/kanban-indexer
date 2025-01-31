"""
This module implements a lexicographic indexing system for (user configurable) ordered
collections, such as a column on a Kanban board.

It uses a base-26 system (A-Z) to generate indices, allowing for ~infinite
insertions between any two existing indices without the need for reindexing.
The system avoids floating-point precision issues by using string comparisons—also
making the indices readily human-readable.

Key features:
- Indices are strings composed of characters A-Z
- Lexicographic ordering determines item placement
- New indices are generated at the midpoint between existing indices
- The default range is (A, Z], allowing insertions before the first item

Example: Between indices "B" and "C", a new item would receive index "BM".
"""

from kanban_indexer.alphabet_indexer import AlphabetIndexer

# Define our alphabet and create AlphabetIndexer map instance.
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA_MAP = AlphabetIndexer(ALPHABET)

ALPHABET_START = ALPHA_MAP.start
ALPHABET_END = ALPHA_MAP.end
ALPHABET_MIDPOINT = ALPHA_MAP.midpoint

# Set our first index value for a new/empty column.
INIT_ORDINAL = ALPHA_MAP.to_int(ALPHABET_START) + 1
INIT_INDEX = ALPHA_MAP.to_char(INIT_ORDINAL)


def get_new_index() -> str:
    """
    Retrieves an initial index for a new column.

    Returns:
        str: The new index.
    """
    return INIT_INDEX


def validate_index(index: str) -> None:
    """
    Validates the given index string.

    Args:
        index (str): The index string to be validated.

    Raises:
        ValueError: If the index contains any character that is not in the range
                    [ALPHABET_START, ALPHABET_END] or if the index ends with
                    ALPHABET_START.

    Returns:
        None
    """
    # Index is invalid if any character is not in [ALPHABET_START and ALPHABET_END].
    if any(char not in ALPHA_MAP.char_to_int for char in index):
        raise ValueError(
            f"Invalid index: '{index}'. "
            f"Characters must be in range ('{ALPHABET_START}', '{ALPHABET_END}']."
        )

    # Index is invalid it ever ends with ALPHABET_START.
    if index.endswith(ALPHABET_START):
        raise ValueError(
            f"Invalid index: '{index}'. " f"Index cannot end with '{ALPHABET_START}'."
        )


def compute_midpoint(ordinal_a: int, ordinal_b: int) -> int:
    """
    Computes the midpoint between two values.

    Args:
        ordinal_a (int): The first ordinal value.
        ordinal_b (int): The second ordinal value.

    Returns:
        int: The midpoint between the two values.
    """
    return (ordinal_a + ordinal_b) // 2


def compute_intermediate_index(index_before: str, index_after: str):
    """
    Computes the intermediate index between two given indices using an expansion flag approach.

    Args:
        index_before (str): The index of the item 'before' the target position.
        index_after (str): The index of the item 'after' the target position.

    Returns:
        str: The computed intermediate index.

    Raises:
        ValueError: If the input indices are not valid.
    """
    # Validate input indices.
    validate_index(index_before)
    validate_index(index_after)

    # Flip order if necessary.
    if index_before > index_after:
        index_before, index_after = index_after, index_before

    intermediate_index = ""
    expand_flag = False
    max_length = max(len(index_before), len(index_after))

    for i in range(max_length):
        # Get the ordinal values, using ALPHABET_START as default for padding.
        lo = (
            ALPHA_MAP.to_int(index_before[i])
            if i < len(index_before)
            else ALPHA_MAP.to_int(ALPHABET_START)
        )

        # For the high value, use ALPHABET_END.
        hi = (
            ALPHA_MAP.to_int(index_after[i])
            if (i < len(index_after) and not expand_flag)
            else ALPHA_MAP.to_int(ALPHABET_END)
        )

        if lo == hi:
            intermediate_index += ALPHA_MAP.to_char(lo)
        elif (hi - lo) > 1:
            intermediate_index += ALPHA_MAP.to_char(compute_midpoint(lo, hi))
            expand_flag = False
            return intermediate_index
        else:
            intermediate_index += ALPHA_MAP.to_char(lo)
            expand_flag = True

    if expand_flag:
        intermediate_index += ALPHABET_MIDPOINT

    return intermediate_index


def compute_preceding_index(index: str) -> str:
    """
    Returns the preceding index value based on the given index.

    Args:
        index (str): The index value.

    Returns:
        str: The preceding index value.

    Raises:
        ValueError: If the index is not valid.
    """
    validate_index(index)

    # Iterate backwards through the string.
    for i in range(len(index) - 1, -1, -1):
        cur_char_ordinal = ALPHA_MAP.to_int(index[i])

        if cur_char_ordinal > INIT_ORDINAL:
            # Decrement least significant character, e.g. CC -> CB.
            return index[:i] + ALPHA_MAP.to_char(cur_char_ordinal - 1) + index[i + 1 :]

    # If we've reached here, all characters were at INIT_ORDINAL already.
    # Expand string and replace previously least significant char,
    # e.g. BB -> BAZ.
    return index[:-1] + ALPHABET_START + ALPHABET_END


def compute_succeeding_index(index: str) -> str:
    """
    Returns the succeeding index based on the given index.

    Args:
        index (str): The index to find the succeeding index for.

    Returns:
        str: The succeeding index.

    Raises:
        ValueError: If the index is not valid.
    """
    validate_index(index)

    if index[-1] == ALPHABET_END:
        # If the last character is Z, append INIT_INDEX.
        return index + INIT_INDEX

    # Otherwise, increment the last character.
    return index[:-1] + ALPHA_MAP.to_char(ALPHA_MAP.to_int(index[-1]) + 1)
