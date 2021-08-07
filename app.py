import requests
import bs4

from tkinter import *

def getWorldData():
    url = "https://www.worldometers.info/coronavirus/"

    html_data = requests.get(url)
    clean_data = bs4.BeautifulSoup(html_data.text, "html.parser")

    info_div = clean_data.find('div', attrs = { 'class': 'content-inner' })

    req_data = ''
    for info in info_div.find_all('div', attrs = { 'id': 'maincounter-wrap' }):
        try:
            req_data += info.h1.get_text() + ' ' + info.span.get_text() + "\n"
        except AttributeError:
            pass

    return req_data


def getCountryData():
    name = country_input.get()

    url = f"https://www.worldometers.info/coronavirus/country/{name}/"

    html_data = requests.get(url)
    clean_data = bs4.BeautifulSoup(html_data.text, "html.parser")

    info_div = clean_data.find('div', attrs = { 'class': 'content-inner' })

    req_data = ''
    for info in info_div.find_all('div', attrs = { 'id': 'maincounter-wrap' }):
        try:
            req_data += info.h1.get_text() + ' ' + info.span.get_text() + "\n"
        except AttributeError:
            pass

    headerLabel['text'] = f"Showing Stats for {name.capitalize()}"
    dataLabel['text'] = req_data

def reloadWindow():
    headerLabel['text'] = "Showing World Wide Stats"
    country_input.set('')
    dataLabel['text'] = getWorldData()




# GUI
window = Tk()

window.title("Covid-19 Live Tracker App")
window.configure(bg = "#2E3440")

title = Label(window, text = "Welcome to Covid-19 Tracker App", font = ("FiraCode Nerd Font Mono", 36, "bold"), bg = "#2E3440", fg = "#D8DEE9")
title.pack()

logo1 = PhotoImage(file = "icon1.png")
logoLabel = Label(window, image = logo1, bg = "#2E3440")
logoLabel.pack()

emptyLine = Label(window, text = "\n", bg = "#2E3440")
emptyLine.pack()

searchButton = Button(window, text = " Search by Country ", font = ("FiraCode Nerd Font Mono", 18, "bold"), bg = "#2E7D32", fg = "#D8DEE9", command = getCountryData)
searchButton.pack()

country_input = StringVar()
country_entry = Entry(window, width = 46, textvariable = country_input, font = 18)
country_entry.pack()

emptyLine = Label(window, text = "\n", bg = "#2E3440", font = 18)
emptyLine.pack()

refreshButton = Button(window, text = "  Show World Data  ", font = ("FiraCode Nerd Font Mono", 18, "bold"), background = "#1565C0", fg = "#D8DEE9", command = reloadWindow)
refreshButton.pack()

emptyLine = Label(window, text = "\n\n\n", bg = "#2E3440")
emptyLine.pack()

headerLabel = Label(window, text = "World Wide Stats", font = ("FiraCode Nerd Font Mono", 28, "bold"), fg = "#D8DEE9", bg = "#2E3440")
headerLabel.pack()

emptyLine = Label(window, text = "\n", bg = "#2E3440")
emptyLine.pack()

dataLabel = Label(window, text = getWorldData(), font = ("FiraCode Nerd Font Mono", 20, "bold"), bg = "#D8DEE9", fg = "#2E3440")
dataLabel.pack()

emptyLine = Label(window, text = "\n", bg = "#2E3440")
emptyLine.pack()

window.mainloop()
