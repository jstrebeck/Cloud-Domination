#!/usr/bin/env python3
import boto3
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time

def get_url(position, location):
    tempalte = 'https://www.indeed.com/jobs?q={}&l={}'
    url = tempalte.format(position, location)
    return url

def CloudJobs_put(state, provider, num_jobs, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('CloudJobs')
    response = table.update_item(
        Key={
            'state': state,
        },
        UpdateExpression="set " + provider +"=:p",
        ExpressionAttributeValues={
            ':p': num_jobs,
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

providers = ['AWS', 'Azure', 'GCP']

def cloud_jobs(state):
    for provider in providers:
        url = get_url(provider, state)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            results = soup.find('div', id = 'searchCountPages').text.split()[3]
            CloudJobs_put(state, provider, results)
            print('Put ' + str(results) + ' ' + provider + ' jobs in ' + state + ' state')
        except Exception as e:
            print(str(e) + ' for ' + state + ' state')
            quit()

def jobsperstate():        
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 
    'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 
    'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
    'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 
    'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 
    'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    for state in states:
        cloud_jobs(state)


def lambda_handler(event, context):
    jobsperstate()
    return {
        'statusCode': 200,
    }