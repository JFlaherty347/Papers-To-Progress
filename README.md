# Papers-To-Progress

### What is this Repository?
This repository holds an excerpt of code written by me as a part of a project [I worked on at Stanford's Health++ 2019 Hackathon](https://healthplusplus19.devpost.com/?ref_content=default&ref_feature=challenge&ref_medium=discover).
The code presented here is a computer vision algorithm that takes an image of a paper as input, and corrects the image so it can
be more easily read and categorized by the google cloud's OCR.

### What is Papers to Progress?
Papers to progress is a medical record digitalization pipeline that allows for data insights into the healthcare in devloping
countries. Papers to Progress is designed to be low cost and easy to implement so that rural hospitals are able to implement it.
Developing countries surprisingly have a large number of smarttphone ussers, however electricity and network connection isn't 
consistent enough to allow for a desktop computer to be used reliably. With Papers to Progress, all a hospital would need is to
take a picture of each record before filing it away, and then to upload them to our google cloud server the next time they have
an internet connection. Papers to Progress is not aiming to completely digitize medical records in developing countries because it
is not viable where electricity and network connections are inconsistent. Instead, Papers to Progress is providing a data pipeline
to allow hospitals to stay with their current paper record system while also generating data about their care. Instead of these
records being filed away where they will most likely not be seen again, their anonymized data is made available to researchers
and lawmakers. 

![image of data pipeline] ()

### How does Papers to Progress Help?
Our project was inspired by the stories of the medical professionals our team met at Health++. They told us of a time where they
had hired people to manually enter medical records into a database for several hours and how it helped them create a more
benefitial health initiative in a developing country. We sought to scale this idea to a larger scale and automate the process.
Once hospitals begin using Papers to Progress, researcher could use the data they generate to determine the best way to improve
the healthcare in that hospital, county, or country. Now, instead of blindly pouring money into improving healthcare and hoping
it makes a difference, developing countries can make informed decisions on what improvements will have the biggest impact.

### Why is Papers to Progress different?
After discussing the problem with an expert who has dealt with this issue first hand, we learned that the biggest issue with
previous attempts to solve this problem were the difficulty of implementing the system in a rural hospital, messy data, and
the demanding requirements of processing the data. To address the difficulty of the problem, we designed a workflow where a
template is setup for a given record, marking each field with a title. Once this template is setup, all that is needed is to snap
a picture of each new record as it is created on a smartphone, and the data is neatly organized to be used. These low costs and
ease of use allow the software to be implemented into the workflow of any hospital that would benefit from these data insights.
The template usage also ensures cleaner data because the fields are defined once at the beginning by the user to make each
category usable. With perfect data categories, data is more easily combined and managed by researchers, allowing insights to be 
made on a larger scale. Furthermore, many steps are taken afterwards using google cloud services to filter and clean the data.
Finally, we addressed the computing requirements by creating a pipeline that required the user to only take and upload photos,
while saving the machine learning for the cloud.

### What was achieved at the event?
At this event we developed a proof of concept that involved the image preparation and OCR stages of the data pipeline. If granted
more time, we would have implemented our planned data cleaning processes and improved the user interface. We primarily focused
on perfecting the data pipeline design and implementing the back-end carefully. Ultimately, the event was an amazing learning
experience which all of the Papers to Progress team values.