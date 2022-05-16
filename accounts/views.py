from django.shortcuts import render


def account_sign_up(request):
    page = 'Sign Up'
    context = {
        'page': page,
    }
    return render(request, 'accounts/sign-up.html', context)


def account_sign_in(request):
    page = 'Sign In'
    context = {
        'page': page,
    }
    return render(request, 'accounts/sign-in.html', context)


def account_info(request, pk):
    page = ''
    context = {
        'page': page,
    }
    context = {}
    return render(request, 'accounts/account-info.html', context)
