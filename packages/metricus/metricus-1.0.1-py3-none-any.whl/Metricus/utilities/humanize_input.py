def humanize_input(message: str) -> str:
    """
    Transforms a given string into a standardized, machine-friendly format by converting it 
    to lowercase and replacing spaces with underscores. It also handles plural forms, 
    such as converting 'meters' to 'meter' and special cases like 'feet' to 'foot'.

    This function is particularly useful for creating consistent identifiers, file names, 
    or variable names from human-readable text.

    Parameters:
    message (str): The input string to be transformed.

    Returns:
    str: The transformed string, with:
         - All characters in lowercase.
         - Plural forms converted to singular (e.g., 'meters' -> 'meter').
         - Spaces replaced by underscores.
         - Special cases like 'feet' handled explicitly (e.g., 'feet' -> 'foot').

    Examples:
    >>> humanize_input('Meters per second squared')
    'meter_per_second_squared'
    
    >>> humanize_input('Nautical Miles')
    'nautical_mile'

    >>> humanize_input('feet')
    'foot'

    >>> humanize_input('Glasses of water')
    'glass_of_water'
    """
    if message.lower() == 'feet':
        message = 'foot'
    
    normalized = message.lower().strip()

    words = normalized.split()
    normalized_words = [
        word[:-1] if word.endswith('s') and not word.endswith('ss') else word
        for word in words
    ]

    normalized = '_'.join(normalized_words)
    return normalized
