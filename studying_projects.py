# GUL programe for organize the time for study.
# thanks !!
# by:Benkaida Salah

from tkinter import * # import the module 
from tkinter import messagebox 
print('software is runing......')# first program 
firstw=Tk()
firstw.title("IT SOURCECODE")
firstw.geometry("800x700+0+0")
firstw.resizable(False,False)
label_bg,button_color = "#FDAC53","#FDAC53"
firstw.configure(bg='#92A8D1')

                                            # labels-part
ly=Label(firstw,bd=10,text="stdying managment system",font=("times new roman",35),bg=label_bg,fg="white")
ly.place(x=250,y=4)
ly2=Label(firstw,bd=5,text="Sunday",font=("times new roman",35),bg=label_bg,fg="white")
ly2.place(x=25,y=150)
ly3=Label(firstw,bd=5,text="Monday",font=("times new roman",35),bg=label_bg,fg="white")
ly3.place(x=25,y=230)
ly4=Label(firstw,bd=5,text="Tuesday",font=("times new roman",35),bg=label_bg,fg="white")
ly4.place(x=25,y=300
          )
ly5=Label(firstw,bd=5,text="Wednesday",font=("times new roman",35),bg=label_bg,fg="white")
ly5.place(x=25,y=370)
ly5=Label(firstw,bd=5,text="Thursday",font=("times new roman",35),bg=label_bg,fg="white")
ly5.place(x=25,y=450)
ly6=Label(firstw,bd=5,text="Friday",font=("times new roman",35),bg=label_bg,fg="white")
ly6.place(x=25,y=530)
ly7=Label(firstw,bd=5,text="Saturday",font=("times new roman",35),bg=label_bg,fg="white").place(x=25,y=600)


# var (controle )
En1_value = StringVar()
En2_value = StringVar()
En3_value = StringVar()
En4_value = StringVar()
En5_value = StringVar()
En6_value = StringVar()
En7_value = StringVar()
Bu1_data = StringVar()
Bu2_data = StringVar()
Bu8_data = StringVar()
Bu9_data= StringVar()
Bu3_data= StringVar()

# programming-part

def Exit():# function for exit from the program
    return firstw.destroy()
def do():
    with open("Stdying-System-Data","w") as F:
        F.write("Welcome To Studying System\n")
        F.write("Sunday -> {}\nStyday -> {}\nSunday ->{}\n".format(en1_data.get(),Bu1.get(),Bu7.get()))
        messagebox.showinfo("Secsuss","Done !!")
        




img=PhotoImage(file='y.png')# icon image
u=Label(firstw,image=img)
u.place(x=20,y=5)

                    #entry's for data
en1_data = Entry(firstw,bd=5,textvariable=En1_value)
en2_data = Entry(firstw,bd=5,textvariable=En2_value)
en3_data = Entry(firstw,bd=5
                 ,textvariable=En3_value)
en4_data = Entry(firstw,bd=5,textvariable=En4_value)
en5_data = Entry(firstw,bd=5,textvariable=En5_value)
en6_data = Entry(firstw,bd=5,textvariable=En6_value)
en7_data = Entry(firstw,bd=5,textvariable=En7_value)
Bu1=Entry(firstw,bd=20,textvariable=Bu1_data)
Bu2=Entry(firstw,bd=5,textvariable=Bu2_data)
Bu3=Entry(firstw,bd=5)
Bu3.place(x=500,y=320,width=100)
Bu4 = Entry(firstw,bd=5)
Bu5 = Entry(firstw,bd=5)
Bu6 = Entry(firstw,bd=5)
Bu7=Entry(firstw,bd=5)
Bu8=Entry(firstw,bd=5,textvariable=Bu8_data)
Bu9=Entry(firstw,bd=5,textvariable=Bu9_data)
Bu10 = Entry(firstw,bd=5)
Bu11 = Entry(firstw,bd=5)
Bu12 = Entry(firstw,bd=5)
Bu13 = Entry(firstw,bd=5)
Bu14 = Entry(firstw,bd=5)

                              # buttons-part
Bu_3 = Button(firstw,text="Exit",bg=button_color,command=Exit,bd=5) # exit 
Bu_4 = Button(firstw,text="Save",bg=button_color,command=do,bd=5) # save the work  
                   # positons
en1_data.place(x=360,y=160,width=100)
en2_data.place(x=360,y=240 ,width=100)
en3_data.place(x=360,y=320,width=100)
en4_data.place(x=360,y=385,width=100)
en5_data.place(x=360,y=465,width=100)
en6_data.place(x=360,y=540,width=100)
en7_data.place(x=360,y=600,width=100)
Bu1.place(x=500,y=160,width=100)
Bu2.place(x=500,y=240,width=100)
Bu4.place(x=500,y=385,width=100)
Bu5.place(x=500,y=460,width=100)
Bu6.place(x=500,y=540
              ,width=100)
Bu7.place(x=660,y=160,width=100)
Bu8.place(x=660,y=240,width=100)
Bu9.place(x=660,y=320,width=100)
Bu10.place(x=660,y=385,width=100)
Bu11.place(x=660,y=460,width=100)
Bu12.place(x=660,y=540
              ,width=100)
Bu13.place(x=660,y=595
              ,width=100)
Bu14.place(x=500,y=600
              ,width=100)


Bu_3.place(x=400,y=650
          ,width=100,height=30)
Bu_4.place(x=520,y=650,width=100,height=30)

                                                 





firstw.mainloop()
