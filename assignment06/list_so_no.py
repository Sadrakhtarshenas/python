colors = ['blue','red','yellow','green','black']
new_color = "blue red yellow green black"

print('color =', colors)
print('colorstr =', new_color)

co = colors.copy()
print('copy',co)

colors.insert(2,'blue')
print('insert',colors)

new_co = new_color.index("green")
print ('index',new_color)

colors.extend(['red'])
print('extend',colors)