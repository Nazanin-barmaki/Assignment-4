from cgitb import text
import qrcode
text = input('This is a practice for python class type anything related to the class')
QR = qrcode.make(text)
QR.save('qrcode_result.jpg')
