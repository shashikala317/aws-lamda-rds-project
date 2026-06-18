# AWS Lambda + RDS MySQL Project

## Architecture

API Gateway → Lambda → RDS MySQL

## Services Used

* AWS Lambda-create function
* Amazon RDS MySQL-create database
* API Gateway
* IAM-attach policies
* VPC-connect to RDS
* Security Groups

## Project Description

This project retrieves student data from an Amazon RDS MySQL database using AWS Lambda and exposes it through API Gateway.

## Database Table

students

Columns:

* id
* name
* course
* created_at

## Sample Response

{
"students": [
{
"id": 1,
"name": "Shashi",
"course": "AWS"
}
]
}

