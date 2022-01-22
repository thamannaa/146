from tkinter import *
root=Tk()
root.title("fibonacci series")
root.geometry("400x400")
enter_number=Entry(root)
label=Label(root,text="fibonacci series")
label2=Label(root,text="fibonacci sum")

def fibonacci():
    input_number=int(enter_number.get())
    first_no=0
    second_no=1
    sum=0
    sum2=0
    counter=1
    
    while (counter<=input_number):
        label["text"]+=str(sum)+" "
        label2["text"]=str(sum2)
        counter=counter+1
        first_no=second_no
        second_no=sum
        sum=first_no+second_no
        sum2=sum2+sum 
        
enter_number.pack()  
btn=Button(root,text="show fibonacci series",command=fibonacci,fg="white",bg="blue")
btn.pack()
label.pack()
label2.pack()

root.mainloop()


