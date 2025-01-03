
import random
import dateutil
from datetime import datetime

def generate_random_int(min_value: int, max_value: int) -> int:
    """Generate a random integer between min_value and max_value."""
    return random.randint(min_value, max_value)

def parse_date(date_string: str) -> datetime:
    """Parse a date string."""
    return dateutil.parser.parse(date_string)

