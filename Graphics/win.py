
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import requests








def update_gif():
    global current_frame, timer_id, gif_images, gif_delays
    current_frame = (current_frame + 1) % len(gif_images)
    gif_label.config(image=gif_images[current_frame])
    gif_label.image = gif_images[current_frame]
    if timer_id is not None:
        app.after_cancel(timer_id)  # Cancel the previous update_gif call
    timer_id = app.after(gif_delays[current_frame] + 10, update_gif)  # Add a 10ms delay  # Schedule a new call # Use frame-specific delay

def load_gif(directory, speed=1.0):
    gif = Image.open(directory)
    gif_images = []
    gif_delays = []
    for frame in ImageSequence.Iterator(gif):
        img = ImageTk.PhotoImage(frame.resize((450, 450)))
        gif_images.append(img)
        delay = frame.info.get('duration', 100)  # Extract frame delay or default to 100 ms
        gif_delays.append(int(delay * speed))  # Multiply delay by speed factor
    return gif_images, gif_delays



def change_gif(active=True):
    global gif_images, gif_delays, current_frame, timer_id
    if timer_id is not None:
        app.after_cancel(timer_id)  # Cancel the previous update_gif call
        timer_id = None  # Ensure timer_id is reset after cancellation
    if active:
        gif_images, gif_delays = active_gif, active_delays
    else:
        gif_images, gif_delays = unactive_gif, unactive_delays
    current_frame = 0
    update_gif()  # Start the GIF animation with the new frames and delays






app = Tk()

app.geometry("960x540+0+0")
app.title("Voice Assistant")

app.resizable(True, True)  # Enable resizing
app.wm_minsize(960, 540)  # Set minimum window size to 1280x720



Vframe = Frame(app, bg='black')
Vframe.place(relwidth=1, relheight=1, x=0, y=0)

TitleVFrame = Frame(Vframe, bg="#38079c")
TitleVFrame.place(relwidth=1, relheight=0.10)
TitleVLable = Label(TitleVFrame, fg='white', font=("Helvetica", "25", "bold"), text="TECHNO THE VOICE ASSISTANT", bg="#38079c")
TitleVLable.place(relx=0.5, rely=0.5, anchor='center')

GFrame = Frame(Vframe, bg='black')
GFrame.place(relwidth=1, relheight=1, x=0, rely=0.10)
gif_label = Label(GFrame, bg='black')
gif_label.place(relx=1.01, rely=0.45, anchor=E, relwidth=0.5, relheight=1.0)

# Load the GIFs along with their frame delays
unactive_gif, unactive_delays = load_gif("Graphics/UnActiveOrb.gif", speed=1.0)
active_gif, active_delays = load_gif("Graphics/ActiveOrb.GIF", speed=0.1)

gif_images, gif_delays = unactive_gif, unactive_delays
current_frame = 0
timer_id = None
update_gif()

output_text = Text(GFrame, bg='#F8F8FF',fg='black', font=("Helvetica", "16", "bold"), wrap=WORD, borderwidth=5, relief="groove")
output_text.place(relheight=0.9,relwidth=0.5)

output_text.insert(END, "Say 'Activate' to Get Started!\n\nFEATURES:\n 1) Date | Time | Year\n 2) Capture a Selfie\n 3) Smart Math Calculations\n 4) Stay Updated with Daily News\n 5) Enjoy a Laugh with Funny Jokes\n 6) Never Forget with Reminders\n 7) Organize Your Day with Schedules\n 8) Test Your Internet Speed\n 9) Play Exciting Games\n 10) Get Real-Time Weather Updates\n 11) Effortless Surfing on YouTube, Wikipedia, Google\n 12) Control YouTube Hands-Free\n 13) Open & Close Apps with Just Your Voice\n 14) Generate Stunning Images\n 15) Unleash the Power of AI\n", 'placeholder')

output_text.tag_configure('placeholder', foreground='grey')

oScroll = Scrollbar(GFrame, orient="vertical")
oScroll.place(relheight=1.0,relx=0.50)

output_text.config(yscrollcommand=oScroll.set)
oScroll.config(command=output_text.yview)






