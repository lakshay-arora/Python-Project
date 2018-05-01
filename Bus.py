from Tkinter import *
from PIL import ImageTk , Image
frame = Tk()
frame.geometry('1050x530+160+100')
frame.title('BUS INFORMATION SYSTEM')
busImage = ImageTk.PhotoImage(Image.open('/home/lakshay/Desktop/bus-sto.png'))

# Top frame color
Top = Frame(frame, width=1050, height=100, bg="#016f82")
Top.pack(side=TOP)

#FILE TO STORE INFORMATION OF BUSES
INFO = open("busInformation.txt" , "a+")

#MAIN LEFT FRAME
frame1 = Frame(frame, width=600, height=450, bg="#016f82")
frame1.pack(padx = 14,pady = 10,side=LEFT)

#MAIN RIGHT FRAME
frame2 = Frame(frame, width=420, height=450, bg="#016f89")

canvas = Canvas(frame2,bg="#016f89", width=500, height=500)
canvas.pack()
canvas.create_image(150, 100, image=busImage)
#frame3 = Label(frame,image = busImage)
#frame3.place(x=700,y=500)
#frame3.pack()
frame2.pack(padx=14,pady=10,side=RIGHT)

# MAIN LABEL
infoLabel = Label(Top, font=('Times New Roman', 50), text="BUS INFORMATION SYSTEM")
infoLabel.place(x=190,y=16)

# VARIABLES
busNO = StringVar()
busFROM = StringVar()
busTO = StringVar()
busDEPARTURE = StringVar()
busARRIVAL = StringVar()
busDISTANCE = StringVar()
busPRICE = StringVar()

#COMMAND FOR ADD BUTTON. IT ADDS INFORMATION REGARDING BUS TO THE TEXT FILE
def addBusInformation() :
    INFO = open("busInformation.txt", "a+")
    text =  str(busNO.get())
    text2 = str(busFROM.get())
    text3 = str(busTO.get())
    text4 = str(busDEPARTURE.get())
    text5 = str(busARRIVAL.get())
    text6 = str(busDISTANCE.get())
    text7 = str(busPRICE.get())

    TEXT = text + " " + text2 +" " + text3+ " "+text4+" "+text5+" "+text6+" "+text7+"\n"
    print TEXT
    INFO.write(TEXT)
    busNO.set("")
    busFROM.set("")
    busTO.set("")
    busDEPARTURE.set("")
    busARRIVAL.set("")
    busDISTANCE.set("")
    busPRICE.set("")
    INFO.close()

#COMMAND FOR DELETE BUTTON. IT DELETS THE BUS INFORMATION OF THE GIVEN BUS NO.
def deleteBusInformation() :
    busno = busNO.get()
    INFO = open("busInformation.txt" ,"r")
    lines = INFO.readlines()
    INFO.close()
    INFO = open("busInformation.txt","w")

    for i in lines :
        x = i.split()
        if ( x[0] != busno) :
            INFO.write(i)


    busNO.set("")
    INFO.close()

# COMMAND FOR FIND BUTTON. IT FINDS AND DISPLAYS THE INFORMATION OF THE GIVEN BUS NO.
def findBusInformation() :
    busno = busNO.get()
    INFO = open("busInformation.txt","r")
    lines = INFO.readlines()
    INFO.close()

    for i in lines :
        x = i.split()
        if (x[0] == busno) :
            busNO.set(busno)
            busFROM.set(x[1])
            busTO.set(x[2])
            busDEPARTURE.set(x[3]+" "+x[4])
            busARRIVAL.set(x[5]+" "+x[6])
            busDISTANCE.set(x[7])
            busPRICE.set(x[8])

# COMMAND FOR CLEAR BUTTON. IT CLEARS ALL THE TEXT FIELDS IN THE GUI.
def clearBusInfromation() :
    busNO.set("")
    busFROM.set("")
    busTO.set("")
    busDEPARTURE.set("")
    busARRIVAL.set("")
    busDISTANCE.set("")
    busPRICE.set("")

#COMMAND FOR THE FIRST BUTTON. IT DISPLAYS THE FIRST BUS INFORMATION IN THE FILE.
def firstBusInformation() :
    INFO = open("busInformation.txt", "r")
    lines = INFO.readlines()
    INFO.close()
    x = lines[0].split()
    busNO.set(x[0])
    busFROM.set(x[1])
    busTO.set(x[2])
    busDEPARTURE.set(x[3] + " " + x[4])
    busARRIVAL.set(x[5] + " " + x[6])
    busDISTANCE.set(x[7])
    busPRICE.set(x[8])

#COMMAND FOR THE LAST BUTTON. IT DISPLAYS THE LAST BUS INFORMATION IN THE FILE.
def lastBusInformation() :
    INFO = open("busInformation.txt", "r")
    lines = INFO.readlines()
    INFO.close()

    x = lines[len(lines)-1].split()
    busNO.set(x[0])
    busFROM.set(x[1])
    busTO.set(x[2])
    busDEPARTURE.set(x[3] + " " + x[4])
    busARRIVAL.set(x[5] + " " + x[6])
    busDISTANCE.set(x[7])
    busPRICE.set(x[8])

#COMMAND FOR THE PREVIOUS BUTTON. IT DISPLAYS THE PREVIOUS BUS INFORMATION OF THE PRESENT BUS NO.
def previousBusInformation() :
    busno = busNO.get()
    INFO = open("busInformation.txt", "r")
    lines = INFO.readlines()
    INFO.close()

    for i in lines:
        x = i.split()
        if (x[0] == busno):
            busNO.set(previous[0])
            busFROM.set(previous[1])
            busTO.set(previous[2])
            busDEPARTURE.set(previous[3] + " " + previous[4])
            busARRIVAL.set(previous[5] + " " + previous[6])
            busDISTANCE.set(previous[7])
            busPRICE.set(previous[8])
        previous = x
#COMMAND FOR THE NEXT BUTTON. IT DISPLAYS THE NEXT BUS INFORMATION OF THE PRESENT BUS NO.
def nextBusInformation() :
    busno = busNO.get()
    INFO = open("busInformation.txt", "r")
    lines = INFO.readlines()
    INFO.close()

    active = False
    for i in lines:
        x = i.split()
        if (active == True) :
            active = False
            busNO.set(x[0])
            busFROM.set(x[1])
            busTO.set(x[2])
            busDEPARTURE.set(x[3] + " " + x[4])
            busARRIVAL.set(x[5] + " " + x[6])
            busDISTANCE.set(x[7])
            busPRICE.set(x[8])

        if (x[0] == busno):
            active = True

#frame 1 GUI TODO : TO ADD NEW BUS TO THE SYSTEM
busNoLabel = Label(frame1, font=('aerial',20,'bold'),text='BUS NO : ',bg = "#016f82")
busNoLabel.place(x=10,y=30)
busNoText = Entry(frame1, font=('aerial',20,'bold'),textvariable=busNO,width=29,justify='right')
busNoText.place(x=165,y=30)

busFromLabel = Label(frame1, font=('aerial',20,'bold'),text='FROM : ',bg="#016f82")
busFromLabel.place(x=10,y=80)
busFromText = Entry(frame1, font=('aerial',20,'bold'),textvariable=busFROM,width=10,justify='right')
busFromText.place(x=165,y=80)

busToLabel = Label(frame1, font=('aerial',20, 'bold'),text='TO : ',bg = "#016f82")
busToLabel.place(x=325,y=80)
busToText = Entry(frame1, font=('aerial',20,'bold'),textvariable=busTO,width= 9,justify='right')
busToText.place(x=444,y=80)

busDepartureLabel = Label(frame1, font=('aerial',20,'bold'),text='DEPARTURE',bg = "#016f82")
busDepartureLabel.place(x=10,y=130)
busDepartureText = Entry(frame1, font=('aerial',20,'bold'),textvariable=busDEPARTURE,width=10,justify='right')
busDepartureText.place(x=165,y=130)

busArrivalLabel = Label(frame1,font=('aerial',20,'bold'),text='ARRIVAL ',bg = "#016f82")
busArrivalLabel.place(x=325,y=130)
busArrivalText = Entry(frame1, font=('aerial',20,'bold'),textvariable=busARRIVAL,width=9,justify='right')
busArrivalText.place(x=444,y=130)

busDurationLabel = Label(frame1, font=('aerial',20, 'bold'),text='DISTANCE : ',bg = "#016f82")
busDurationLabel.place(x=10,y=180)
busDurationText = Entry(frame1, font=('aerial',20,'bold'),textvariable=busDISTANCE,width = 29,justify='right')
busDurationText.place(x=165,y=180)

busPriceLabel = Label(frame1, font=('aerial',20,'bold'),text='PRICE : ',bg = "#016f82")
busPriceLabel.place(x=10,y=230)
busPriceText = Entry(frame1, font=('aerial',20,'bold'),textvariable=busPRICE,width=29,justify='right')
busPriceText.place(x=165,y=230)

AddBusButton = Button(frame1,fg='black',font=('aerial',20,'bold'),height=1,width=11,text='ADD BUS',command = addBusInformation,bg="#016FA2")
AddBusButton.place(x=165,y=280)

DeleteButton = Button(frame1,fg='black',font=('aerial',20,'bold'),height=1,width=11,text='DELETE',command = deleteBusInformation ,bg = "#016FA2")
DeleteButton.place(x=395,y=280)

FindButton = Button(frame1,fg='black',font=('aerial',20,'bold'),height=1,width=11,text='FIND BUS',command = findBusInformation ,bg = "#016FA2")
FindButton.place(x=165,y=335)

ClearButton = Button(frame1,fg='black',font=('aerial',20,'bold'),height=1,width=11,text='CLEAR',command = clearBusInfromation ,bg = "#016FA2")
ClearButton.place(x=395,y=335)

FirstButton = Button(frame2,fg='black',font=('aerial',20,'bold'),height=1,width=10,text='FIRST',command = firstBusInformation,bg="#016FA2")
FirstButton.place(x=10,y=284)

LastButton = Button(frame2,fg='black',font=('aerial',20,'bold'),height=1,width=10,text='LAST',command = lastBusInformation ,bg = "#016FA2")
LastButton.place(x=200,y=284)

PreviousButton = Button(frame2,fg='black',font=('aerial',20,'bold'),height=1,width=10,text='PREVIOUS',command = previousBusInformation ,bg = "#016FA2")
PreviousButton.place(x=10,y=339)

NextButton = Button(frame2,fg='black',font=('aerial',20,'bold'),height=1,width=10,text='NEXT',command = nextBusInformation ,bg = "#016FA2")
NextButton.place(x=200,y=339)

frame.mainloop()