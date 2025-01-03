from viesvatcheck import parse_number


def test_parse():
    for value, result in [
        # Austria
        ("ATU99999999", ("AT", "U99999999")),
        # Belgium
        ("BE0999999999", ("BE", "0999999999")),
        ("BE1999999999", ("BE", "1999999999")),
        # Bulgaria
        ("BG999999999", ("BG", "999999999")),
        ("BG9999999999", ("BG", "9999999999")),
        # Cyprus
        ("CY99999999L", ("CY", "99999999L")),
        # Czech Republic
        ("CZ99999999", ("CZ", "99999999")),
        ("CZ999999999", ("CZ", "999999999")),
        ("CZ9999999999", ("CZ", "9999999999")),
        # Germany
        ("DE999999999", ("DE", "999999999")),
        # Denmark
        ("DK99 99 99 99", ("DK", "99999999")),
        # Estonia
        ("EE999999999", ("EE", "999999999")),
        # Greece
        ("EL999999999", ("EL", "999999999")),
        # Spain
        ("ESX9999999X", ("ES", "X9999999X")),
        # Finland
        ("FI99999999", ("FI", "99999999")),
        # France
        ("FRXX 999999999", ("FR", "XX999999999")),
        # Croatia
        ("HR99999999999", ("HR", "99999999999")),
        # Hungary
        ("HU99999999", ("HU", "99999999")),
        # Ireland
        ("IE9S99999L", ("IE", "9S99999L")),
        ("IE9999999WI", ("IE", "9999999WI")),
        # Italy
        ("IT99999999999", ("IT", "99999999999")),
        # Lithuania
        ("LT999999999", ("LT", "999999999")),
        ("LT999999999999", ("LT", "999999999999")),
        # Luxembourg
        ("LU99999999", ("LU", "99999999")),
        # Latvia
        ("LV99999999999", ("LV", "99999999999")),
        # Malta
        ("MT99999999", ("MT", "99999999")),
        # The Netherlands
        ("NLSSSSSSSSSSSS", ("NL", "SSSSSSSSSSSS")),
        # Poland
        ("PL9999999999", ("PL", "9999999999")),
        # Portugal
        ("PT999999999", ("PT", "999999999")),
        # Romania
        ("RO99", ("RO", "99")),
        ("RO999999999", ("RO", "999999999")),
        # Sweden
        ("SE999999999999", ("SE", "999999999999")),
        # Slovenia
        ("SI99999999", ("SI", "99999999")),
        # Slovakia
        ("SK9999999999", ("SK", "9999999999")),
        # Northern Ireland
        ("XI999 9999 99", ("XI", "999999999")),
        ("XI999 9999 99 999", ("XI", "999999999999")),
        ("XIGD999", ("XI", "GD999")),
        ("XIHA999", ("XI", "HA999")),
    ]:
        assert parse_number(value) == result
