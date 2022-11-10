# CorrectAngleOver2Img
AIM :rectify difference between 2 images wand wrap these in a new shape where all the epilines are parallel.

1/ Epipolar lines
  Here my 2 images : 
![image](https://user-images.githubusercontent.com/79518374/201160489-9c570cd8-cdd5-4f96-902e-139bc32cd966.png)
![image](https://user-images.githubusercontent.com/79518374/201160518-03a20831-cb6b-4dad-926a-65bc01132a9e.png)

By drawing the epipolar lines I get : 
![image](https://user-images.githubusercontent.com/79518374/201160677-f9209fca-5ba3-432a-a1dd-e62c0f514b2b.png)


  2/ Corect
Now let’s observe how we will do to rectify the difference between the two images.

![image](https://user-images.githubusercontent.com/79518374/201161222-490b0eb5-0083-4ec4-aeb9-fe20b271fdd6.png)
Thanks to this part we obtain 2 rectified image (there are some difference due to lack of accuracy in the computation of epipalar lines)
How it works ? 
First we use opencv function called « stereoRectifyUncalibrated() » to obtain the two matrix of homography.
To do so, we need the size of our two input images (here it’s the same size). 
We also input to the function the fundamental matrix and the two lists of good points which allowed us to find the epilines.
Finally, we can use the homography matrix to create our rectified image by passing their as parameters into the openCV function « warpPerspective() ».
![crectified_1](https://user-images.githubusercontent.com/79518374/201161755-97f6259f-16d0-49da-88cb-9ce2b1598698.png)
![crectified_2](https://user-images.githubusercontent.com/79518374/201161765-7292441a-241a-4c71-ac34-715d9ea82412.png)

To observe more easily, the same two blue horizontal lines are drawn on top of the images. 
![rectified_images](https://user-images.githubusercontent.com/79518374/201162367-9c201b12-edf4-4457-8158-f513b5c93e32.png)

Normally we should see the same object lied by the lines  in their respective image. 
Unfortunatelly, here it appears that there is a lack of accuracy in my work. 
I print the mean errors : 
![image](https://user-images.githubusercontent.com/79518374/201162543-4f94fae0-5412-4268-8f7e-5538c99f6049.png)

We have a mean error of -28.5/439 = 0.065 and -21.3/439 = 0.048. 
Even if it’s far lower from the last image it can be too much as with this matrix we compute H1 and H2, which will contain more error, and generate at the end the difference we saw through the two blue lines.
But we can be pretty sure that the averge computing was good because on this last picture we saw epilines aren’t perfectly parallel due to the different angle and position of my camera.

So a good way to check if the computing are all wrong or if it’s just some small error.
We can launch the program computing the epolines on the two rectified images and observe if the epiline are parallel from one picture to the other : 

![image](https://user-images.githubusercontent.com/79518374/201162884-113a1ac5-b6c2-481d-b1ff-54322a658d6d.png)
![image](https://user-images.githubusercontent.com/79518374/201162911-dfa35cb9-2730-491d-ae63-3713fe929fbb.png)
![image](https://user-images.githubusercontent.com/79518374/201162932-b788f22f-62af-479f-b0dd-bb80930f7e9c.png)

It’s a little bit difficult to see if they really are parallel but I my mind it seems to be right.

  3/ Go further --> Generate a disparity map from the rectified images.
  To do so i use the second script named "dmap.py", a short code with two important lines which compute the disparity map.
  
![Screenshot from 2022-11-10 18-21-47](https://user-images.githubusercontent.com/79518374/201163906-7999dfaa-fd51-458d-9a7c-1c4c969cbda3.png)






