
import xml.etree.cElementTree as ET
from tkinter import ttk
from tkinter import *
import lxml.etree

     
tr=lxml.etree.parse('atelier1.xml')

def GenerateXML():
    ntree = ET.parse('atelier1.xml')
    root = ntree.getroot()
    
    ids=list()
    for livre in root.findall('livre'):
        ids.append(livre.get('id'))
    nid=int(ids[-1])+1
    listBox.insert ( parent='', index='end', values=[nid,str(e1.get()),str(e2.get()) ,str(r.get())] )
    newrecord = ET.SubElement(root, "livre",id=str(nid),genre=str(r.get()))
    ET.SubElement(newrecord, "auteur").text = e2.get()
    ET.SubElement(newrecord, "titre").text = e1.get()
    ntree.write("atelier1.xml")    
    e1.delete(0,"end")
    e2.delete(0,"end") 
    
    

def delete():
     mytree = ET.parse('atelier1.xml')
     myroot = mytree.getroot()
    
     for livre in myroot.findall('livre'):
         ids=livre.get('id')
         id = listBox.focus()
         print (id)
         for siid in ids:
             if "I00"+(siid) == str(id):
                 myroot.remove(livre)
                 mytree.write("atelier1.xml")
     mytree.write('atelier1.xml')
     listBox.delete ( listBox.focus() )
    

def Update():
    mytree = ET.parse('atelier1.xml')
    myroot = mytree.getroot()
    selected =listBox.focus()
    for selected_item in listBox.selection():   
        item = listBox.item(selected_item)
        record = item['values']
        id=record[0]
        print(id)
    for livre in myroot.findall('livre'):
        idb = livre.get('id')
        print(idb) 
        if str(idb)==str(id):
            titre = e1.get()
            livre.find('titre').text= titre
            auteur = e2.get()
            livre.find('auteur').text= auteur
            genre = r.get()
            livre.set('genre',genre)  
            mytree.write("atelier1.xml")            
    listBox.item ( selected, text="", values=[id,str(e1.get()),str(e2.get()) ,str(r.get())] )
    e1.delete(0,"end")
    e2.delete(0,"end") 



root = Tk()
root.geometry("830x500")
root.title("bibliotique")
root.configure(bg="darkolivegreen")
Label(root,bg="darkolivegreen", text="Biblioteque", fg="white",font=("Courier", 25, "italic")).place(x=400, y=5)
Label(root,bg="darkolivegreen", fg="white",text="Titre").place(x=10, y=10)
Label(root,bg="darkolivegreen", fg="white",text="Auteur").place(x=10, y=40)
Label(root,bg="darkolivegreen", fg="white",text="genre").place(x=10, y=70)
global e1
global e2
e1 = Entry(root)
e1.place(x=140, y=10)
e2 = Entry(root)
e2.place(x=140, y=40)
r=StringVar() 
Radiobutton(root,bg="darkolivegreen",text="fiction",variable=r,value="fiction").place(x=140, y=70)
Radiobutton(root,bg="darkolivegreen",text="drame",variable=r,value="drame").place(x=140, y=90)
Radiobutton(root,bg="darkolivegreen",text="aventure",variable=r,value="aventure").place(x=200, y=70)
Radiobutton(root,bg="darkolivegreen",text="policier",variable=r,value="policier").place(x=200, y=90) 

Button(root, text="Add",height=3,fg="darkolivegreen", command=GenerateXML,width= 13).place(x=300, y=55)
Button(root, text="update",fg="darkolivegreen",height=3,command=Update, width= 13).place(x=450, y=55)
Button(root, text="Delete",fg="darkolivegreen",height=3,command=delete, width= 13).place(x=600, y=55)
 


    


ntreee = ET.parse('atelier1.xml')
roott = ntreee.getroot()      
ids=[]
for livre in roott.findall('livre'):
        ids.append((livre.get('id'),livre.find('titre').text,livre.find('auteur').text,livre.get('genre')))


           


def putVALUES(event):
    for selected_item in listBox.selection():   
        item = listBox.item(selected_item)
        record = item['values']
    e1.delete(0,"end")
    e2.delete(0,"end")
    r.initialize   
    e1.insert(0,record[1])
    e2.insert(1,record[2])
    r.set(record[3])




cols = ('id','Titre', 'Auteur', 'genre')
listBox = ttk.Treeview(root, columns=cols, show='headings')
for col in cols:
       listBox.heading(col, text=col)
       listBox.grid(row=1, column=0, columnspan=2)
       listBox.place(x=10, y=160)
for id in ids:    
       listBox.insert ( parent='', index='end', values=id )
       
listBox.bind('<Double-Button-1>',putVALUES)


root.mainloop()







# def show(ids,listbox):
#   cols = ('Titre', 'Auteur', 'genre')
#   listBox = ttk.Treeview(root, columns=cols, show='headings')
#   for col in cols:
#        listBox.heading(col, text=col)
#        listBox.grid(row=1, column=0, columnspan=2)
#        listBox.place(x=10, y=200)
#   for id in ids:    
#        listBox.insert ( parent='', index='end', values=id )
# show(ids)

# def refresh():
#     ntree = ET.parse('atelier1.xml')
#     roottt = ntree.getroot()      
#     ids=[]
#     for livre in roottt.findall('livre'):
#         ids.append((livre.find('titre').text,livre.find('auteur').text,livre.get('genre')))