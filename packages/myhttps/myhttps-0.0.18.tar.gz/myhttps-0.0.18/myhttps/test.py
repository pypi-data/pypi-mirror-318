# coding=utf-8
import os, sys, codecs
from http.server import HTTPServer, SimpleHTTPRequestHandler
from outdated import check_outdated
from socketserver import ThreadingMixIn
import ssl
from OpenSSL import crypto
import site
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib3.exceptions import InsecureRequestWarning


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class HTTPS:

    def __init__(self,host,port,keyfile,certfile,share_dir=None):
        print('keyfile =',keyfile)
        print('certfile =',certfile)

        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if share_dir:
            os.chdir(share_dir)
        httpd = ThreadingSimpleServer((host, port), SimpleHTTPRequestHandler)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        print("server started at https://%s:%s" % (host, port))
        httpd.serve_forever()
        pass

class HTTP:

    def __init__(self,host,port,share_dir=None):
        if share_dir:
            os.chdir(share_dir)
        httpd = ThreadingSimpleServer((host, port), SimpleHTTPRequestHandler)
        print("server started at http://%s:%s" % (host, port))
        httpd.serve_forever()
        pass

def main():

    host = '0.0.0.0'
    port = 11443
    keyfile = 'cert/key.pem'
    certfile = 'cert/cert.pem'
    share_dir = '/Users/liyang/Desktop'
    # HTTPS(host,port,keyfile,certfile,share_dir)
    HTTP(host,port,share_dir)

if __name__ == '__main__':
    main()
