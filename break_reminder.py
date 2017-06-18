import time
import webbrowser
import random

for _ in range(1,10):
	time.sleep(45*60)
	urls = ["https://www.youtube.com/watch?v=-bzWSJG93P8","https://www.youtube.com/watch?v=Gw_o7XUX3fg",
	        "https://www.youtube.com/watch?v=eHFA_wEK_00","https://www.youtube.com/watch?v=_D0ZQPqeJkk"]
	webbrowser.open(random.choice(urls))