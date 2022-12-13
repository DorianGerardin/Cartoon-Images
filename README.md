# Cartoon-Images
An image processing project for images cartoonization

Available at http://imagecartoonizer.pythonanywhere.com/ 

![Cartoon Poster](Poster_Cartoon.png)

## Traditional Image Processing Method

#### 1.  Here are few examples of image quantization using K-means algorithm on different images :

* **Drake's face :**

Image to process           |           K = 5           |            K = 9          | K = 12 | K = 15 | K = 19 | Best Image (K = 7)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![drake's face](images/quantization/face_drake/face_drake.png)   | ![drake's face (k=5)](images/quantization/face_drake/face_drake_k5.png)| ![drake's face (k=9)](images/quantization/face_drake/face_drake_k9.png) | ![drake's face (k=12)](images/quantization/face_drake/face_drake_k12.png) | ![drake's face (k=15)](images/quantization/face_drake/face_drake_k15.png) | ![drake's face (k=19)](images/quantization/face_drake/face_drake_k19.png) | ![drake's face (k=7)](images/quantization/face_drake/face_drake_k7.png)

<br>

* **Japan landscape :**

Image to process           |           K = 5           |            K = 9          | K = 12 | K = 15 | K = 19 | Best Image (K = 9)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![japan landscape](images/quantization/japan_landscape/japan_landscape.png)   | ![japan landscape (k=5)](images/quantization/japan_landscape/japan_landscape_k5.png)| ![japan landscape (k=9)](images/quantization/japan_landscape/japan_landscape_k9.png) | ![japan landscape (k=12)](images/quantization/japan_landscape/japan_landscape_k12.png) | ![japan landscape (k=15)](images/quantization/japan_landscape/japan_landscape_k15.png) | ![japan landscape (k=19)](images/quantization/japan_landscape/japan_landscape_k19.png) | ![japan landscape (k=9)](images/quantization/japan_landscape/japan_landscape_k9.png)

<br>

* **A burger :**

Image to process           |           K = 5           |            K = 9          | K = 12 | K = 15 | K = 19 | Best Image (K = 15)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![burger](images/quantization/burger/burger.png)   | ![burger (k=5)](images/quantization/burger/burger_k5.png)| ![burger (k=9)](images/quantization/burger/burger_k9.png) | ![burger (k=12)](images/quantization/burger/burger_k12.png) | ![burger (k=15)](images/quantization/burger/burger_k15.png) | ![burger (k=19)](images/quantization/burger/burger_k19.png) | ![burger (k=15)](images/quantization/burger/burger_k15.png)

<br>

* **Taylor Swift's face :**

Image to process           |           K = 5           |            K = 9          | K = 12 | K = 15 | K = 19 | Best Image (K = 19)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![Taylor Swift's face](images/quantization/face_taylor/face_taylor.png)  | ![Taylor Swift's face (k=5)](images/quantization/face_taylor/face_taylor_k5.png)| ![Taylor Swift's face (k=9)](images/quantization/face_taylor/face_taylor_k9.png) | ![Taylor Swift's face (k=12)](images/quantization/face_taylor/face_taylor_k12.png) | ![Taylor Swift's face (k=15)](images/quantization/face_taylor/face_taylor_k15.png) | ![Taylor Swift's face (k=19)](images/quantization/face_taylor/face_taylor_k19.png) | ![Taylor Swift's face (k=19)](images/quantization/face_taylor/face_taylor_k19.png)

#### 2.  Here are few examples of edge enhancement on quantized images :


* **Drake's face :**

Image to process           |           line size = 5           |           line size = 7          | line size = 9 | line size = 11 | Best Image (line size = 9)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![drake's face](images/quantization/face_drake/face_drake_k7.png)   | ![drake's face (ls=5)](images/edges/face_drake/face_drake_ls5.png)| ![drake's face (ls=9)](images/edges/face_drake/face_drake_ls7.png) | ![drake's face (ls=7)](images/edges/face_drake/face_drake_ls9.png) | ![drake's face (ls=11)](images/edges/face_drake/face_drake_ls11.png) | ![drake's face (ls=9)](images/edges/face_drake/face_drake_ls9.png) 

<br>

* **Japan landscape :**

Image to process           |           line size = 5           |           line size = 7          | line size = 9 | line size = 11 | Best Image (line size = 5)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![japan landscape](images/quantization/japan_landscape/japan_landscape_k9.png)   | ![japan landscape (ls=5)](images/edges/japan_landscape/jap_ls5.png)| ![japan landscape (ls=9)](images/edges/japan_landscape/jap_ls7.png) | ![japan landscape (ls=7)](images/edges/japan_landscape/jap_ls9.png) | ![japan landscape (ls=11)](images/edges/japan_landscape/jap_ls11.png) | ![japan landscape (ls=5)](images/edges/japan_landscape/jap_ls5.png) 

<br>

* **A burger :**
 
Image to process           |           line size = 5           |           line size = 7          | line size = 9 | line size = 11 | Best Image (line size = 11)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![burger](images/quantization/burger/burger_k15.png)   | ![burger (ls=5)](images/edges/burger/burger_ls5.png)| ![burger (ls=9)](images/edges/burger/burger_ls7.png) | ![burger (ls=7)](images/edges/burger/burger_ls9.png) | ![burger (ls=11)](images/edges/burger/burger_ls11.png) | ![burger (ls=11)](images/edges/burger/burger_ls11.png) 

<br>

* **Taylor Swift's face :**

Image to process           |           line size = 5           |           line size = 7          | line size = 9 | line size = 11 | Best Image (line size = 9)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![Taylor Swift's face](images/quantization/face_taylor/face_taylor_k19.png)   | ![Taylor Swift's face (ls=5)](images/edges/face_taylor/ts_ls5.png)| ![Taylor Swift's face (ls=9)](images/edges/face_taylor/ts_ls7.png) | ![Taylor Swift's face (ls=7)](images/edges/face_taylor/ts_ls9.png) | ![Taylor Swift's face (ls=11)](images/edges/face_taylor/ts_ls11.png) | ![Taylor Swift's face (ls=9)](images/edges/face_taylor/ts_ls9.png) 

#### 2.  Here are few examples of image cartoonization using White Box Algorithm :

* **Drake's face :**

Image to process           |           Cartoonized Image       
:-------------------------:|:-------------------------:|
![drake's face](images/quantization/face_drake/face_drake.png)   | ![drake's face cartoonized](images/WhiteBox%20Cartoon/drake.png)

<br>

* **Taylor Swift's face :**

Image to process           |           Cartoonized Image             
:-------------------------:|:-------------------------:|
![Taylor Swift's face](images/quantization/face_taylor/face_taylor.png)   | ![Taylor Swift's face cartoonized](images/WhiteBox%20Cartoon/TS.jpeg)

<br>

* **A burger :**

Image to process           |           Cartoonized Image              
:-------------------------:|:-------------------------:|
![Burger](images/quantization/burger/burger.png)   | ![Burger cartoonized](images/WhiteBox%20Cartoon/burger.png)

<br>

* **A Japan landscape :**

Image to process           |           Cartoonized Image              
:-------------------------:|:-------------------------:|
![Japan landscape](images/quantization/japan_landscape/japan_landscape.png)   | ![Japan landscape cartoonized](images/WhiteBox%20Cartoon/jap.jpeg)

#### 3.  Comparison between the two methods

* **Drake's face :**

Image to process           |           Traditional method   | Deep Learning method  
:-------------------------:|:-------------------------:|:-------------------------:|
![Drake's face](images/quantization/face_drake/face_drake.png)   | ![Drake's face cartoonized](images/edges/face_drake/face_drake_ls9.png) | ![drake's face cartoonized](images/WhiteBox%20Cartoon/drake.png)

<br>

* **Taylor Swift's face :**

Image to process           |           Traditional method   | Deep Learning method    
:-------------------------:|:-------------------------:|:-------------------------:|
![Taylor Swift's face](images/quantization/face_taylor/face_taylor.png)   | ![Taylor Swift's face cartoonized](images/edges/face_taylor/ts_ls9.png) | ![Taylor Swift's face cartoonized](images/WhiteBox%20Cartoon/TS.jpeg)

<br>

* **A burger :**

Image to process           |           Traditional method   | Deep Learning method      
:-------------------------:|:-------------------------:|:-------------------------:|
![Burger](images/quantization/burger/burger.png)   | ![Burger cartoonized](images/edges/burger/burger_ls11.png) | ![Burger cartoonized](images/WhiteBox%20Cartoon/burger.png)

<br>

* **A Japan landscape :**

Image to process           |           Traditional method   | Deep Learning method      
:-------------------------:|:-------------------------:|:-------------------------:|
![Japan landscape](images/quantization/japan_landscape/japan_landscape.png)   | ![Japan landscape cartoonized](images/edges/japan_landscape/jap_ls5.png) | ![Japan landscape cartoonized](images/WhiteBox%20Cartoon/jap.jpeg)
