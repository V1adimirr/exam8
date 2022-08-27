from django.views.generic import  DetailView

from webapp.models import Review


class IndexReview(DetailView):
    model = Review
    template_name = 'reviews/review_view.html'
    context_object_name = 'reviews'

