# Containerized Flask app on Docker and GCP 

The project demonstrates containerizing a flask application, pushing it to docker hub and subsequently consuming it on Google cloud platform (GCP)

The Container can be downloaded from https://hub.docker.com/repository/docker/akshaypunwatkar/logoclassifier

## Getting Started

The project is a demonstration of a containerized flask application. The application is **Logo Detection** model, which for a given logo image URL, identify the logo brand. The current model is trained using **Flicker 27 logo dataset**, and can only identify the logos of the brands listed below :     
Adidas, Apple, BMW, Citroen, Coca Cola, DHL, FedEx, Ferrari, Ford, Google, Heineken, HP, McDonald's, Mini, NBC, Nike, Pepsi, Porsche, Puma, Red Bull, Sprite, Starbucks, Intel, Texaco, Unicef, Vodafone, and Yahoo.

## Prerequisites

For the execution of the Container, **Docker** is required.    
It could be downloaded from https://www.docker.com/products/docker-desktop

## Guide to use the container

Since the model was trained on annotated images containing only the logo *without* any noise in the picture, the model might not give accurate results for images with noise beside the logos. For best results, use cropped logo images such that the entire image is only of the corresponding logo.     
       
* The application  operates on port 8088.      
* To detect the logo, provide the image url in the format : **localhost:8088/imageurl/<image_path>**



## Links to documentation

> Flask :  https://flask.palletsprojects.com/en/1.1.x/    
> Containers and Docker : https://www.docker.com/resources/what-container.      
> Flickr 27 Logo Dataset : http://image.ntua.gr/iva/datasets/flickr_logos/

# Authors

Akshay Punwatkar

## Acknowledgments

The project was developed under the guidance of Professor Noha Gift (https://noahgift.com) at Duke University. 
