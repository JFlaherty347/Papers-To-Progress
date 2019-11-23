# Papers-To-Progress

### What is this Repository?
This repository holds an excerpt of code written by me as a part of a project [I worked on at Stanford's Health++ 2019 Hackathon](https://healthplusplus19.devpost.com/?ref_content=default&ref_feature=challenge&ref_medium=discover).
The code presented here is a computer vision algorithm that takes an image of a paper as input and corrects the image so it can
be more easily read and categorized by the google cloud's OCR. Please note that this repository was created after the event
for the purpose of presenting the code specifically written by me and as a result, it only has improvements made after the event. Please keep in mind that the event was only 24 hours long during which our group not only had to produce a proof of concept but 
also a business plan for implementing our global health solution.

### What is Papers to Progress?
Papers to progress is a medical record digitalization pipeline that allows for data insights into healthcare in developing
countries. Papers to Progress is designed to be low cost and easy to implement so that rural hospitals are able to implement it.
Developing countries surprisingly have a large number of smartphone users, however, electricity and network connection isn't 
consistent enough to allow for a desktop computer to be used reliably. With Papers to Progress, all a hospital would need is to
take a picture of each record before filing it away, and then to upload them to our google cloud server the next time they have
an internet connection. Papers to Progress is not aiming to completely digitize medical records in developing countries because it
is not viable where electricity and network connections are inconsistent. Instead, Papers to Progress is providing a data pipeline
to allow hospitals to stay with their current paper record system while also generating data about their care. Instead of these
records being filed away where they will most likely not be seen again, their anonymized data is made available to researchers
and lawmakers. 

![image of data pipeline](https://github.com/JFlaherty347/Papers-To-Progress/blob/master/Images/DataCollectionStages.png)

### How does the Code in this Repository Prepare the Photo for OCR?
This code utilizes the OpenCV library for python to find and apply a [homography](https://en.wikipedia.org/wiki/Homography_(computer_vision)) to the users' input image in
comparison to the template image. This code uses [ORB](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_orb/py_orb.html) in order to find matching points between the input and the template 
images. The reference points that orbs find may look something like the following example:

<img src="https://github.com/JFlaherty347/Papers-To-Progress/blob/master/Output/matches.jpg" alt="Reference Point Image" width="1000">

In this example, a printed form was created with handwriting on it and is about to be added to the database. The left image  is the new form to be added to the database and the image on the right is the template for that form. The colored circles show
reference points that ORB has found between the two images. For each circle, there is a corresponding circle on the other image,
connected by a line. These are used to find a homography which is then used to warp the perspective of the image.

After the image is warped, there will likely be unnecessary visual noise leftover past the paper since the transformation was
done exclusively with respect to the paper. To fix this, [all contours in the image](https://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html) are found are sorted by size.
The biggest contour is assumed to be the page, as if there were a contour larger than the page in the image, the existing part of
the image with the actual form on it is likely to small to be accurately handled by OCR anyways. Now that the paper has been
found, the image is cropped to the size of the paper which can then be lined up with the fields set for the template of the form.
Here is the result of the above image after being transformed and cropped:

<img src="https://github.com/JFlaherty347/Papers-To-Progress/blob/master/Output/Aligned.jpg" alt="Result image" width="400">

Now, the image of the completed form has been transformed to match the template, but it still contains all of the writing from
the completed form. This in effect has allowed any picture of the form to be used with Papers to Progress without having to 
take a perfectly aligned image. As a result, the ease of use is increased and requires the end-user to only know how to snap
a picture on their smartphone.

### How does Papers to Progress Help?
Our project was inspired by the stories of the medical professionals our team met at Health++. They told us of a time where they
had hired people to manually enter medical records into a database for several hours and how it helped them create a more
beneficial health initiative in a developing country. We sought to scale this idea to a larger scale and automate the process.
Once hospitals begin using Papers to Progress, researchers could use the data they generate to determine the best way to improve
healthcare in that hospital, county, or country. Now, instead of blindly pouring money into improving healthcare and hoping
it makes a difference, developing countries can make informed decisions on what improvements will have the biggest impact.

### Why is Papers to Progress different?
After discussing the problem with an expert who has dealt with this issue first hand, we learned that the biggest problems with
previous attempts to solve this problem were the difficulty of implementing the system in a rural hospital, messy data, and
the demanding requirements of processing the data. To address the difficulty of the problem, we designed a workflow where a
template is setup for a given record, marking each field with a title. Once this template is configured, all that is needed is to 
snap a picture of each new record as it is created on a smartphone, and the data is neatly organized to be used. These low costs 
and ease of use allow the software to be implemented into the workflow of any hospital that would benefit from these data 
insights. The template usage also ensures cleaner data because the fields are defined once at the beginning by the user to make 
each category usable. With perfect data categories, data is more easily combined and managed by researchers, allowing insights to 
be made on a larger scale. Furthermore, many steps are taken afterward using google cloud services to filter and clean the data.
Finally, we addressed the computing requirements by creating a pipeline that required the user to only take and upload photos,
while saving the machine learning for the cloud.

### What was achieved at the event?
At this event, we developed a proof of concept that involved the image preparation and OCR stages of the data pipeline. If granted more time, we would have implemented our planned data cleaning processes and improved the user interface. We primarily focused on perfecting the data pipeline design and implementing the back-end carefully. Ultimately, the event was an amazing learning experience which all of the Papers to Progress team values.
