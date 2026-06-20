import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.etl.normaliser import normalize_year, normalize_ticker

# ---------- normalize_year tests ----------

assert normalize_year("Dec 2012") == 2012
assert normalize_year("Mar 2014") == 2014
assert normalize_year("Mar-13") == 2013
assert normalize_year("Mar-24") == 2024
assert normalize_year("Mar-20") == 2020
assert normalize_year("Mar-21") == 2021
assert normalize_year("Mar-22") == 2022
assert normalize_year("Mar-23") == 2023
assert normalize_year("Mar-25") == 2025
assert normalize_year("Mar-19") == 2019

assert normalize_year("Jan 2018") == 2018
assert normalize_year("Feb 2017") == 2017
assert normalize_year("Apr 2016") == 2016
assert normalize_year("May 2015") == 2015
assert normalize_year("Jun 2014") == 2014
assert normalize_year("Jul 2013") == 2013
assert normalize_year("Aug 2012") == 2012
assert normalize_year("Sep 2011") == 2011
assert normalize_year("Oct 2010") == 2010
assert normalize_year("Nov 2009") == 2009

# ---------- normalize_ticker tests ----------

assert normalize_ticker("tcs") == "TCS"
assert normalize_ticker(" TCS ") == "TCS"
assert normalize_ticker("infy") == "INFY"
assert normalize_ticker(" INFY ") == "INFY"
assert normalize_ticker("reliance") == "RELIANCE"
assert normalize_ticker(" hdfcbank ") == "HDFCBANK"
assert normalize_ticker("axisbank") == "AXISBANK"
assert normalize_ticker("sbin") == "SBIN"
assert normalize_ticker("itc") == "ITC"
assert normalize_ticker("abb") == "ABB"

assert normalize_ticker("adanient") == "ADANIENT"
assert normalize_ticker("asianpaint") == "ASIANPAINT"
assert normalize_ticker("nestleind") == "NESTLEIND"
assert normalize_ticker("sunpharma") == "SUNPHARMA"
assert normalize_ticker("tatamotors") == "TATAMOTORS"

print("35 tests passed!")