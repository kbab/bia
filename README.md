# bia
Code for Bioimage Archive Interview task

This repo contains a [Django](https://www.djangoproject.com/) app using the [Django REST framework](https://www.django-rest-framework.org/) for API calls as specified in the Bioimage Archive Interview task. Please note that as it is an informal demo, the app runs in debug mode and is allowed to be hosted on any server.

Until 22/06/2021 there will be a working version of the app online which can be accessed by:
* List of accession IDs - http://94.156.201.94:8000/api/v1/images
* Metadata by accession ID - http://94.156.201.94:8000/api/v1/accessions/BIA-02/metadata
* Imagesize by accession ID - http://94.156.201.94:8000/api/v1/accessions/BIA-03/imagesize

### Four options for running the app locally
The commands below assume use of a Linux terminal and that port 8000 is free on your local machine. The options are listed in the order I believe is most convenient

1. Download the image from dockerhub and run locally - `docker container run -p 8000:8000 -d sprynt001/bia:latest` then browse onto http://localhost:8000/api/v1/images etc
2. Clone/download this repo and use `docker-compose`. Simply navigate to the base directory containing the docker-compose.yml file and run `docker-compose up -d` then browse onto http://localhost:8000/api/v1/images etc
3. Clone/download this repo and use `docker`. Navigate to the base directory containing the `Docker` file and run `docker build . -t bia && docker container run -p 8000:8000 -d bia` then browse onto http://localhost:8000/api/v1/images etc
4. Clone/download this repo and run using python. This requires all the python modules to be installed, so a virtual environment is best. Instructions below use miniconda (https://docs.conda.io/en/latest/)
    1. cd to base directory of repository
    2. `conda create -n bia python=3.8`
    3. `conda activate bia`
    4. `pip install -r requirements.txt`
    5. `python manage.py runserver 8000`
    6. browse onto http://localhost:8000/api/v1/images etc
  
