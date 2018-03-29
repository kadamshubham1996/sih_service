from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
import os
import django; django.setup()
from user_service.db.user_models.models import BillingEntry
dir_path = os.path.dirname(os.path.realpath(__file__))

def send_pdf(bill_object):
    print bill_object.user
    username = bill_object.user.username
    month = bill_object.month
    bill_unit = bill_object.billing_units
    bill_amount = bill_object.bill_amount
    billname = str(username) + str(month) + ".pdf"
    path = os.path.join(dir_path + "/static", billname)
    c= canvas.Canvas(billname, pagesize=letter)
    c.drawImage('powerheader.jpg',2,670,600,95)
    c.drawImage('2.jpg',2,120,620,115)
    c.drawImage('header.jpg',5,700)
    c.drawInlineImage('3.jpg',5,702,105,70)
    c.setFillColor(HexColor('#ffffff'))
    c.setFontSize(size=12)
    c.setFillColor(HexColor('#000000'))
    c.drawString(15,630,"--------------------------------------------------------------------------------------------------------------------------------------------------")
    c.drawString(15,200,"--------------------------------------------------------------------------------------------------------------------------------------------------")
    #c.drawString(20, 600, "Customer_ID :")
    #c.drawString(250,600,str(bill_object.user.connection.id.customer_id))
    c.drawString(20, 550, "Name:")
    c.drawString(250,550,username)
    #c.drawString(20,500,"Address:")
    c.drawString(20, 500, "month:")
    c.drawString(20, 500, month)
    #address = (billing_object.user.connection.survey_number+billing_object.user.connection.society_name+billing_object.user.connection.village+billing_object.user.connection.taluka+billing_object.user.connection.district+billing_object.user.connection.pincode)
    #c.drawString(250,500,str(address))
    # c.drawString(20, 450, "Mobile No:")
    # c.drawString(250,450,str(billing_object.user.phone))
    c.drawString(20,400,"Billing_units:")
    c.drawString(250,400,bill_unit)
    # c.drawString(20, 350, "Month :")
    # c.drawString(250,350,str(billing_object.month))
    c.drawString(20, 300, "Billing Amount:")
    c.drawString(250, 300, bill_amount)
    # c.drawString(20, 250, "Last Date:")
    # c.drawString(250, 250, str(billing_object.last_date))
    qr_code = qr.QrCodeWidget(bill_object.id)
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(110, 110, transform=[110. / width, 0, 0, 110. / height, 0, 0])
    d.add(qr_code)
    renderPDF.draw(d, c, 490, 520)
    c.drawImage('3.jpg',2,-5,620,200)
    c.save()
if __name__ == "__main__":
    bill_object = BillingEntry.objects.first()
    send_pdf(bill_object)

