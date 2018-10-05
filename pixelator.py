from PIL import Image
import requests
from StringIO import StringIO

URL = requests.get("http://getdrawings.com/image/cartoon-portrait-drawing-65.jpg")

img = Image.open(StringIO(URL.content))

width, height = img.size

resolution = 7

block_size = 4

block_height = block_size
block_width = block_size

n_rows = height / (block_size)
n_cols = width / (block_size)

blocks = [[0 for x in range(n_cols)] for y in range(n_rows)] 

for row in range(0, n_rows, resolution):
	for col in range(0, n_cols, resolution):
		area = [col * block_size, row * block_size, col * block_size + block_width, row * block_size + block_height]
		blocks[row][col] = (img.crop(area))

x_offset = 0
y_offset = 0

small = Image.new('RGB', (n_cols * block_width / resolution, n_rows * block_height / resolution))

for row in range(0, n_rows, resolution):
	for col in range(0, n_cols, resolution):
		small.paste(blocks[row][col], [y_offset, x_offset])
		y_offset += block_height
	y_offset = 0
	x_offset += block_width

small.show()