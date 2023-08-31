import cv2

# 02/05/2023

# Configurable Parameters
# source = "cheetah.jpg"
source = "R.jpeg"
desti = f"resized_{source}"
# desti = f"resized.png"
# desti = f"resized.jpg"
# desti = f"resized.jpeg"
# desti = "resized_img.png"
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)

# Percent by which image is resized

# Calculate 50 oercent of original dimentions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(desti, output)
# cv2.waitKey(0)