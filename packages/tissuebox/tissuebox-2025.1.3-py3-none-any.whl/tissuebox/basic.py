import re
from datetime import datetime
from decimal import Decimal
from ipaddress import ip_address
from urllib.parse import urlparse


# Existing core type validators
def integer(x):
    if isinstance(x, bool):
        return False
    return isinstance(x, int)


integer.msg = "integer"


def numeric(x):
    if isinstance(x, bool):
        return False
    return isinstance(x, (int, float, Decimal))


numeric.msg = "numeric"


def complex_number(x):
    return isinstance(x, complex)


complex_number.msg = "complex number"


def string(x):
    return isinstance(x, str)


string.msg = "string"


def array(x):
    return isinstance(x, list)


array.msg = "list"


def dictionary(x):
    return isinstance(x, dict)


dictionary.msg = "dictionary"


def boolean(x):
    return isinstance(x, bool)


boolean.msg = "boolean"


def null(x):
    return x is None


null.msg = "null"


# Enhanced string validators
def length(min_len=None, max_len=None):
    """Validate string length is within range"""

    def validator(x):
        if not isinstance(x, str):
            return False
        if min_len is not None and len(x) < min_len:
            return False
        if max_len is not None and len(x) > max_len:
            return False
        return True

    msg_parts = []
    if min_len is not None:
        msg_parts.append(f"at least {min_len} characters")
    if max_len is not None:
        msg_parts.append(f"at most {max_len} characters")

    validator.msg = f"string with {' and '.join(msg_parts)}"
    return validator


def pattern(regex, flags=0):
    """Validate string matches regex pattern"""

    def validator(x):
        if not isinstance(x, str):
            return False
        return bool(re.match(regex, x, flags))

    validator.msg = f"string matching pattern {regex}"
    return validator


def alpha():
    """Validate string contains only letters"""

    def validator(x):
        if not isinstance(x, str):
            return False
        return x.isalpha()

    validator.msg = "string containing only letters"
    return validator


def alphanumeric():
    """Validate string contains only letters and numbers"""

    def validator(x):
        if not isinstance(x, str):
            return False
        return x.isalnum()

    validator.msg = "string containing only letters and numbers"
    return validator


def lowercase():
    """Validate string is lowercase"""

    def validator(x):
        if not isinstance(x, str):
            return False
        return x.islower()

    validator.msg = "lowercase string"
    return validator


def uppercase():
    """Validate string is uppercase"""

    def validator(x):
        if not isinstance(x, str):
            return False
        return x.isupper()

    validator.msg = "uppercase string"
    return validator


# Number validators
def positive(x):
    """Validate number is positive"""
    if not numeric(x):
        return False
    return x > 0


positive.msg = "positive number"


def negative(x):
    """Validate number is negative"""
    if not numeric(x):
        return False
    return x < 0


negative.msg = "negative number"


def between(min_val=None, max_val=None):
    """Validate number is within range"""

    def validator(x):
        if not numeric(x):
            return False
        if min_val is not None and x < min_val:
            return False
        if max_val is not None and x > max_val:
            return False
        return True

    msg_parts = []
    if min_val is not None:
        msg_parts.append(f"greater than or equal to {min_val}")
    if max_val is not None:
        msg_parts.append(f"less than or equal to {max_val}")

    validator.msg = f"number {' and '.join(msg_parts)}"
    return validator


def even(x):
    """Validate number is even"""
    if not integer(x):
        return False
    return x % 2 == 0


even.msg = "even number"


def odd(x):
    """Validate number is odd"""
    if not integer(x):
        return False
    return x % 2 != 0


odd.msg = "odd number"


# Date and time validators
def iso_date(x):
    """Validate string is ISO format date"""
    if not isinstance(x, str):
        return False
    try:
        datetime.fromisoformat(x)
        return True
    except ValueError:
        return False


iso_date.msg = "ISO format date string (YYYY-MM-DD)"


def future_date():
    """Validate date is in the future"""

    def validator(x):
        if not isinstance(x, str):
            return False
        try:
            date = datetime.fromisoformat(x)
            return date > datetime.now()
        except ValueError:
            return False

    validator.msg = "future date"
    return validator


def past_date():
    """Validate date is in the past"""

    def validator(x):
        if not isinstance(x, str):
            return False
        try:
            date = datetime.fromisoformat(x)
            return date < datetime.now()
        except ValueError:
            return False

    validator.msg = "past date"
    return validator


# Array validators
def min_length(min_len):
    """Validate array has minimum length"""

    def validator(x):
        if not array(x):
            return False
        return len(x) >= min_len

    validator.msg = f"array with at least {min_len} items"
    return validator


def max_length(max_len):
    """Validate array has maximum length"""

    def validator(x):
        if not array(x):
            return False
        return len(x) <= max_len

    validator.msg = f"array with at most {max_len} items"
    return validator


# Web-related validators
def email(x):
    """Validate email address"""
    if not isinstance(x, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, x))


email.msg = "valid email address"


def url(x):
    """Validate URL"""
    if not isinstance(x, str):
        return False
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


url.msg = "valid URL"


def ip_address_str(x):
    """Validate IP address (v4 or v6)"""
    if not isinstance(x, str):
        return False
    try:
        ip_address(x)
        return True
    except ValueError:
        return False


ip_address_str.msg = "valid IP address"


def ipv4(x):
    """Validate IPv4 address"""
    if not isinstance(x, str):
        return False
    try:
        addr = ip_address(x)
        return addr.version == 4
    except ValueError:
        return False


ipv4.msg = "valid IPv4 address"


def ipv6(x):
    """Validate IPv6 address"""
    if not isinstance(x, str):
        return False
    try:
        addr = ip_address(x)
        return addr.version == 6
    except ValueError:
        return False


ipv6.msg = "valid IPv6 address"


def hostname(x):
    """Validate hostname"""
    if not isinstance(x, str):
        return False
    if len(x) > 255:
        return False
    pattern = r"^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    return bool(re.match(pattern, x))


hostname.msg = "valid hostname"


# Specialized string validators
def uuid4(x):
    """Validate UUID v4"""
    if not isinstance(x, str):
        return False
    pattern = r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
    return bool(re.match(pattern, x, re.I))


uuid4.msg = "valid UUID v4"


def slug(x):
    """Validate slug (URL-friendly string)"""
    if not isinstance(x, str):
        return False
    pattern = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
    return bool(re.match(pattern, x))


slug.msg = "valid slug (lowercase letters, numbers, hyphens)"


def hex_color(x):
    """Validate hex color code"""
    if not isinstance(x, str):
        return False
    pattern = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
    return bool(re.match(pattern, x))


hex_color.msg = "valid hex color code"


def credit_card(x):
    """Validate credit card number using Luhn algorithm"""
    if not isinstance(x, str):
        return False

    # Remove spaces and hyphens
    x = x.replace(" ", "").replace("-", "")

    if not x.isdigit():
        return False

    # Luhn algorithm
    digits = [int(d) for d in x]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    return sum(digits) % 10 == 0


credit_card.msg = "valid credit card number"


def phone(country_code=None):
    """Validate phone number"""

    def validator(x):
        if not isinstance(x, str):
            return False

        # Remove common separators
        x = re.sub(r"[\s\-\(\)]", "", x)

        if country_code == "US":
            pattern = r"^\+?1?\d{10}$"
        else:
            # Generic international format
            pattern = r"^\+?[1-9]\d{1,14}$"

        return bool(re.match(pattern, x))

    validator.msg = "valid phone number"
    if country_code:
        validator.msg += f" ({country_code} format)"
    return validator


def password_strength(min_length=8, require_special=True):
    """Validate password strength"""

    def validator(x):
        if not isinstance(x, str):
            return False

        if len(x) < min_length:
            return False

        # Check for at least one uppercase, lowercase, and digit
        if not (any(c.isupper() for c in x) and any(c.islower() for c in x) and any(c.isdigit() for c in x)):
            return False

        if require_special:
            special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
            if not any(c in special_chars for c in x):
                return False

        return True

    validator.msg = f"password with minimum length {min_length}, mixed case, numbers" + (" and special characters" if require_special else "")
    return validator


# Data format validators
def json_string(x):
    """Validate JSON string"""
    if not isinstance(x, str):
        return False
    try:
        import json

        json.loads(x)
        return True
    except ValueError:
        return False


json_string.msg = "valid JSON string"


def base64(x):
    """Validate base64 string"""
    if not isinstance(x, str):
        return False
    pattern = r"^[A-Za-z0-9+/]*={0,2}$"
    return bool(re.match(pattern, x))


base64.msg = "valid base64 string"


# Geographic validators
def latitude(x):
    """Validate latitude"""
    if not numeric(x):
        return False
    return -90 <= float(x) <= 90


latitude.msg = "valid latitude (-90 to 90)"


def longitude(x):
    """Validate longitude"""
    if not numeric(x):
        return False
    return -180 <= float(x) <= 180


longitude.msg = "valid longitude (-180 to 180)"


# Required field validator (existing)
def required(x):
    """Required field validator - always returns True as it just checks presence"""
    return True


required.msg = "required"


def lt(n):
    def lt(x):
        return x < n

    lt.msg = f"less than {n}"
    return lt


def gt(n):
    def gt(x):
        return x < n

    gt.msg = f"greater than {n}"
    return lt


def divisible(n):
    def divisible(x):
        return numeric(x) and numeric(n) and x % n == 0

    divisible.msg = f"multiple of {n}"
    return divisible
