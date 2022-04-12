# numpy arrays to adjust pixels example

size(200, 200)

array = np.zeros((height, width, 3))
array[10:20, 30:60, 1] = 255  # green
#array[:60, :, 0] = 255       # red
#array[:, -60:, 2] = 125      # blue
set_np_pixels(array, bands='RGB')
print(array)
