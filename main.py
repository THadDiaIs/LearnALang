from tkinter import *
import pandas as pd
from random import choice

BG='#B1DDC6'
PRMRY='#360404'
SCNDRY='#DCA3C6'
cardTurn = None
data = []


#--------Turn Card and updt translat...
def FrConf():
	card.itemconfigure(lang,text='French',fill=SCNDRY)
	card.itemconfig(dinamiCard,image=bgFrontCard)
	card.itemconfig(word,fill=SCNDRY)
	
def EnConf():
	card.itemconfigure(lang,text='English',fill=PRMRY)
	card.itemconfig(dinamiCard,image=bgBackCard)
	card.itemconfig(word,fill=PRMRY,text=curWord['En'])


#--------Reading data from csv and 1rst displ...
try:
	data = pd.read_csv('./ToLearn.CSV').to_dict(orient='records')
except FileNotFoundError:
	data = pd.read_csv('./FR_EN.CSV').to_dict(orient='records')
	
curWord = ''

def updateCard():
	global curWord,cardTurn
	curWord=choice(data)
	FrConf()
	card.itemconfigure(word,text=curWord['Fr'].title())
	if cardTurn != None:root.after_cancel(cardTurn)
	cardTurn=root.after(3000,EnConf)


#--------rec9gnis8ng words to lear and learned
def learned():
	updateCard()
	data.remove(curWord)
	saveProgress()

def unlearned():
	updateCard()

def saveProgress():
	pd.DataFrame(data).to_csv('./ToLearn.CSV',index=False)


#--------GUI
root = Tk()
root.title('Flash Learn')
root.config(padx=50,pady=50,bg=BG)

card = Canvas(width=800,height=526,bg=BG,highlightthickness=0)
bgFrontCard = PhotoImage(file='./FrontCard.png')
bgBackCard= PhotoImage(file='./BackCard.png')
dinamiCard = card.create_image(400,263,image=bgFrontCard)
word=card.create_text(400,250,text='Word',font=('Ariel',37,'bold'),fill=SCNDRY)
lang=card.create_text(400,380,text='Title',font=('Ariel',19,'italic'),fill=SCNDRY)
card.grid(column=0,row=0,columnspan=2)

AImage=PhotoImage(file='./check.png')
CImage=PhotoImage(file='./negative.png')

CBtn = Button(image=CImage,highlightthickness=0,command=unlearned,bg=BG)
CBtn.grid(row=1,column=0)

ABtn=Button(image=AImage,highlightthickness=0,command=learned,bg=BG)
ABtn.grid(row=1,column=1)

updateCard()

root.mainloop()