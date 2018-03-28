from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
import django; django.setup()
from user_service.db.user_models.models import BillingEntry
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def send_pdf1(bill_object):
    username=bill_object.user.username
    month=bill_object.month
    bill_unit=bill_object.billing_units
    bill_amount=bill_object.bill_amount
    billname = str(username)+str(month)+".pdf"
    path = os.path.join(dir_path+"/static", billname)
    c = canvas.Canvas(path, pagesize=letter)

    #c= canvas.Canvas("Qrcodes1.pdf", pagesize=letter)

    c.setFontSize(size=20)
    c.drawString(20,600,"Username:")
    c.drawString(250,600,username)
    c.drawString(20,560,"Month:")
    c.drawString(250,560,month)
    c.drawString(20,520,"Billing_units:")
    c.drawString(250,520,str(bill_unit))

    c.drawString(20, 480, "Billing Amount:")
    c.drawString(250, 480, str(bill_amount))

    qr_code = qr.QrCodeWidget(str(bill_object.id))
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(60, 60, transform=[60. / width, 0, 0, 60. / height, 0, 0])
    d.add(qr_code)
    renderPDF.draw(d, c, 500, 560)
    c.save()
    return billname


if __name__ == "__main__":
    bill_object = BillingEntry.objects.first()
    send_pdf(bill_object)
