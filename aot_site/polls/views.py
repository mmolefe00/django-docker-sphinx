# === IMPORTS === #

# imports for registering, logging in and logging out
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

# imports for poll views
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

# === CREATE VIEWS HERE === #

# ---------------------------------
# INDEX to LOGIN / SIGN UP to HOME
# ---------------------------------

# === index / landing page ===
def index(request):
    return render(request, "index.html")


# === register as user ===
def register(request):

    if request.method != 'POST':
        # return blank form if user enters incorrectly
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        # if user registers correctly, save their data
        if form.is_valid():
            new_user = form.save()

            # authenticate the user
            authenticate_user = authenticate(
                username=new_user.username, password=form.cleaned_data['password1']
            )

            # once authenticated, login user
            login(request, authenticate_user)

            # redirect the logged-in user to home page
            return HttpResponseRedirect(reverse('polls:home'))

    # render the html file
    return render(request, 'registration/register.html', {'form': form})


# === login as user ===
def user_login(request):
    if request.method != 'POST':
        form = AuthenticationForm()

    else:
        form = AuthenticationForm(request, request.POST)

        # if authentication is valid, get user from database and log them in
        if form.is_valid():
            login(request, form.get_user())

            # redirect the logged-in user to home page
            return HttpResponseRedirect(reverse('polls:home'))

    # render the login.html form
    return render(request, 'registration/login.html')


# === home page ===
def home(request):
    return render(request, "home.html")


# -------------------------
#  POLLS APP FUNCTIONALITY
# -------------------------

# === list page ===
def polls(request):
    # home view (landing page or list of poll questions) in order of date published
    # using poll.html in templates folder
    latest_question_list = Question.objects.order_by('date_published')
    context = {'latest_question_list': latest_question_list}
    return render(request, "poll.html", context)


# === poll detail view ===
def detail(request, question_id):
    # displays the detail view of the question being asked using detail.html file in templates folder
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


# === poll vote view ===
def vote(request, question_id):
    # displays page for user to vote on question with an array of choice options
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form if no choice is selected
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."})

    else:
        # if correct choice is selected, increase vote total by one
        selected_choice.votes += 1
        selected_choice.save()

        # return result data as http response to prevent data from being posted twice if user hits the back button
        return HttpResponseRedirect(
            reverse('polls:result', args=(question_id,))
        )


# === poll results view ===
def result(request, question_id):
    # displays the results of our question using results.html file in templates folder
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


# ------------------------------------
#  Store
# ------------------------------------

def store(request):
    return render(request, "online_store.html")

# === END === #
