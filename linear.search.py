import pyglet 
import random

window = pyglet.window.Window(width=1300, height=300, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()
numbers = random.sample(range(1, 100), 30) + [64]
random.shuffle(numbers)
current_index = 0
found_index = -1
search_complete = False
def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == 64:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True
pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)
@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        x = i * 40 + 10
        y = window.height // 2
        width = 40
        height = 40
        if i == current_index and not search_complete:
            color = (250, 128, 114)  # Salmon 
        elif i == found_index:
            color = (0, 255, 127)  # Springgreen 
        else:
            color = (200, 200, 200)  # Grey 
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()
        label.color = (0, 0, 0)  # black
        label.size = 20
        label.draw()
        
pyglet.app.run()