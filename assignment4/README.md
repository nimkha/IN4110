# Mandatory Assignment 4

### Intro

In this assignment we are making a python program for blurring images using different libraries to 
compare efficiency.<br/>
We are going to take in an image, run it through different implementation of blurring and optionally storing the blurred version.
We also store the time spent on the different implementations<br/>
I was unfortunately not able to complete all he parts of the assignment.

### 1 Python implementation

This version of the implementation uses plain python.<br/>
Run time with this implementation was in my testing about 7.7s <br/>

To run the program use the added blur script.<br/>
First make the blur.py file executable: chmod +x blur.py<br/>
Then run: python blur.py 1 "beatles.jpg" "blurred_beatles.jpg"<br/>
The last argument is optional<br/> 

### 2 Numpy implementation

This version of the implementation uses numpy.<br/>
In my testing the run time went from about 7.7s to 0.3s <br/>

To run the program use the added blur script.<br/>
First make the blur.py file executable: chmod +x blur.py<br/>
Then run: python blur.py 2 "beatles.jpg" "blurred_beatles.jpg"<br/>
The last argument is optional<br/>

### 3 Numba implementation

This version of the implementation uses numba.<br/>
With numba the run time actually went up. from about 7.7s to 8.5 this must be retested after troubleshooting<br/>

This implementation did not work as intended. It is not possible to run with python command.<br/>
Running from IDE(Intellij) would finnish the process though with warnings.<br/>
![](troubleshoot_blur_3_top.png)<br/>

![](troubleshoot_blur_3_bottom.png)<br/>

I did not have more time to troubleshoot this

### 4 Cython implementation

This version of the implementation uses cython.<br/>
With cython run time went from about 7.7s to 5.3s <br/>

There are two ways to run this script:<br/>

1 To run the program use the added blur script.<br/>
First make the blur.py file executable: chmod +x blur.py<br/>
Then run: python blur.py 2 "beatles.jpg" "blurred_beatles.jpg"<br/>
The last argument is optional<br/>

2 Use interactive python.<br/>
first run ipython<br/>
then import blur_4: import blur_4<br/>
then run: blur_4.run("beatles.jpg")

### 5 User interface
For this task we are making a simple command line interface using argparse.<br/>
Usage: python blur.py method_type source destination<br/>
method type = which blur script to use. 1 = blur_1 2 = blur_2 ... <br/>
source = full image name with suffix <br/>
destination (optional) = image name for blurred version
