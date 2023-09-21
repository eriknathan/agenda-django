from django.shortcuts import get_object_or_404, render

from contact.models import Contact


def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')[:10]

    print(contacts.query)

    context = {'contacts': contacts}
    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):
    single_contacts = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {'contact': single_contacts}

    return render(
        request,
        'contact/contact.html',
        context
    )
