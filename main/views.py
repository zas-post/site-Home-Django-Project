from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import lorem


def index(request):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О НАС",
        "text_on_page": "«Поговорим не про Vim», олдам, сеньорам и тру-си-разработчикам на проверку: пользуетесь ли вы такими сочетаниями VS Code? Если же вы только начинаете программировать, влетаете в айти на реактивном самолете курсов по Питону, или просто не знаете ничего про хоткеи VS Code, возможно вам точно пригодится парочка сочетаний :)",
    }
    return render(request, "main/about.html", context)
