from django.shortcuts import render, reverse
import random
from random import choice
import re
from re import search
import markdown2
from markdown2 import Markdown
from django.http import HttpResponseRedirect
from . import util


def index(request):



    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),

    })

def wiki(request, title):
    mdValue = util.get_entry(title)

    if mdValue:

        context = {
        "content" : markdown2.markdown(mdValue),
        "title": title,
        #"entry": util.get_entry(body),


        }

        return render(request, "encyclopedia/wiki.html", #{
            #"entries": util.get_entry(title)

        #}, '
        context
        )
    else:
        return render(request, "encyclopedia/wrong.html")



def Create(request):
    content = request.POST.get("content")
    title = request.POST.get("title")




    y= request.POST.get("title","content")


    if request.method == "POST":
        mdValue = util.list_entries()


        if y in mdValue:

            return render(request, "encyclopedia/already.html")

        else:
            i = util.save_entry(title, content)



            return render(request,  "encyclopedia/index.html", {
                "entries": util.list_entries(),

            })
    else:
        return render(request, "encyclopedia/new.html")



def search(request):

    search_box = request.GET.get('si')
    #search_box = request.GET['si']
    x = util.list_entries()
    #context ={
    search_result = []
    #"search_result":search_result

    #}

    print(search_result)
    #if util.get_entry(title) is not None:





    if request.method == 'GET':

        for entry in x:

            if search_box.lower() in entry.lower():

                search_result.append(entry)

            #if search_box in x:





                print(search_result)



                print(search_result)
                if len(search_result) == 0:
                    return render(request,"encyclopedia/wrong.html")
                else:
                    return render(request,"encyclopedia/search.html", {
                    "search_result":search_result

                    })

        else:
            return render(request,"encyclopedia/wrong.html")










def EditPage(request, title):
    content = request.POST.get("content")
    #title = request.POST.get("title")
    mdValue = util.get_entry(title)
    y= request.POST.get("title","content")
    context = {
    "title" : title,
    "content": util.get_entry(title)
    }


    if request.method == "POST":

        if y in mdValue:
            i = util.save_entry(title, content)
            return render(request,  "encyclopedia/index.html", {
                "entries": util.list_entries(),

            })
        else:
            return render(request,  "encyclopedia/wrong.html")
    else:
        return render(request,  "encyclopedia/edit.html", context)


def random_page(request):
    x = util.list_entries()


    selected_page = random.choice(x)
    mdValue = util.get_entry(selected_page)
    context = {
    "title": selected_page,
    "content" : markdown2.markdown(mdValue),
    }
    return render(request,'encyclopedia/wiki.html', context)
