from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import HttpResponse
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review
from django.contrib.auth.models import User
from .forms import ProductForm, ReviewForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details
    with reviews for the product """

    product = get_object_or_404(Product, pk=product_id)

    # Gets product reviews from DB
    reviews = product.reviews.filter(is_approved=True).order_by('-rating', '-created_on')

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)

def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required()
def add_review(request, product_id):
    """
    Renders form to add review.
    Logged in Users Only (redirects to log in).
    Adds new review to database.
    """

    # Sets product based on product_id
    product = get_object_or_404(Product, pk=product_id)

    # Sets author based on current user
    author = User.objects.get(username=request.user)

    # Handles Form Submission
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = author
            review.save()

            # Updates product rating on product object
            if product.reviews.filter(is_approved=True).count() > 0:
                product.rating = round(
                    product.reviews.filter(is_approved=True).aggregate(
                        Avg('rating'))['rating__avg'])
            else:
                product.rating = 0
            product.save()

            request.session['show_bag_summary'] = False
            messages.success(
                request,
                "Your review has been created. " +
                "It will appear on the site once it has been approved. " +
                "You can see your review on your profile page until then. " +
                "We value your feedback and only " +
                "reject reviews with inappropriate content."
            )

            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Form invalid, please try again.")

    # Handles View Rendering
    else:
        form = ReviewForm()

    # Sets page template
    template = 'products/reviews/add_review.html'

    # Sets current product & form content
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edits a product in db """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required()
def edit_review(request, review_id):
    """
    View to edit user reviews.
    only logged in Users can edit.
    also updates the review in database.
    """

    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.filter(reviews=review)[0]

    # Checks if user is the author
    # redirects to product detail if not
    if request.user != review.user:
        messages.error(request, 'You can only edit your own reviews.')
        return redirect(reverse('product_detail', args=[product.id]))

    # Handles Form Submission
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)

        if form.is_valid():
            review = form.save()
            review.is_approved = False
            review.save()

            # Updates product rating on product object
            if product.reviews.filter(is_approved=True).count() > 0:
                product.rating = round(
                    product.reviews.filter(
                        is_approved=True).aggregate(
                            Avg('rating'))['rating__avg'])
            else:
                product.rating = 0
            product.save()

            request.session['show_bag_summary'] = False
            messages.success(
                request,
                "Your review has been updated. " +
                "It will appear on the site once it has been approved. " +
                "We value your feedback and only! "
            )
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Form invalid, please try again.")

    # Handles View Rendering
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing... "{review.content}"')

    # Sets page template
    template = 'products/reviews/edit_review.html'

    # Sets current product & form content
    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Deletes a review """

    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.filter(reviews=review)[0]

    # Gets the previous page URL for redirect
    next = request.GET.get('next', '')

    # Checks user is author of review or superuser
    # redirects to product detail if not
    if not request.user.is_superuser:
        if request.user != review.user:
            messages.error(request, 'You can only delete your own reviews.')
            return redirect(reverse('product_detail', args=[product.id]))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()

    # Updates product rating on product object
    if product.reviews.filter(is_approved=True).count() > 0:
        product.rating = round(
            product.reviews.filter(
                is_approved=True).aggregate(Avg('rating'))['rating__avg'])
    else:
        product.rating = 0
    product.save()

    request.session['show_bag_summary'] = False
    messages.success(request, 'Review successfully deleted!')
    return redirect(next)



