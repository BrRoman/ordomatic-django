from django.shortcuts import render


def index(request):
    """ 'Index' page of docs. """
    return render(
        request,
        'docs/index.html',
        {
            'pages': [
                {
                    'url': 'overview',
                    'title': 'Overview',
                },
                {
                    'url': 'what_is_an_ordo',
                    'title': 'What is an ordo?',
                },
                {
                    'url': 'create_an_account',
                    'title': 'Create an account',
                },
                {
                    'url': 'create_a_calendar',
                    'title': 'Create a calendar',
                },
                {
                    'url': 'populate_your_calendar',
                    'title': 'Populate your calendar',
                },
                {
                    'url': 'create_an_ordo',
                    'title': 'Create an ordo!',
                },
                {
                    'url': 'for_developers',
                    'title': 'For developers',
                },
            ],
        }
    )


def overview(request):
    """ 'Overview' page of docs. """
    return render(request, 'docs/overview.html')


def what_is_an_ordo(request):
    """ 'What is an ordo?' page of docs. """
    return render(request, 'docs/what_is_an_ordo.html')


def create_an_account(request):
    """ 'Create an account' page of docs. """
    return render(request, 'docs/create_an_account.html')


def create_a_calendar(request):
    """ 'Create a calendar' page of docs. """
    return render(request, 'docs/create_a_calendar.html')


def populate_your_calendar(request):
    """ 'Populate your calendar' page of docs. """
    return render(request, 'docs/populate_your_calendar.html')


def create_an_ordo(request):
    """ 'Create an ordo' page of docs. """
    return render(request, 'docs/create_an_ordo.html')


def for_developers(request):
    """ 'For developers' page of docs. """
    return render(request, 'docs/for_developers.html')
