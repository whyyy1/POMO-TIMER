from tkinter import *
import datetime
# CONSTANTS 
WORK_MIN = 25
SHORT_BREAK = 5 *60
LONG_BREAK = 15 *60
REPS = 0 
COUNT = 0
TC = 0
window = Tk()
title_label = None
timer = None
timerInput=None
repInput=None
textR=None
textT=None
canvas = None
checks = None
repL = None
k = None
exitButton = None

startButton = None

resetButton = None

def runIT():
    global window 
    global title_label
    global timer 
    global timerInput
    global repInput
    global textR
    global textT
    global canvas 
    global checks 
    global repL 
    global k 
    global exitButton
    global startButton
    global resetButton
    window.attributes('-topmost', True)
    window.minsize(width=600,height=400)
    window.title('Work smarter and harder')
    window.config(bg='#F4F2DE',pady=25)
    mainTitle = Label(text='POMO',fg='#7A9D54', bg='#F4F2DE', font=('Aria',50,'bold'))
    mainTitle.grid(row=0,column=1)
    descTitle = Label(text='short breaks = 5 min / long breaks = 15 min',fg='#7A9D54', bg='#F4F2DE', font=('Aria',25,'bold'))
    descTitle.grid(row=1,column=1)


    # Inputs
    # timeStr = StringVar()
    timerInput = Spinbox(from_=1,to=60, width=5) 
    time = f'{timerInput.get()}:00'
    textT = Label(text = 'Time')
    textT.grid(row=5,column=1)
    timerInput.grid(row=6,column=1)

    # Rep input 
    repStr = StringVar()
    repInput = Spinbox(from_=1,to=10, width=5)
    textR = Label(text = 'Reps')
    textR.grid(row=5,column=2)
    repInput.grid(row=6, column=2)


    k = Label(text=time, fg='#7A9D54', bg='#F4F2DE',  font=('Aria',50,'bold'),)
    k.grid(row=4,column=1)
    repL = Label(text='Timer', fg='#7A9D54',  font=('Aria',25,'bold'),)
    repL.grid(row=2,column=1)

    canvas = Canvas(width=200,height=400,highlightthickness=0)
    canvas.config(bg='#F4F2DE')
    imageBG = PhotoImage(file='./kumiko-tomato.gif')
    checks = Label(text='')
    checks.grid(row=4,column=2)
    canvas.create_image(100,200,image=imageBG)
    # k = canvas.create_text(100,30,text=time,font=('Aria',35,'bold'))
    # i = canvas.create_rectangle(canvas.bbox(k),fill='#557A46')

    # canvas.tag_lower(i,k)
    canvas.grid(column=1,row=3,)
    title_label = Label(text='', fg='#7A9D54', font=('Aria',25,'bold'),)
    title_label.grid(row=7,column=1)
    exitButton = Button(text='Exit', command=close,highlightthickness=0)
    exitButton.grid(row=8,column=0,padx = 50, pady = 25)
    startButton = Button(text='start', command=start,highlightthickness=0)
    startButton.grid(row=8,column=1,padx = 50, pady = 25)
    resetButton = Button(text='reset', command=resetTime,highlightthickness=0)
    resetButton.grid(row=8,column=2,padx = 50, pady = 25)

    window.mainloop()

def start():
    global REPS
    global COUNT
    global TC
    global window 
    global title_label 
    global timer 
    global timerInput
    global repInput
    global textR
    global textT
    global canvas 
    global checks 
    global repL 
    global k 
    startButton.grid_remove()
    timerInput.grid_remove()
    repInput.grid_remove()
    textR.grid_remove()
    textT.grid_remove()
   
    
    
    title_label.config(text=f'Reps - {TC} / {repInput.get()} Done')
    
    totalTime = int(timerInput.get())  *60 
    
    SHORT_BREAKS = 5 *60  
    LONG_BREAKS = 15 *60   
    REPS += 1 
    if TC >0:
        marks = ''
        for _ in range(TC):
            marks += '✔'
            checks.configure(text=marks, font=('Aria',35,'bold'))
                
    if int(TC) == int(repInput.get()):
        print('all done')
        window.configure(bg='red')
        canvas.config(bg='red')
        k.configure(bg='red')
        repL.configure(text = f'DONE!', fg='black')
    else:

                    
        print(f'{TC} / {repInput.get()} Done')
        if REPS % 2 != 0:
            window.configure(bg='green')
            canvas.config(bg='green')
            k.configure(bg='green')
            repL.configure(text = f'Work', fg='black') 
            countDown(totalTime )
            
            
        else:
            
            if COUNT == 3:
                COUNT = 0 
                
                repL.configure(text = f'Long Break',fg='black')
                window.configure(bg='orange')
                canvas.config(bg='orange')
                k.configure(bg='orange')
                countDown(LONG_BREAKS)
                
                print('long break')
                TC += 1
                
                    
            else:
                window.configure(bg='yellow')
                repL.configure(text = f'Short Break', fg='black')
                canvas.config(bg='yellow')
                k.configure(bg='yellow')
                countDown(SHORT_BREAKS)
                print('short break')
            COUNT += 1
def resetTime():
    global REPS
    global COUNT
    global TC
    global window 
    global timer 
    global timerInput
    global repInput
    global textR
    global textT
    global canvas 
    global checks 
    global repL 
    global k
    global title_label 
    REPS = 0 
    COUNT = 0
    TC = 0
    title_label.configure(text='')
    checks.grid_remove()
    repL.grid_remove()
    window.after_cancel(timer)
    runIT()
    
    
def countDown(count):
    global timer
    # Create a timedelta object
    delta = datetime.timedelta(seconds=count)

    # Extract minutes and seconds
    minutes, seconds = divmod(delta.total_seconds(), 60)
    
    # Format as minutes and seconds
    
   
            
    if seconds < 10:
        formatted_time = f"{int(minutes)}:0{int(seconds)}"
        if seconds == 0.0:
        
            formatted_time = f"{int(minutes)}:00"
    else:
    
        formatted_time = f"{int(minutes)}:{int(seconds)}"
    k.configure(text=formatted_time)    
    # canvas.itemconfig(k,text=formatted_time)
    if count > 0:
        timer = window.after(1000,countDown,count-1)
    else:
        start()
        

def close():
    exit()



# exitButton.pack()


if __name__ == "__main__":
   
    runIT()