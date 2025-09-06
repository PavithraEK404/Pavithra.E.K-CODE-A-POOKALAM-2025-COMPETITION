# --- Outer boundary circle (thick red border) ---
outer = circle(r=130, fill="black")

# --- Outer pointed petals (yellow + orange alternating) ---
#pet_yellow = rectangle(w=18, h=40, fill="yellow") | translate(x=140)
#pet_orange  = rectangle(w=10, h=35, fill="orange")  | translate(x=140)
r1 = rectangle(w=230, h=230, fill="brown", stroke="brown") | repeat(15, rotate(angle=50))
r2 = rectangle(w=220, h=220, fill="red", stroke="red") | repeat(15, rotate(angle=50))
r3 = rectangle(w=210, h=210, fill="orange", stroke="orange") | rotate(15) | repeat(15, rotate(angle=50))
r4 = rectangle(w=200, h=200, fill="yellow", stroke="yellow") | repeat(15, rotate(angle=50))
pet_layer  = r1 + r2 + r3 + r4


# --- Middle fan petals (layered ellipses with color bands) ---
def fan_band():
    colors = ["red", "orange", "yellow", "white"]
    sizes  = [(120, 60), (100, 50), (80, 40), (60, 30)]
    band = ellipse(w=sizes[0][0], h=sizes[0][1], fill=colors[0])
    for (w, h), c in zip(sizes[1:], colors[1:]):
        band = band + ellipse(w=w, h=h, fill=c)
    return band

middle = fan_band() | repeat(6, rotate(angle=360/6))

# --- Inner hex star (layered petals in red, orange, yellow) ---
def layered_diamond():
    colors = ["red", "orange", "yellow"]
    base = rectangle(w=20, h=90, fill=colors[0])
    d = base
    for i, c in enumerate(colors[1:], start=1):
        d = d + rectangle(w=20*(1 - i*0.3), h=90*(1 - i*0.3), fill=c)
    return d

inner_star = layered_diamond() | repeat(6, rotate(angle=360/6))

# --- Central circle (green) ---
center_circle1 = circle(r=30, fill="brown")
center_circle2= circle(r=25, fill="red")
center_circle3= circle(r=20, fill="yellow")
center_circle= center_circle1 + center_circle2 + center_circle3
# --- Decorative inner ring (small dots in blue) ---
dot = circle(r=15, fill="red") | translate(x=110)
inner_dots1 = dot | repeat(40, rotate(angle=360/40))
dot = circle(r=10, fill="orange") | translate(x=90)
inner_dots2 = dot | repeat(36, rotate(angle=360/36))
dot = circle(r=8, fill="yellow") | translate(x=70)
inner_dots3= dot | repeat(32, rotate(angle=360/32))

# --- Combine all layers ---
design = pet_layer + outer + middle + inner_star + center_circle + inner_dots1+inner_dots2+inner_dots3

def logo():
    # Top rectangles
    r1 = rectangle(w=105, h=50, fill='#2CC0CF', stroke='none', x=-45, y=70)
    r2 = rectangle(w=50, h=50, fill='#2078F9', stroke='none', x=50, y=70)
    top = r1 + r2

    # Middle rectangle
    mid = rectangle(w=175, h=50, fill='#FECD3D', stroke='none', x=-12, y=0)

    # Bottom rectangles
    r3 = rectangle(w=70, h=50, fill='#EE3C35', stroke='none', x=-65, y=-70)
    r4 = rectangle(w=42, h=50, fill='#91BF23', stroke='none', x=0, y=-70)
    r5 = rectangle(w=42, h=50, fill='#045768', stroke='none', x=52, y=-70)
    bottom = r3 + r4 + r5

    # Combine all layers
    logo = top + mid + bottom
    return logo | scale(0.12) | translate(x=1)

# Build logo
logo = logo()

# Show design inline (works in Jupyter/Colab)
show(design+logo)