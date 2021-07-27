from contact.models import Contact

def contact_us(reqest):
    contact = Contact.objects.all()
    return {'contact':contact}