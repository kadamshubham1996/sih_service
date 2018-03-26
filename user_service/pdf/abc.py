from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF


# ----------------------------------------------------------------------
def createBarCodes():
    """
    Create barcode examples and embed in a PDF
    """
    c = canvas.Canvas("Qrcodes.pdf", pagesize=letter)


    # draw a QR code
    qr_code = qr.QrCodeWidget('Bill Amount')
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(45, 45, transform=[45. / width, 0, 0, 45. / height, 0, 0])
    d.add(qr_code)
    renderPDF.draw(d, c, 15, 405)

    c.save()


if __name__ == "__main__":
    createBarCodes()