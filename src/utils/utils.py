import logging
import re


def my_normalize_string(text: str) -> str:
    """Normalize a string. Primarily used to rename column names. Returns lower case words divided by underscores.
    Args:
        text: String to normalize.

    Returns:
        Normalized string.
    """
    reserved_words = ("date", "name", "type", "value", "charge")

    # 1. Insert an underscore between lowercase and uppercase letters.
    text = re.sub(r"([a-z])([A-Z])", r"\1_\2", text)

    # 2. Convert to lowercase.
    text = text.lower()

    # 3. Prefix reserved substrings unless they start at position zero.
    pattern = r"(?<!^)(?:" + "|".join(map(re.escape, reserved_words)) + r")"
    text = re.sub(pattern, r"_\g<0>", text)

    # 4. Replace consecutive non-alphanumeric with an underscore.
    text = re.sub(r"[^a-z0-9]+", "_", text)

    # 5. Remove non-alphanumeric characters from the beginning and end.
    text = re.sub(r"^[^a-z0-9]+|[^a-z0-9]+$", "", text)

    return text

def setup_logger(name: str, log_file: str, level=logging.INFO):
    """
    Creates and configures a logger.

    Args:
        name (str): Logger name.
        log_file (str): File to log to.
        level: Logging level.
    """
    handler = logging.FileHandler(log_file)        
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger