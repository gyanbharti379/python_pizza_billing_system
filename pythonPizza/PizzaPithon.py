import tkinter
import tkinter.ttk
import tkinter.messagebox
from PIL import Image,ImageTk

class PythonPizza:

    price_for_large_pizza = 899
    price_for_medium_pizza = 499
    price_for_small_pizza = 299
    price_for_pepperoni = 99
    totalprice = 0
    totalqty = 0
    pre_item = ""
    pre_price = 0
    itemlist =[]
    dot = "."*10
    welcome = (f"{dot}Welcome to the Python Pizza{dot}\n \nwe are happy to serve you\n \n"
               f"Note: Select Pizza in the list and click add to \nadd the item in the cart \n \n"
               f"Note: if you add many items in the cart and you \nneed to scroll by using mouse wheel")

    def __init__(self):

# --------------Area for creating window ------------------START-------------------------#

        self.master = tkinter.Tk()
        self.master.title("Python Pizaa....")
        self.master.geometry("900x650+270+50")
        self.master.resizable(False, False)

        img4 = Image.open("images/pizzaCompanyLogo.jpg")
        img4 = ImageTk.PhotoImage(img4)
        self.master.iconphoto(True, img4)

# need dot in many times ----------------------------------------------------------#
        self.dot = "."*80

# Area to add widgets in window -------------------------START--------------------------#
        self.frame = tkinter.LabelFrame(self.master, text=f"Welcome to Python Pizza{self.dot}", font=("bookman old style",15,"bold"), background="pink",
                                        fg="red")

        self.imgtitle = Image.open("images/titleLogo.jpg")
        self.imgtitle = self.imgtitle.resize((860,218),Image.BOX)
        self.imagePhototitle = ImageTk.PhotoImage(self.imgtitle)

        self.imglarge = Image.open("images/largePizza.png")
        self.imglarge = self.imglarge.resize((90, 90), Image.BOX)
        self.imagePhotoLarge = ImageTk.PhotoImage(self.imglarge)

        self.imgMedium = Image.open("images/mediumPizza.png")
        self.imgMedium = self.imgMedium.resize((90, 90), Image.BOX)
        self.imagePhotoMedium = ImageTk.PhotoImage(self.imgMedium)

        self.imgSmall = Image.open("images/smallPizza.png")
        self.imgSmall = self.imgSmall.resize((90, 90), Image.BOX)
        self.imagePhotoSmall = ImageTk.PhotoImage(self.imgSmall)

        self.frame.place(x=20,y=10)
        self.label = tkinter.Label(self.frame,image=self.imagePhototitle, compound=tkinter.LEFT)
        self.label.pack()

        self.label1 = tkinter.Label(self.master, text=f"{PythonPizza.dot}We have 3 types of pizzaa{PythonPizza.dot}",
                                    font=("bookman old style",20,"bold"), width=48, height=2,  background="green", fg="white")
        self.label1.place(x=20, y=260 )

        self.pizzaFrame = tkinter.LabelFrame(self.master, text="List of Pizzaaaa", background="green", fg="yellow")
        self.pizzaFrame.place(x=20,y=320)



        self.labelLarge = tkinter.Label(self.pizzaFrame, image=self.imagePhotoLarge, compound=tkinter.LEFT,
                                        text="Large pizzaa ......... Rs. %d" %(self.price_for_large_pizza),font=("bookman old style",15,"bold"), background="green", fg="yellow")
        self.labelLarge.grid(row=2, column=0, sticky="w")

        self.labelMedium = tkinter.Label(self.pizzaFrame, image=self.imagePhotoMedium, compound=tkinter.LEFT,
                                         text="Medium pizzaa ..... Rs. %d" %(self.price_for_medium_pizza),font=("bookman old style",15,"bold"), background="green", fg="yellow")
        self.labelMedium.grid(row=3, column=0, sticky="w")

        self.labelSmall = tkinter.Label(self.pizzaFrame, image=self.imagePhotoSmall, compound=tkinter.LEFT,
                                        text="Small pizzaa ........ Rs. %d" %(self.price_for_small_pizza),font=("bookman old style",15,"bold"), background="green", fg="yellow")
        self.labelSmall.grid(row=4, column=0, sticky="w")

        self.billFrame = tkinter.LabelFrame(self.master, text="Billing Here . . .")
        self.billFrame.place(x=400, y=320)

        self.billArea = tkinter.Text(self.billFrame, width=50 ,height=11, padx=20, pady=5)
        self.billArea.insert(tkinter.END,self.welcome)
        self.billArea.grid(row=0,column=0, padx=20, pady=20, sticky="news")

        self.countSpinbox = tkinter.Spinbox(self.billFrame, from_=1, to=10, increment=1, width=5)
        self.countSpinbox.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.addItemCombobox = tkinter.ttk.Combobox(self.billFrame, width=12,
                                                    values=["Select","large pizza", "Medium Pizza", "Small Pizza", "Pepperoni"])
        self.addItemCombobox.grid(row=1, column=0, padx=72, pady=20, sticky="w")

        self.addbtnimage = Image.open("images/addimage.png")
        self.addbtnimage = self.addbtnimage.resize((30, 20), Image.BOX)
        self.imagePhotoaddbtnimage = ImageTk.PhotoImage(self.addbtnimage)

        self.addButton = tkinter.Button(self.billFrame, text="Add", width=88, command=self.additem, image=self.imagePhotoaddbtnimage, compound=tkinter.LEFT)
        self.addButton.grid(row=1, column=0, padx=170,pady=20, sticky="w")

        self.delbtnimage = Image.open("images/deleteimage.jpg")
        self.delbtnimage = self.delbtnimage.resize((30, 20), Image.BOX)
        self.imagePhotodelbtnimage = ImageTk.PhotoImage(self.delbtnimage)

        self.delButton = tkinter.Button(self.billFrame, text="Delete", width=88, command=self.deleteitem, image=self.imagePhotodelbtnimage, compound=tkinter.LEFT)
        self.delButton.grid(row=1, column=0, padx=118, pady=20, sticky="e")

        self.calbtnimage = Image.open("images/calimage.png")
        self.calbtnimage = self.calbtnimage.resize((30, 20), Image.BOX)
        self.imagePhotocalbtnimage = ImageTk.PhotoImage(self.calbtnimage)

        self.calButton = tkinter.Button(self.billFrame, text="Total",width=88, command=self.calculate, image=self.imagePhotocalbtnimage,compound=tkinter.LEFT)
        self.calButton.grid(row=1, column=0, padx=20, pady=20, sticky="e")

# Area to add widgets in window -------------------------END--------------------------#

        totalItem = ""
        lenItem =0

        self.master.mainloop()

# --------------Area for creating window ------------------END-------------------------#

    def additem(self):

        if self.addItemCombobox.get() == "" or self.addItemCombobox.get().lower() == "select":
            tkinter.messagebox.showerror("Error","Please select Items in list")
        else:
            qty = int(self.countSpinbox.get())
            item = self.addItemCombobox.get()

            price = 0

            if item == "large pizza":

                    price = qty*self.price_for_large_pizza
                    self.totalqty += qty
                    self.totalprice += price

                    self.totalItem = "%d X" % (qty) + " " + item + " of               Rs. %d" % (price) + "\n"
                    self.itemlist.append(self.totalItem)
                    self.billArea.delete("1.0", tkinter.END)
                    for item in self.itemlist:
                        self.billArea.insert(tkinter.END, str(item))

            elif item == "Medium Pizza":

                    price = qty * self.price_for_medium_pizza
                    self.totalqty += qty
                    self.totalprice += price

                    self.totalItem = "%d X" % (qty) + " " + item + " of              Rs. %d" % (price) + "\n"
                    self.itemlist.append(self.totalItem)
                    self.billArea.delete("1.0", tkinter.END)
                    for item in self.itemlist:
                        self.billArea.insert(tkinter.END, str(item))

            elif item == "Small Pizza":

                    price = qty * self.price_for_small_pizza
                    self.totalqty += qty
                    self.totalprice += price

                    self.totalItem = "%d X" %(qty) + " " + item + " of               Rs. %d" %(price) + "\n"
                    self.itemlist.append(self.totalItem)
                    self.billArea.delete("1.0", tkinter.END)
                    for item in self.itemlist:
                        self.billArea.insert(tkinter.END, str(item))

            elif item == "Pepperoni":

                    price = qty * self.price_for_pepperoni
                    self.totalqty += qty
                    self.totalprice += price

                    self.totalItem = "%d X" %(qty) + " " + item + " of                 Rs. %d" %(price) + "\n"
                    self.itemlist.append(self.totalItem)
                    self.billArea.delete("1.0", tkinter.END)
                    for item in self.itemlist:
                        self.billArea.insert(tkinter.END, str(item))


    def deleteitem(self):
        self.billArea.delete("1.0", tkinter.END)
        self.billArea.insert(tkinter.END,self.welcome)
        self.itemlist.clear()

        self.totalprice = 0
        self.totalqty = 0

        self.countSpinbox.delete(0,1)
        self.countSpinbox.insert(0,"1")

        self.addItemCombobox.current(0)


    def calculate(self):

        if self.totalqty == 0:
            self.deleteitem()
        else:
            testspace = "__"*20+"\n"

            total = self.totalprice + self.totalprice*0.025 + self.totalprice*0.025
            self.totalItem = testspace + "Subtotal of %d" % (self.totalqty) + " items of          Rs. %d" % (self.totalprice) + "\nCharges" + "__" *16 + "\nCGST @2.5" + "__" * 12 + "Rs. %d" % (self.totalprice * 0.025) + "\nSGST @2.5" + "__" * 12 + "Rs. %d" % (self.totalprice * 0.025) + "\nBill of %d" % (self.totalqty) + " items of              Rs. %d" % (total)+"\n" + testspace
            self.itemlist.append(self.totalItem)
            self.billArea.delete("1.0", tkinter.END)
            for item in self.itemlist:
                self.billArea.insert(tkinter.END, str(item))

            self.countSpinbox.delete(0, 1)
            self.countSpinbox.insert(0, "1")

            self.addItemCombobox.current(0)

if __name__ == "__main__":
    PythonPizza()