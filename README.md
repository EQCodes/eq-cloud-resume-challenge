<h1>Cloud Resume Challenge</h1>
<h2>Overview</h2>

This is my online AWS hosted cloud resume as part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws) . I used this as a learning project when I joined Skyscanner as a Software Engineer after completing the [Code First Girls Full Stack Degree](https://codefirstgirls.com/courses/cfgdegree/) to develop my understanding of AWS services, Infrastructure as Code and CI/CD.

This version of the repo is a copy of my internal Skyscanner repo, so various CICD files and lines of config have been removed for this public repo.

Screenshots of the web page are below:

![Cloud Resume Website Screenshot](/website-screenshots/Screenshot%202022-10-18%20at%2011.57.55.png)
![Cloud Resume Website Screenshot](/website-screenshots/Screenshot%202022-10-18%20at%2011.58.08.png)
![Cloud Resume Website Screenshot](/website-screenshots/Screenshot%202022-10-18%20at%2011.58.36.png)

I chose to do a slightly altered version of the 'original' Cloud Resume Challenge in order to familiarise myself with Skyscanner tools and Skyscanner AWS accounts. As such, I replaced the suggested AWS SAM with CloudFormation and GitHub Actions with Drone and Slingshot (internal tool) for CI/CD.

The project was created in a Sandbox AWS account. I firstly worked through the steps of the project using the AWS console to familiarise myself with the different services, before then carrying out each step again but using Infrastructure as Code rather than clicking around the Console.

The overall architecture of my site is as follows:

![Diagram of AWS Services](/website-screenshots/Screenshot%202022-11-02%20at%2014.55.33.png)


<h2>Details about technologies used</h2>
    <li><b>HTML/CSS Web Page:</b> the web page was written with simple HTML & CSS.</li>
    <li><b>Amazon S3 Static Website:</b> the website was deployed to an Amazon S3 bucket and deployed as a static website</li>
    <li><b>Amazon CloudFront for HTTPS:</b> the S3 bucket was configured with an Amazon CloudFront Distribution both for high performance delivery of content using edgepoints but also for HTTPS for security.</li>
    <li><b>Amazon Route53 for DNS domain name:</b> a DNS domain name was set up via Amazon Route53 and this points to the CloudFront distribution. I used a Hosted Zone already set up in the Skyscanner Sandbox account, so just added a new record to this Hosted Zone.</li>
    <li><b>Live Visitor Counter using JavaScript with Amazon API Gateway, Lambda and DynamoDB:</b> simple JavaScript code embedded in the HTML file allows the web page to make a call to the API Gateway that triggers a Lambda Function which reads, increments and returns a DynamoDB table value with the number of website visitors. The Lambda function was written using the Python Boto3 library for AWS.</li>
    <li><b>Resource Deployment using IaC via CloudFormation:</b> a CloudFormation template was written and deployed to create a Stack with the required resources: S3 Bucket, S3 Bucket Policy Route53 Record, CloudFront Distribution, & DynamoDB.</li>
    <li><b>Lambda Function & API Gateway deployed using m-shell cut and Slingshot:</b> as per standard approach at Skyscanner, the Lambda function and API Gateway were deployed using a microservices tool called mshell-cut which helped create a lot of the boiler plate requirements for safe and secure deployment.</li>
    <li><b>GitHub, Drone & Slingshot for CI/CD:</b> a standard internal deployment pipeline was used for source control and deployment. Changes to GitHub initiates a Drone build which then triggers internal Skyscanner tool, Slingshot, to deploy those changes in AWS.</li>
</ul>
<br>

<h2>Summary</h2>

Ultimately, this project was incredibly insightful for getting to grips with the basics of cloud & AWS, Infrastructure as Code and safe and secure CI/CD pipelines. For those who are new to this area of work and learn by 'doing', I would really recommend this as a project to get you up to speed with the foundational knowledge required for your role. 
