# Known issues
- setting window size/geometry doesn't work on wayland
	- tkinter has no wayland backend, and wayland doesn't really allow this kind of operations anyway
- the month frame sizes change depending on screen size
	- probably something to do with the way tkinter calculates width and height? it doesn't seem to be pixels at least
	- smaller screen, [correct](./images/calendar_correct_frames.png) 
	- larger screen, [incorrect](./images/calendar_incorrect_frames.png) 
