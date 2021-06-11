
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from matplotlib import colors
try:
    from PIL import Image
except ImportError:
    import Image

image = Image.open('HNBusData-crop.jpg')
width, height = image.size
my_dpi=70
part_width = 42
part_height = 50
w, h = 42, 50

# data = [[0 for i in range(width)] for j in range(height)]

# Set up figure
fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
ax=fig.add_subplot(111)

# Remove whitespace from around the image
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)


# cmap = colors.ListedColormap(['white', 'blue'])
# bounds = [0,1,2]
# norm = colors.BoundaryNorm(bounds, cmap.N)


# Set the gridding interval: here we use the major tick interval
myInterval_x= width*1.0 / part_width
myInterval_y= height*1.0 / part_height
loc_x = plticker.MultipleLocator(base=myInterval_x)
loc_y = plticker.MultipleLocator(base=myInterval_y)
ax.xaxis.set_major_locator(loc_x)
ax.yaxis.set_major_locator(loc_y)

# Add the grid
ax.grid(which='major', axis='both', linestyle='-')

# Add the image
ax.imshow(image)
# ax.imshow(data, cmap=cmap, norm=norm)

# Find number of gridsquares in x and y direction
nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval_x)))
ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval_y)))

# Add some labels to the gridsquares
for j in range(ny):
    y=myInterval_x/2+j*myInterval_y
    for i in range(nx):
        x=myInterval_x/2.+float(i)*myInterval_x
        ax.text(x,y,'{:d} {:d}'.format(j, i),color='r',ha='center',va='center',fontsize=15)



# Save the figure
fig.savefig('busmap-grid50x42.jpg',dpi=my_dpi)