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
    """This function displays the landing page of the site.
    It renders the index.html template and returns it as a response.

    :param request: A Django HttpRequest object representing the user's request.
    :type request: HttpRequest

    :return: A Django HttpResponse object containing the rendered "index.html" template.
    :rtype: HttpResponse
    """

    return render(request, "index.html")


# === register as user ===
def register(request):
    """This function facilitates the registration of a new user based on a POST request; then authenticates them
    and redirects them to the home page. If the request is not successful, the user will be prompted to start again
    with a clean registration form.

    :param HttpRequest request: The HTTP request object.

    :return: A response containing either a registration form or a redirect to the home page.
    :rtype: HttpResponse

    :raises: None

    :example:
        To register a new user, make a POST request to this view with the necessary form data.

    :note:
        This view assumes that you have a Django `UserCreationForm` for user registration.
        It also assumes that you have configured URL routing with a 'polls:home' reverse URL.
    """

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
    """Facilitates the login of an existing user, authenticates and then redirects them to the home page.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: A rendered HTML page for user login or a redirection to the home page upon successful login.
    :rtype: HttpResponse
    """

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
    """This function is the home page displayed after login/registration
    It renders the home.html template and returns it as a response.

    :param request: A Django HttpRequest object representing the user's request.
    :type request: HttpRequest

    :return: A Django HttpResponse object containing the rendered "home.html" template.
    :rtype: HttpResponse
    """

    return render(request, "home.html")


# -------------------------
#  POLLS APP FUNCTIONALITY
# -------------------------

# === list page ===
def polls(request):
    """Displays a list of poll questions retrieved from the database to the user, in order of date published,
    and renders the 'poll.html' template

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: The rendered HTML response containing the list of poll questions.
    :rtype: HttpResponse
    """

    latest_question_list = Question.objects.order_by('date_published')
    context = {'latest_question_list': latest_question_list}
    return render(request, "poll.html", context)


# === poll detail view ===
def detail(request, question_id):
    """Displays the detail view of a specific question to the user, along with its choice options.
    Users can then vote for a particular choice.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :param question_id: The unique identifier of the question.
    :type question_id: int

    :return: The rendered detail page for the question.
    :rtype: HttpResponse
    """

    # displays the detail view of the question being asked using detail.html file in templates folder
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


# === poll vote view ===
def vote(request, question_id):
    """
    This function facilitates the voting process for a given question and redirects users to the results page.

    :param request: The HTTP request object.
    :type request: django.http.HttpRequest
    :param question_id: The ID of the question to vote on.
    :type question_id: int

    :returns: HttpResponseRedirect to the results page.
    :rtype: django.http.HttpResponseRedirect
    """

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
    """Displays the poll results of a particular question to the user.
    It takes a `request` object and a `question_id` as parameters
    and renders a template to display the results of the specified question.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :param question_id: The ID of the question to display results for.
    :type question_id: int

    :return: A rendered HTML page displaying the poll results.
    :rtype: HttpResponse
    """

    # displays the results of our question using results.html file in templates folder
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


# ------------------------------------
#  Store
# ------------------------------------

def store(request):
    """This function displays the online store to the user. The store is not functional yet.
    It renders the online_store.html template and returns it as a response.

    :param request: A Django HttpRequest object representing the user's request.
    :type request: HttpRequest

    :return: A Django HttpResponse object containing the rendered "online_store.html" template.
    :rtype: HttpResponse
    """

    return render(request, "online_store.html")

# === END === #
