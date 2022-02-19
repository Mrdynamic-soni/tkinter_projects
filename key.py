from pynput.keyboard import Key, Listener

def show(key):

	print(f"{key} inputted")

	if key ==Key.is_pressed("l"):
		# Stop listener
		return False

# Collect all event until released
with Listener(on_press = show) as listener:
	listener.join()