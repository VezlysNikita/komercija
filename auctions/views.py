from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Watchlist, Watchlists



def create(request):
    if request.method == "POST":

        listing = Listing()

        listing.title = request.POST["title"]
        listing.description = request.POST["description"]
        listing.price = request.POST["startbid"]
        listing.category = request.POST["category"]
        listing.img_link = request.POST["image"]
        listing.seller = User.objects.get(pk=request.user.id)


        listing.save()

        products = Listing.objects.all()

        return HttpResponseRedirect(reverse(index))
                
    else:
        return render(request, "auctions/create.html")


def view_page(request, listing_id):

    if request.method == "POST":

        
        listid = Listings.objects.get(pk=request.Listings.listing_id)

        user = User.objects.get(pk=request.user.id)


 

        return HttpResponseRedirect(reverse("auctions/page.html", args=(listings.listing_id)))


    else: 

        listings = Listing.objects.filter(pk=listing_id)

        return render(request, "auctions/page.html", {
        "listings": listings
    })


def index(request):

    listings = Listing.objects.filter(closed=False)


    return render(request, "auctions/index.html", {
        "listings": listings
    })


def addwatchlist(request, listing_id):

    print(listing_id)

    listid = Listing.objects.get(listing_id=listing_id)

    if request.method == "POST":


        user = User.objects.get(pk=request.user.id)

        Watchlist = Watchlists()


        if not Watchlists.objects.filter(listing_id=listid, user_id=user):


            Watchlist.user_id = user
            Watchlist.listing_id = listid

            Watchlist.save()

        else:

            Watchlists.objects.filter(listing_id=listid, user_id=user).delete()


        return HttpResponseRedirect(reverse(index))
                
    else: 

        listings = Listing.objects.filter(pk=listid)

        return render(request, "auctions/page.html", {
        "listings": listings
    })


def watchlist(request):

    items = Watchlists.objects.filter(user_id=request.user.id)
    listings = []
    for item in items:
        listings.append(Listing.objects.get(pk=item.listing_id))
        print(item)
        

    empty = False
    if len(listings) == 0:
        empty = True
        
    return render(request, "auctions/watchlist.html", {
        "empty": empty,
        "listings": listings
    })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
