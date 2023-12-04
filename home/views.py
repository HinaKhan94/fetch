from django.shortcuts import render, redirect
from django.views import View
from .forms import MessageForm
from django.contrib import messages

# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

class MessageView(View):
    """
    saves inquiry data in the Contact model
    when the form is submitted successfully.

    """
    template_name = 'home/message.html'

    def get(self, request):
        message_form = MessageForm()
        context = {'message_form': message_form}
        return render(request, self.template_name, context)

    def post(self, request):
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            messages.success(request, "Your message has been sent! "
                             "You will be contacted within 24 hours.")
            return redirect('home')
        else:
            messages.error(request, "There was an error "
                           "in your submission. Please try again.")
            # Redirects to the contact page in case of an error
            return redirect('message')
