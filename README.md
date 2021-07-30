# Cloud-Domination
This project is to demonstrate which cloud platform is dominant per state.
To see which provider is dominate in your sate check out [clouddomination.net](https://clouddomination.net)


The first question many new cloud engineers ask is what cloud platform should I learn from the big three? The most common answer to this question that I have found is to study the platform that has the most job postings in your area. 

The next step in your journey to becoming a cloud engineer is to deploy some personal projects in the cloud to earn some experience. That’s when I decided to pull all cloud job postings into one place to truly see which cloud platform is dominant.

As I was working through this project it became very apparent that my Idea had some flaws that I will discuss later. However, my goal for this project was just to give me a custom application where I can hone my cloud skills.

## The following is my infrastructure design for this project. 

![Cloud Diagram](https://raw.githubusercontent.com/jstrebeck/Cloud-Domination/main/Cloud%20Domination%20Diagram.png)

1. The first step will be to gather job listings from a popular job site. Indeed was chosen since it had an easy-to-use API. Unfortunately, after two months I am still on the waiting list to get access to their API. I took this opportunity to learn more about web scraping with Python. I created a function using the requests library for HTTP requests. The scraper iterates over jobs postings for all 50 states and for all three of the major cloud providers. Once that data is pulled in it is parsed using Beautiful Soup. This function could then be deployed to AWS Lambda and a schedule can be created to regularly run this function and in turn, update our data. Now that we have our information it needs to be uploaded to a database. In the future, I would like to revisit this project to use their API to pull this data instead.


1. DynamoDB was chosen as the database for Cloud Domination. States were used as the PK for our states table. Three additional columns were created to represent the job postings for each provider being AWS, Azure, and GCP. Using a serverless offering greatly reduced the time it normally takes me to deploy and troubleshoot a database server and connect it to your application. This option was also extremely easy to connect to our Lambda function by just creating a role with access to both services. At this stage in the process we got our first look at job postings for all 50 states in one place, it became very apparent which cloud provider had the most job postings.

1. Now that we had a database populated with our data we need an easy way to visualize it. My goal was to create a web app that highlights each state with whichever provider is dominant according to job postings on Indeed. Google provides their [Maps API](https://developers.google.com/maps/gmp-get-started) which is configured with javascript. The one downside to this solution is they don’t have a built-in way to select states at this time. A workaround is to draw shapes using Longitude and Lattitude coordinates to draw out each state which is stored in the States.js file. Another Javascript function is created to pull the provider listings by state, determine which provider has the greatest value, and assign that state to the color which matches their provider where AWS is orange, Azure is blue, and GCP is yellow. This webpage is hosted on an EC2 t2.micro Ubuntu using Ngnix as the webserver.


1.  Our Elastic Load Balancer simply handles requests and has our one EC2 instance in the target group. In the future, I would like to create a scaling group to dynamically add more EC2 targets to balance across.


1.  CloudFront is used as our CDN for our webpage to cache the data at all of Amazon’s endpoints. Since our website is used to display timely data our cached information will be invalidated every time our database is updated which is completed with our serverless function. This is where our clients will terminate to view and browse Cloud Domination.
  1.AWS Certificate Manager provides an SSL cert and ties into our domain name of clouddomination.net
