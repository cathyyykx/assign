x = 0
y = 250
page = 0
text_size = 30


def setup():
    global sat_img, back_img
    size(640, 480)
    
    back_img = loadImage("background.png")
    sat_img = loadImage("fairy.png")


def draw():
    global x, y, text_size
    
    
    while x == width:
        x = 0
        
    while y == width:
        y = 0
        
    x += 2.5
    y += 2
    
    
    background(back_img)  # sky blue

    # moon
    fill(255, 255, 153)
    ellipse(540, 80, 95, 90)
    
    # tree
    fill(102, 51, 0)
    rect(480, 280, 50, 120)
    
    fill(0, 132, 39)
    triangle(450, 280, 560, 280, 505, 200)
    
    # house
    fill(163, 65, 0)
    rect(width / 2 - 150, 300, 150, 110)
    
    fill(249, 0, 0)
    triangle(130, 300, 360, 300, 245, 180)
    
    # clouds
    fill(255)
    noStroke()
    ellipse(x, height/2 - 100, 60, 60)
    ellipse(x+30, height/2 - 100, 60, 60)
    ellipse(x+15, height/2 - 120, 60, 60)
    ellipse(x + 45, height/2 - 120, 60, 60)
    
    ellipse(y, height/2 - 30, 50, 50)
    ellipse(y + 35, height / 2 - 30, 50, 50)
    ellipse(y + 15, height / 2 - 50, 50, 50)
    ellipse(y + 45, height / 2 - 50, 50, 50)
    
    ellipse(y + 50, height/2 - 150, 50, 50)
    ellipse(y + 85, height / 2 - 150, 50, 50)
    ellipse(y + 60, height / 2 - 175, 50, 50)
    ellipse(y + 75, height / 2 - 175, 50, 50)
    ellipse(y + 105, height / 2 - 170, 50, 50)
    
    image(sat_img, x - 5, 97, 55, 55)
    
    if page == 0:
        textAlign(CENTER, CENTER)
        translate(width/2, height/2)
        textSize(text_size)
        fill(255, 255, 255, 255-text_size/2)
        text("Welcome to my world!", 10, 10)
    elif page == 1:
        textAlign(CENTER, CENTER)
        translate(width/2, height/2)
        textSize(text_size)
        fill(255, 255, 255, 255-text_size/2)
        text("Now enjoy it!", 0, 0)
        
        
def mousePressed():
    global page
    page += 1
    if page == 2:
        page = 0
