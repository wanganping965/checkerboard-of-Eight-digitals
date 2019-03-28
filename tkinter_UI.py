import tkinter
import tkinter.messagebox
import A_star
import json
import random
from PIL import Image, ImageTk

def main():
    routes = {}
    cur_step = 0
    steps = 0
    whether_set_original = False
    original_status = []
    root = tkinter.Tk()
    root.title("eight_digital_checkerboard")
    root.geometry("600x700")
    # root.resizable(width=True, height=True)
    root.tk.eval('package require Tix')

    input_l = tkinter.Label(root,font = ('Helvetica', '16', 'bold'),bg="green",
                            text="The original 3*3 checkerboard is random generated\n Final status is the sequence\"123456780\"")
    input_l.pack()
    input_l1 = tkinter.Label(root, text="you can also input original checkerboard sequence below",font=("Arial", 14),bg="blue")
    input_l1.pack(fill = tkinter.X)
    origi_status_text = tkinter.Entry(font = ('Helvetica', '14', 'bold'))  # create a text input field
    origi_status_text.pack()

    # add a move status label to show the current status and move status
    move_status_label = tkinter.Label(root, text="Need ** times of move totally, now it's the 0th status", font=("Arial", 16),
                             bg="orange")
    move_status_label.pack(fill=tkinter.X)
    #
    # input_l2 = tkinter.Label(root, text="input the original checkerboard sequence below")
    # input_l2.pack()
    # goal_status_text = tkinter.Entry(font = ('Helvetica', '14', 'bold'))  # create a text input field
    # goal_status_text.pack()

    imgpath1 = 'previous.jpg'
    img1 = Image.open(imgpath1)
    photo_left = ImageTk.PhotoImage(img1)
    imgpath2 = 'next.jpg'
    img2 = Image.open(imgpath2)
    photo_right = ImageTk.PhotoImage(img2)

    photo0 = ImageTk.PhotoImage(Image.open("./image/0.png"))
    photo1 = ImageTk.PhotoImage(Image.open("./image/1.png"))
    photo2 = ImageTk.PhotoImage(Image.open("./image/2.png"))
    photo3 = ImageTk.PhotoImage(Image.open("./image/3.png"))
    photo4 = ImageTk.PhotoImage(Image.open("./image/4.png"))
    photo5 = ImageTk.PhotoImage(Image.open("./image/5.png"))
    photo6 = ImageTk.PhotoImage(Image.open("./image/6.png"))
    photo7 = ImageTk.PhotoImage(Image.open("./image/7.png"))
    photo8 = ImageTk.PhotoImage(Image.open("./image/8.png"))

    def valid_input(status):
        if len(status) != 9:
            #
            tkinter.messagebox.showinfo(title="prompt", message="check the length of your input sequence")
            print("check your input status sequence,length is not enough")
            return False
        nums = {}
        digitals = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        flag = True
        for c in status:
            if not c in digitals:
                flag = False
                tkinter.messagebox.showinfo(title="prompt", message="the unexpected char in the input sequence")
                print("the invalid input char in the sequence")
                break
            nums[c] = 1
        if flag:
            for digital in digitals:
                if nums.get(digital, 0) == 0:
                    flag = False
                    tkinter.messagebox.showinfo(title="prompt",
                                                message="the input sequence is invalid, modify it as required")
                    print("the input sequence is invalid")
                    break
        if flag:
            return True
        else:
            return False

    # confirm the input sequence is whether valid
    def confirm_the_input():
        nonlocal original_status
        nonlocal whether_set_original
        status = origi_status_text.get() # from Entry text field to get the sequence
        status = status.strip().replace(" ","") # type string without space

        if not valid_input(status):
            return
        status = [int(x) for x in status] # convert to the list ,type List[int]

        # to justify whether the sequence is a even sequence
        full_arr = {}
        with open("./even_sequence_result.json", "r") as ff:
            full_arr = json.load(ff)
        if not status in full_arr.values():
            tkinter.messagebox.showinfo(title="Input Error", message="Sorry, it's not a even sequence!")
            return
        # tkinter.messagebox.showinfo(title="prompt", message="the original status is valid")
        whether_set_original = True
        original_status = status[:]

        # change the picture original status
        move_status_label["text"] = "Need ** times of move totally, now it's the 0th status"
        for i in range(len(status)):
            path2 = "./image/" + str(status[i]) + ".png"
            photo = ImageTk.PhotoImage(Image.open(path2))
            if i == 0:
                Lab1.config(image=photo)
                Lab1.image = photo
            elif i == 1:
                Lab2.config(image=photo)
                Lab2.image = photo
            elif i == 2:
                Lab3.config(image=photo)
                Lab3.image = photo
            elif i == 3:
                Lab4.config(image=photo)
                Lab4.image = photo
            elif i == 4:
                Lab5.config(image=photo)
                Lab5.image = photo
            elif i == 5:
                Lab6.config(image=photo)
                Lab6.image = photo
            elif i == 6:
                Lab7.config(image=photo)
                Lab7.image = photo
            elif i == 7:
                Lab8.config(image=photo)
                Lab8.image = photo
            elif i == 8:
                Lab9.config(image=photo)
                Lab9.image = photo

    def get_optimal_route():
        nonlocal original_status
        nonlocal whether_set_original
        spac = 0

        if whether_set_original:
            for i in range(len(original_status)):
                if original_status[i] == 0:
                    spac = i
                    break
            print(spac)

        else:
            full_arr = {}
            with open("./even_sequence_result.json","r") as ff:
                full_arr = json.load(ff)
            num = random.randint(0,181439)
            original_status = full_arr.get(str(num))
            # spac = 0
            for i in range(len(original_status)):
                if original_status[i] == 0:
                    spac = i
                    break
            print(spac)
            print(original_status)
            # change the picture original status
            nums = original_status[:]
            for i in range(len(nums)):
                path2 = "./image/" + str(nums[i])+".png"
                photo = ImageTk.PhotoImage(Image.open(path2))
                if i == 0:
                    Lab1.config(image= photo)
                    Lab1.image = photo
                elif i == 1:
                    Lab2.config(image=photo)
                    Lab2.image = photo
                elif i == 2:
                    Lab3.config(image=photo)
                    Lab3.image = photo
                elif i == 3:
                    Lab4.config(image=photo)
                    Lab4.image = photo
                elif i == 4:
                    Lab5.config(image=photo)
                    Lab5.image = photo
                elif i == 5:
                    Lab6.config(image=photo)
                    Lab6.image = photo
                elif i == 6:
                    Lab7.config(image=photo)
                    Lab7.image = photo
                elif i == 7:
                    Lab8.config(image=photo)
                    Lab8.image = photo
                elif i == 8:
                    Lab9.config(image=photo)
                    Lab9.image = photo

        original_status = " ".join([str(x) for x in original_status])
        print("original status: " + json.dumps(original_status))

        goal_status = list("123456780")
        goal_status = " ".join(goal_status)
        # print(original_status)
        # print(goal_status)
        # write the valid original and goal sequence to the file
        with open("./eight.txt", "w") as f:
            f.write(original_status)
            f.write("\n")
            f.write(str(spac))
            f.write("\n")
            f.write(goal_status)
            f.write("\n")
        # find the optimal route
        A_star.main()

        # store the result in the global route
        nonlocal routes
        with open("./route_result.json", "r") as json_f:
            routes = json.load(json_f)
        nonlocal steps
        steps = len(routes)
        # modify the text of the move status label board to show the current status .
        move_status_label["text"] = "Need "+ str(steps-1) + " times of move totally, now it's the 0th status"

        print("the optimal routes is : "+json.dumps(routes))
        print("the current step is: "+json.dumps(cur_step))

    frame1 = tkinter.Frame(root, height=350, width=350, relief=tkinter.RIDGE, bg="pink")
    frame1.pack(fill=tkinter.NONE, ipady=2, expand=False)

    Lab1 = tkinter.Label(frame1, width =80,height = 80, image=photo1)
    Lab1.image = photo1
    Lab1.pack(padx=1, pady=1,side =tkinter.LEFT,expand = 1)

    Lab2 = tkinter.Label(frame1,  width =80,height = 80,  image=photo2)
    Lab2.image = photo2
    Lab2.pack(padx=1, pady=1,side=tkinter.LEFT)
    # Lab2.pack(fill=tkinter.X, expand=0.3)
    Lab3 = tkinter.Label(frame1,  width =80,height = 80,  image=photo3)
    Lab3.image = photo3
    Lab3.pack(padx=1, pady=1,side =tkinter.LEFT)

    frame2 = tkinter.Frame(root, height=350, width=350, relief=tkinter.RIDGE, bg="pink")
    frame2.pack(fill=tkinter.NONE, ipady=2, expand=False)

    Lab4 = tkinter.Label(frame2, width=80, height=80, image=photo4)
    Lab4.image = photo4
    Lab4.pack(padx=1, pady=1, side=tkinter.LEFT, expand=1)

    Lab5 = tkinter.Label(frame2, width=80, height=80, image=photo5)
    Lab5.image = photo5
    Lab5.pack(padx=1, pady=1, side=tkinter.LEFT)
    # Lab2.pack(fill=tkinter.X, expand=0.3)
    Lab6 = tkinter.Label(frame2, width=80, height=80, image=photo6)
    Lab6.image = photo6
    Lab6.pack(padx=1, pady=1, side=tkinter.LEFT)

    frame3 = tkinter.Frame(root, height=350, width=350, relief=tkinter.RIDGE, bg="pink")
    frame3.pack(fill=tkinter.NONE, ipady=2, expand=False)

    Lab7 = tkinter.Label(frame3, width=80, height=80, image=photo7)
    Lab7.image = photo7
    Lab7.pack(padx=1, pady=1, side=tkinter.LEFT, expand=1)

    Lab8 = tkinter.Label(frame3, width=80, height=80, image=photo8)
    Lab8.image = photo8
    Lab8.pack(padx=1, pady=1, side=tkinter.LEFT)
    # Lab2.pack(fill=tkinter.X, expand=0.3)
    Lab9 = tkinter.Label(frame3, width=80, height=80, image=photo0)
    Lab9.image = photo0
    Lab9.pack(padx=1, pady=1, side=tkinter.LEFT)

    frame4 = tkinter.Frame(root, height=350, width=350, relief=tkinter.RIDGE, bg="pink")
    frame4.pack(fill=tkinter.NONE, ipady=2, expand=False)
    confirm = tkinter.Button(frame4,text="Confirm input sequence", width=30, height=5, \
                             font=("Arial", 13),bg="red",command=confirm_the_input)
    confirm.pack(padx=1, pady=1, side=tkinter.LEFT, expand=1)

    run = tkinter.Button(frame4, text="Run the program",width=30, height=5, \
                         font=("Arial", 13),bg ="green",command=get_optimal_route)
    run.pack(padx=1, pady=1, side=tkinter.LEFT)

    def get_next_route_node():
        nonlocal cur_step
        nonlocal steps
        nonlocal routes
        if cur_step + 1 >= len(routes):
            tkinter.messagebox.showinfo(title="prompt", message="Now,it is the final status!")
            return
        cur_step += 1
        status = routes.get(str(cur_step))
        print("the status is "+json.dumps(status))

        move_status_label["text"] = "Need " + str(steps - 1) + \
                                    " times of move totally, now it's the "+str(cur_step)+"th status"
        for i in range(len(status)):
            path2 = "./image/" + str(status[i])+".png"
            photo = ImageTk.PhotoImage(Image.open(path2))
            if i == 0:
                Lab1.config(image= photo)
                Lab1.image = photo
            elif i == 1:
                Lab2.config(image=photo)
                Lab2.image = photo
            elif i == 2:
                Lab3.config(image=photo)
                Lab3.image = photo
            elif i == 3:
                Lab4.config(image=photo)
                Lab4.image = photo
            elif i == 4:
                Lab5.config(image=photo)
                Lab5.image = photo
            elif i == 5:
                Lab6.config(image=photo)
                Lab6.image = photo
            elif i == 6:
                Lab7.config(image=photo)
                Lab7.image = photo
            elif i == 7:
                Lab8.config(image=photo)
                Lab8.image = photo
            elif i == 8:
                Lab9.config(image=photo)
                Lab9.image = photo

    def get_previous_route_node():
        nonlocal routes
        nonlocal cur_step
        nonlocal steps
        if cur_step - 1 < 0:
            tkinter.messagebox.showinfo(title="prompt", message="Now,it is the original status")
            return
        cur_step -= 1
        status = routes.get(str(cur_step))
        print("the current step:")
        print("the status is "+json.dumps(status))

        move_status_label["text"] = "Need " + str(steps - 1) + \
                                    " times of move totally, now it's the " + str(cur_step) + "th status"
        for i in range(len(status)):
            path2 = "./image/" + str(status[i]) + ".png"
            photo = ImageTk.PhotoImage(Image.open(path2))
            if i == 0:
                Lab1.config(image=photo)
                Lab1.image = photo
            elif i == 1:
                Lab2.config(image=photo)
                Lab2.image = photo
            elif i == 2:
                Lab3.config(image=photo)
                Lab3.image = photo
            elif i == 3:
                Lab4.config(image=photo)
                Lab4.image = photo
            elif i == 4:
                Lab5.config(image=photo)
                Lab5.image = photo
            elif i == 5:
                Lab6.config(image=photo)
                Lab6.image = photo
            elif i == 6:
                Lab7.config(image=photo)
                Lab7.image = photo
            elif i == 7:
                Lab8.config(image=photo)
                Lab8.image = photo
            elif i == 8:
                Lab9.config(image=photo)
                Lab9.image = photo


    frame5 = tkinter.Frame(root, height=350, width=350, relief=tkinter.RIDGE, bg="pink")
    frame5.pack(fill=tkinter.NONE, ipady=2, expand=False)
    tkinter.Button(frame5, text="<-- previous step", width=220, height=120, \
                   font=("Arial", 8),bg="yellow",image= photo_left, \
                   command=get_previous_route_node).pack(fill=tkinter.X, expand=0.4,side=tkinter.LEFT)
    tkinter.Button(frame5, text="--> next step", width=220, height=120,\
                   font=("Arial", 8),bg="yellow",image= photo_right,\
                   command = get_next_route_node).pack(fill=tkinter.X, expand=0.4,side=tkinter.RIGHT)

    root.mainloop()

if __name__ == '__main__':
    main()
