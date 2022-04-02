# Reddit
  Reddit r/place canvase automation.
  You can use it to draw you logo , picture or any shorts of picture in the reddit r/plce canvase
!["r/reddit image"](https://raw.githubusercontent.com/leyuskckiran1510/Reddit/master/ReadmeImage/redditcanvas.png "r/place")

##How to use
1) Download the file or repo
2) pip install -r ./requi......txt or create virtual environmet if you now what I mean( python venv environment_name)
3) Now open up browser and goto r/place and "Ctrl+Shit+I" to open Dev tab
4) Goto "Network" tab
5) filter out the XHR requests (hold "CTRl" and click on "Fetch/XHR")
6) now click on requests with name "query..."
7) goto "header" sub-tab
8) and scroll down to Requests Headers
9) Copy the authorization token after "Bearer" and paste into redditplaceputter.py's "TOKKEN" variable
10) Now booom You are good to goo run the script in background and it will do it's Task.

# Want's to change the image from Nepal's flag to any other images
Easy! just change the image.jpg file with another image 
# Note the image name must be image.jpg not .jpeg/.png/ .wepb/ .bmp if you want to put other format images you also have to change the file name in the bin.py 
file

# sample of executed code in pycharm you can use any other interpreater
!["r/reddit image"](https://raw.githubusercontent.com/leyuskckiran1510/Reddit/master/ReadmeImage/projectScreenShot.png "r/place")
