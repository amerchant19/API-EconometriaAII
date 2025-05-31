# Astronomic Album

Hello There!

Welcome to this repository, where we explore a fun data scraping exercise using the NASA APOD (Astronomy Picture of the Day) API.
The goal is to extract the image (or video) URL for each day over the past 1,000 days, building what we like to call a digital *Astronomic Album*.
 
## What is APD?

The Astronomy Picture of the Day (APD) is a daily feature from NASA that highlights a unique and often stunning view of space or Earth.
These visuals are usually captured with some of the most advanced cameras and powerful telescopes available, making for truly breathtaking imagery.
Alongside images, APD often includes videos that further enrich the experience.

More: [https://apod.nasa.gov/apod/archivepix.html](https://apod.nasa.gov/apod/lib/about_apod.html)

## About this Repo

To get started, you’ll need an API key from NASA. You can request one here: [https://api.nasa.gov](https://api.nasa.gov)

You need to create a file .env where you can save your own API KEY:
NASA_KEY=*yourkey*



The aim of this project is to collect the following data for each of the last 1,000 days:

- **Date** of the picture (`date`)  
- **Title** of the picture (`title`)  
- A brief **description** (`explanation`)  
- The **URL** to the image (JPG) or video (usually YouTube) (`url`)

We’ll use the APOD API, available at:  
`https://api.nasa.gov/planetary/apod`

Once you run the `APD_data_extraction.py` script in the `code/` folder, a CSV file will be generated containing all the collected data.  
You’ll find the final dataset saved as `astronomic_album.csv` in the `data/` folder.


 ## Workflow structure

This repo is structured as follows:

 ```
API-EconometriaAII/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── code/                  
│   └── APD_data_extraction.py        
│
└── data/                  
    └── astronomic_album.csv          
```
## Note

For more about APD API visit https://github.com/nasa/apod-api


## An incredible example

*Analemma over the Callanish Stones*

February 18, 2022

![intro](https://apod.nasa.gov/apod/image/2209/CallanishAnalemma_Petricca_960.jpg)


 
