from django.shortcuts import render
def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    return render(request, 'contactus.html')
def home(request):
    return render(request, 'home.html')
def movies(request):
    return render(request, 'movies.html')
def news(request):
    return render(request, 'news.html')
def shows(request):
    return render(request, 'shows.html')
def main(request):
    return render(request, 'main.html')
def recipe(request):
    ingrideants = ["maggie", "tomato"]
    data = {
        "name":"maggie", 
        "time": 2,
        "ingredient":ingrideants}
    return render(request, 'recipe.html', data)
def team(request):
    playerlist = ["Shubman Gill", "Rashid Khan", "Sai Sudarshan"]
    info = {
        "teamName":"Gujarat Titans",
        "cap":"Shubman Gill",
        "playerli":playerlist,
        "trophy":0
    }
    return render(request, "ipl.html", info)
def library(request):
    roomlist = ["Room_1", "Room_2", "Room_3"]
    lib_info = {
        "Lib_name":"Om Libary",
        "Lib_Address":"Near Siddhpur Cross, Patan",
        "Lib_mob":"1234567890",
        "Lib_Fees":100,
        "Lib_room":roomlist,
        "Lib_roomType":"AC/NonAc"
    }
    return render(request, "lib.html", lib_info)