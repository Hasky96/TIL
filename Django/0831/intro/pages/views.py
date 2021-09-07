from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    lotto_list = list(range(1, 46))
    random.shuffle(lotto_list)
    context = {
        "lotto" : lotto_list[:6]
    }
    return render(request, 'lotto.html', context)
 