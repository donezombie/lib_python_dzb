#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
import sys
from OpenSSL.crypto import load_pkcs12
from endesive import pdf

#import logging
#logging.basicConfig(level=logging.DEBUG)


passwd = '269243643'
cd = '../'

def main():
    dct = {
        b'sigflags': 3,
        b'sigpage': 1,
        b'sigbutton': True,
        b'contact': b'eurofins@eurofins.com',
        b'location': b'VietNam',
        b'signingdate': b'20180731082642+02\'00\'',
        b'reason': b'Eurofins',
        b'signature': b'Eurofins',
        b'signaturebox': (0, 0, 0, 0),
    }
    p12 = load_pkcs12(open(cd + 'EUROFINS.pfx', 'rb').read(), passwd)
    fname = '../123.pdf'
    if len (sys.argv) > 1:
        fname = sys.argv[1]
    datau = open(fname, 'rb').read()
    datas = pdf.cms.sign(datau, dct,
        p12.get_privatekey().to_cryptography_key(),
        p12.get_certificate().to_cryptography(),
        [],
        'sha256'
    )
    fname = fname.replace('.pdf', 'abc_xyz.pdf')
    with open(fname, 'wb') as fp:
        fp.write(datau)
        fp.write(datas)

main()