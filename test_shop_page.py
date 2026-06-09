def valid_serial_number(serial_number):
    if not (7 <= len(serial_number) <= 10):
        return False

    year_part = serial_number[:4]
    if not year_part.isdigit():
        return False

    year = int(year_part)
    if year < 1990:
        return False

    if serial_number[4] != "_":
        return False

    return True

def test_valid_min_length():
    assert valid_serial_number("2023_AB") == True

def test_valid_max_length():
    assert valid_serial_number("2023_ABCDE") == True

def test_invalid_too_short():
    assert valid_serial_number("2023_A") == False

def test_invalid_too_long():
    assert valid_serial_number("2023_ABCDEF") == False

def test_valid_boundary_year():
    assert valid_serial_number("1990_ABC") == True

def test_invalid_boundary_year():
    assert valid_serial_number("1989_ABC") == False

def test_invalid_letters_in_year():
    assert valid_serial_number("ABCD_XYZ") == False

def test_invalid_partial_letters_in_year():
    assert valid_serial_number("20AB_XYZ") == False

def test_invalid_empty_string():
    assert valid_serial_number("") == False

def test_invalid_no_symb_after_underscore():
    assert valid_serial_number("2023_") == False