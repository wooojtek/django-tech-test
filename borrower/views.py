from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from borrower.forms import BorrowerForm


@login_required
def borrower(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        user = request.user
        profile = user.profile
        form = BorrowerForm(instance=profile)

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('borrower/profile.html', args)
