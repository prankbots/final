# -*- coding: utf-8 -*-
class Callback(object):
    def __init__(self, callback):
        self.callback = callback
    def PinVerified(self, pin):
        self.callback("KODE PIN [ '" + pin + "' ]")
    def QrUrl(self, url, showQr=True):
        if showQr:
            notice='ATAU SCAN KODE QR '
        else:
            notice=''
        self.callback('BUKA LINK ' + notice + 'WAKTU 2 MENIT\n' + url)
        if showQr:
            try:
                import pyqrcode
                url = pyqrcode.create(url)
                self.callback(url.terminal('green', 'white', 1))
            except:
                pass
    def default(self, str):
        self.callback(str)
