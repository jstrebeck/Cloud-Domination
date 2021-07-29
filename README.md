# Cloud-Domination
This project is to demonstrate which cloud platform is dominant per state.


The first question many new cloud engineers ask is what cloud platform should I learn from the big three? The most common answer to this question that I have found is to study the platform that has the most job postings in your area. 

The next step in your journey to becoming a cloud engineer is to deploy some personal projects in the cloud to earn some experience. That’s when I decided to pull all cloud job postings into one place to truly see which cloud platform is dominant.

##The following is my infrastructure design for this project. 

![Cloud Diagram](https://raw.githubusercontent.com/jstrebeck/Cloud-Domination/main/Cloud%20Domination%20Diagram.png)

1. The first step will be to gather job listings from a popular job site. Indeed was chosen since it had an easy-to-use API. Unfortunately, after two months I am still on the waiting list to get access to their API. I took this opportunity to learn more about web scraping with Python. I created a function using the requests library for HTTP requests. The scraper iterates over jobs postings for all 50 states and for all three of the major cloud providers. Once that data is pulled in it used parsed using Beautiful Soup. This function could then be deployed to AWS Lambda and a schedule can be created to regularly run this function and in turn, update our data. Now that we have our information it needs to be uploaded to a database.


1. DynamoDB was chosen as the database for Cloud Domination. States were used as the PK for our states table. Three additional columns were created to represent the job postings for each provider. Using a serverless offering greatly reduced the time it normally takes to deploy and troubleshoot a database server and connect it to your application.
