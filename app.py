import requests
import bs4

from tkinter import *

def getData():
    url = "https://www.mygov.in/covid-19/"
    html_data = requests.get(url)
    clean_data = bs4.BeautifulSoup(html_data.text, "html.parser")
    span = clean_data.findAll('span',class_ = "icount")

    headings = ["Active Cases Currently","Total Cases Count","Total Discharged","Total Deaths"]
    all_details = ''

    i = 0
    for data in span:
        all_details += headings[i] + ' ' + data.get_text() + "\n\n"
        i += 1

    return all_details


def refreshData():
    new_data = getData()
    dataLabel.config(text = new_data + "Data Refreshed")

def closeWindow():
    window.destroy()
    exit()




window = Tk()

window.title("Covid-19 Tracker App")
window.geometry("900x900")
window.configure(bg = "#1d2021")

logo1 = PhotoImage(file = "icon.png")

logoLabel = Label(window, image = logo1, bg = "#1d2021")
logoLabel.pack()

dataLabel = Label(window, bg = "#1d2021",text = getData(), font = ("FiraCode Nerd Font Mono", 20, "bold"), fg = "white")
dataLabel.pack()

refreshButton = Button(window, text = "Click to Refresh", font = ("FiraCode Nerd Font Mono", 25, "bold"), command = refreshData)
refreshButton.pack()

exitButton = Button(window, text = "Click to Exit", font = ("FiraCode Nerd Font Mono", 25, "bold"),command = closeWindow)
exitButton.pack()


window.mainloop()
