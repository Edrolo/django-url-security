from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    render,
)
from polls.models import Question


def basic_public_view(request):
    return HttpResponse('<html><body>Public</body></html')


@login_required
def basic_private_view_that_redirects(request):
    return HttpResponse('<html><body>Private</body></html')


@permission_required('polls.add_question', raise_exception=True)
def basic_private_view_that_raises_403(request):
    return HttpResponse('<html><body>Private</body></html')


def basic_public_view_requiring_fixture(request, *, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/detail.html', {'question': question})
