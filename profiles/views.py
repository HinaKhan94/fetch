from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import UserProfile, Wishlist
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Review, Product
from products.utils import products_pagination
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def my_reviews(request):
    user_reviews_approved = (
        Review.objects
        .filter(user=request.user, is_approved=True)
    )
    user_reviews_pending = (
        Review.objects
        .filter(user=request.user, is_approved=False)
    )

    template = 'profiles/my_reviews.html'
    context = {
        'user_reviews_approved': user_reviews_approved,
        'user_reviews_pending': user_reviews_pending,
    }
    return render(request, template, context)


@login_required
def wishlist_view(request):
    """ renders wishlist page """
    user_wishlist = Wishlist.objects.filter(user=request.user.userprofile)
    paginated_wishlist = products_pagination(request, user_wishlist, 4)
    template = 'profiles/wishlist.html'
    context = {'wishlist_items': paginated_wishlist}
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """view to add an item to wishlist """
    product = Product.objects.get(pk=product_id)
    # Check if the item is already in the wishlist
    if Wishlist.objects.filter(
        user=request.user.userprofile,
        product=product
         ).exists():
        messages.warning(
            request, f"{product.name} is already in your wishlist.")
    else:
        # Add the item to the wishlist
        Wishlist.objects.create(user=request.user.userprofile, product=product)
        messages.success(request, f"{product.name} added to your wishlist.")

    return redirect('products')


@login_required
def remove_from_wishlist(request, wishlist_item_id):
    """ to remove an item from wishlist """
    wishlist_item = get_object_or_404(Wishlist, pk=wishlist_item_id)

    # Remove the item from the user's wishlist
    wishlist_item.delete()

    # Redirect to the wishlist or wherever you want
    return redirect('wishlist')
