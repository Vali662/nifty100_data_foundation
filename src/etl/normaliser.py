def normalize_year(year):
    """
    Extract year from:
    Dec 2012 -> 2012
    Mar 2014 -> 2014
    Mar-13   -> 2013
    """

    if year is None:
        return None

    year = str(year).strip()

    if "-" in year:
        yy = int(year.split("-")[-1])

        if yy <= 30:
            return 2000 + yy
        else:
            return 1900 + yy

    return int(year[-4:])


def normalize_ticker(ticker):
    """
    Standardize ticker symbols.
    Example:
    ' tcs ' -> 'TCS'
    """

    if ticker is None:
        return None

    return str(ticker).strip().upper()


print(normalize_year("Dec 2012"))
print(normalize_year("Mar 2014"))
print(normalize_year("Mar-13"))
print(normalize_year("Mar-24"))

print(normalize_ticker(" tcs "))