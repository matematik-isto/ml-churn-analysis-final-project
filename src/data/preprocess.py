import pandas as pd


import re


def normalize_string(text: str) -> str:
    """Normalize a string for use as an identifier.

    Inserts underscores between lowercase and uppercase letters,
    converts the string to lowercase, replaces consecutive whitespace
    with underscores, strips non-alphanumeric characters from the ends,
    and prefixes reserved substrings except at the beginning.

    Args:
        text: String to normalize.

    Returns:
        Normalized string.
    """
    reserved_words = ("date", "name", "type", "value")

    # 1. Insert an underscore between lowercase and uppercase letters.
    text = re.sub(r"([a-z])([A-Z])", r"\1_\2", text)

    # 2. Convert to lowercase.
    text = text.lower()

    # 5. Prefix reserved substrings unless they start at position zero.
    pattern = r"(?<!^)(?:" + "|".join(map(re.escape, reserved_words)) + r")"
    text = re.sub(pattern, r"_\g<0>", text)

    # 3. Replace consecutive non-alphanumeric with an underscore.
    text = re.sub(r"[^a-z0-9]+", "_", text)

    # 4. Remove non-alphanumeric characters from the beginning and end.
    text = re.sub(r"^[^a-z0-9]+|[^a-z0-9]+$", "", text)

 

    # 6. Collapse consecutive underscores.
    #text = re.sub(r"_+", "_", text)

    return text

#def preprocess_data(df: pd.DataFrame, target_col: str = 'churn'):
test_string = '.value - name'
print(normalize_string(test_string))