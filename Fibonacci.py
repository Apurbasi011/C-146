from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci Series: ")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        label_flower["text"] = "Flower Is Fully Bloomed"
        label_spiral["text"] = "Spirals In Right Direction Are " + str(first_no) + " And Spirals In Left Direction Are " + str(second_no) + "\n. Total Spirals Are " + str(sum)
        
        btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
        btn.pack()
        label_series.pack()
        label_flower.pack()
        label_spiral.pack()
        root.mainloop()