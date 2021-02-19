# Spam detection in e-mails

![spam](https://user-images.githubusercontent.com/57860857/107559135-f8bbd000-6bdb-11eb-935d-50411086bf89.jpg)

## Introduction

This project is a simple implementation of spam detection model for e-mails.

## The dataset

The data used for training the model is available [here](https://www.kaggle.com/venky73/spam-mails-dataset).

## The workflow

The complete workflow can be seen in the `workflow.ipynb`.

## Running the model

I used flask package, as well as Dockerfile to deploy the application. To run it, you can clone this repository onto your computer. Then, in the directory, run the following command (with Docker runnung): `docker build . -t spam_detection`. When the container is created, you can simply type `flask run`. Then, the application will be available under the following adress: `http://127.0.0.1:5000/`.
