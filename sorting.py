import matplotlib
import numpy as np
import random
import matplotlib.pyplot as plt
from tkinter import *
import matplotlib.animation as animation


matplotlib.use('tkagg')
window = Tk()
window.title("SB Software: sorting")
# window.geometry('400x110')
window.resizable(0,0)
window.attributes("-alpha",0.975)
window.configure(bg="#ffffff")


a = 0
def startsorting(xx):
    global a
    global fig
    a = 0
    n = int(arraysize.get())
    sort = str(sortingname.get()).lower()

    arr = np.random.random_sample(n, ) * 100 + random.randint(-10, 10)
    temp = None
    y = np.linspace(0, n, n)


    def barlist(n):
        return [1 / float(n * k) for k in range(1, 6)]


    fig = plt.figure(dpi = 80, figsize=(14.65,5))
    plt.subplots_adjust(0.05,0.05,0.97,0.94, wspace=0.02, hspace=0.02)




    barcollection = plt.bar(y, arr)

    if (sort is not ""):
        if (sort == "bubble"):
            # bubble sort
            def animate(i):
                global a
                for j in range(i + 1, n):
                    a = a + 1
                    if (arr[i] > arr[j]):
                        temp = arr[i]
                        arr[i] = arr[j]
                        arr[j] = temp
                for i, b in enumerate(barcollection):
                    b.set_height(arr[i])


            animate(n)

        if (sort == "insertion"):
            # insertion  sort
            def animate(i):
                global a
                a += 1
                key = arr[i]
                # Move elements of arr[0..i-1], that are
                # greater than key, to one position ahead
                # of their current position
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
                for i, b in enumerate(barcollection):
                    b.set_height(arr[i])


            animate(n - 1)

        if (sort == "selection"):
            # selection  sort
            def animate(i):
                global a
                a += 1
                # Find the minimum element in remaining
                # unsorted array
                min_idx = i
                for j in range(i , len(arr)):
                    if arr[min_idx] > arr[j]:
                        min_idx = j
                        # Swarrp the found minimum element with
                # the first element
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                for i, b in enumerate(barcollection):
                    b.set_height(arr[i])


            animate(n - 1)

    speed = 20
    framespeed = 1

    if (n <= 100):
        speed = 100


    elif (n > 100):
        speed = 10


    elif (n > 200):
        speed = 10


    elif (n > 300):
        speed = 10


    elif (n > 400):
        speed = 10


    elif (n > 500):
        speed = 10


    elif (n > 600):
        speed = 10


    elif (n > 750):
        speed = 10


    elif (n > 950):
        speed = 10


    elif (n > 1000):
        speed = 10

    frame = int(n * framespeed)

    anim = animation.FuncAnimation(fig, animate, repeat=False, blit=False, frames=frame * 100,
                                   interval=speed)
    plt.title(sort.capitalize() +" Sort")
    plt.show()




searchbtn = Button(window, text ="start", padx=10, pady=2, bg="#4885ef", command=lambda:startsorting(None), bd=0, fg="#ffffff",
                   font=('comic sans ms', '11'))

arraylabel = Label(window, text="Enter Array Size: ", bg="#ffffff", bd=0, fg="#000000",
                   font=('comic sans ms', '11'))
arraysize = Entry(window, bg="#efefef", bd=0, fg="#000000", justify="center",
                   font=('comic sans ms', '11'))

sortinglabel = Label(window, text="Enter Sorting Algorithm: ", bg="#ffffff", bd=0, fg="#000000",
                   font=('comic sans ms', '11'))
sortingname = Entry(window, bg="#efefef", bd=0, fg="#000000", justify="center",
                   font=('comic sans ms', '11'))










arraylabel.pack(pady=4, padx=70)
arraysize.pack(pady=4, padx=70)
sortinglabel.pack(pady=4, padx=70)
sortingname.pack(pady=4, padx=70)
searchbtn.pack(pady=6, padx=70)


searchbtn.bind("<Return>",startsorting)
sortingname.bind("<Return>",startsorting)

window.mainloop()
