from datetime import datetime

from django.shortcuts import render


def index(request):
    date = datetime.today()

    return render(
        request, "DocBlog/index.html", context={"prenom": "Jean-Yves", "date": date}
    )
