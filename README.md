# find_shapes
Find shapes from image

## Approach:

#### Convert image to grayscale 
#### Apply Median blur to smooth the image
#### Sharpen the image to enhance edges
#### Apply Threshold
#### Perform morphological transformations
#### Find contours
#### Filter using minimum/maximum threshold area
#### Calculate (x1,y1) and (x2, y2)
#### Crop and save ROI


## Command to run:
### python3 find_square.py -f 3.bmp --min_area 3000 --max_area 6000 
