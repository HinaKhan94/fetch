from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

class ContactView(View):
    """
    saves contact form data in the Contact model
    when the form is submitted successfully.

    """
    template_name = 'home/contact.html'

    def get(self, request):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, self.template_name, context)

    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Your message has been sent! "
                             "You will be contacted within 24 hours.")
            return redirect('home')
        else:
            messages.error(request, "There was an error "
                           "in your submission. Please try again.")
            # Redirects to the contact page in case of an error
            return redirect('contact')
