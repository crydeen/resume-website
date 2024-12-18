from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    """Render the main page with the interactive resume."""
    return render(request, 'website/home.html')

@csrf_exempt
def timeline_data(request):
    """Endpoint to serve timeline data as JSON."""
    if request.method == 'GET':
        data = {
            "timeline": [
                {
                    "date": "2013",
                    "title": "Computer Science Spark",
                    "description": "First Computer Science Project - Pac-Man",
                    "details": "My project in my high school computer science class sparked my love for computer science. Wrote a working Pac-Man game in Java.",
                    "category":"education",
                    "skills":"java"
                },
                {
                    "date": "2014",
                    "title": "Began College",
                    "description": "Started my undergraduate degree in Computer Science at the University of Mississippi",
                    "details": "I chose the University of Mississippi after touring multiple colleges with my father and falling in love with the campus at Ole Miss. I received a full ride to the university and found great classmates and great professors in the computer science program there. I was a member of the Sally McDonnell Barksdale Honors College and received a special scholarship only awarded to a select group of students belonging to the honors college.",
                    "category":"education"
                },
                {
                    "date": "2015",
                    "title": "First Internship",
                    "description": "Began my first internship at Raising Canes corporate office in Plano, Texas.",
                    "details": "During the internship I rotated through three different programs participating in Networking Design at the corporate office, new restaurant opening IT installations, and finally Help Desk support for any IT related issues at the restaurants.",
                    "category":"work",
                    "skills":"LogMeIn,Cisco Routers,Bose Soundsystem Install,Troubleshooting,Help Desk"
                },
                {
                    "date": "2017",
                    "title": "Second Internship",
                    "description": "Began my second internship, this one at FedEx in Collierville, TN.",
                    "details": "Worked on an intern team consisting of five people and we created two diﬀerent projects during a 10-week program. The first was a groundbreaking big data application that equipped Cloud Ops with greater visibility into their cloud deployment infrastructure. The second was another big data application that utilized Splunk to create visualizations and dashboards of storage performance metrics that is projected to save FedEx $8.78 million over the course of one year. Learned how to eﬀectively work on a team and coordinate a large-scale eﬀort to implement software and practiced public speaking skills in front of full auditoriums of people.",
                    "category":"work",
                    "skills":"Backend,Front-End,React,NodeJS,CSS"
                },
                {
                    "date": "2018",
                    "title": "Defended Honors Thesis",
                    "description": "I successfully defended my Honors College thesis \"Sentiment of the Union\" to a panel of computer science professionals and graduated summa cum laude from the University of Mississippi.",
                    "details": "My honors college thesis was titled \"Sentiment of the Union\" that was focused on natural language processing and the texts analyzed were the presidential State of the Union addresses. These State of the Union addresses were processed using custom tokenization and lexical features to abstract meaning from the content of the addresses. This was utilized to categorize sentiment towards major factors of society including economy, crime, jobs. This data was processed using python and D3.js to create an interactive web interface that facilitated exploration of the data.",
                    "category":"education",
                    "skills":"Python,D3.js,NLTK,Natural Language Processing"
                },
                {
                    "date": "2018",
                    "title": "Graduated from the University of Mississippi",
                    "description": "I graduated summa cum laude from the University of Mississippi with a degree in Computer Science and a minor in Mathematics.",
                    "details": "I graduated from the University of Mississippi Summa Cum Laude with a final undergraduate GPA of 3.97. I received a Taylor Medal, the highest academic honor at the University given only to outstanding seniors, as I had the highest GPA in my major and was one of only of a handful of Computer Science majors to receive the award.",
                    "category":"education",
                    "skills":"Python,D3.js,NLTK,Natural Language Processing,Java,Mobile App Development,Data Science,Database Administration,SQL,Data Visualization,Haskell,Web Development"
                },
                {
                    "date": "2018",
                    "title": "First Job",
                    "description": "I began my career as an Associate Database Administrator at FedEx in Collierville, TN.",
                    "details": "I was offered a full-time position at the conclusion of my internship and accepted the job to begin my career at FedEx. Worked on a team focused on Major Incident Management and Splunk Administration. Troubleshooting and Command Center work focused primarily on production support of Oracle databases with close supervision from a Database Principal. Splunk Administration focused on daily maintenance and upkeep of Splunk as well as automating workflows and features to improve our Splunk Enterprise Implementation.",
                    "category":"work",
                    "skills":"Splunk,Python,Bash Scripting,Oracle,Git,Database Performance Tuning,Major Incident Management"
                },
                {
                    "date": "2019",
                    "title": "Promotion to Software Engineer II",
                    "description": "I achieved my first promotion after working at FedEx for one year, pivoting from database support to a full-time Software Engineering position.",
                    "details": "I was offered a promotion to do software development work on the same team more focused towards supporting the application we had inherited. I worked along with my team to support the FedEx enterprise instance of Splunk. I was the Technical Lead for Splunk Production Build in Google Cloud Platform consisting of a cluster of 250 VMs built and maintained through automated scripts using Ansible and Bash. Developed an automated deployment pipeline to quickly and eﬃciently deploy applications to over 20,000 endpoints. Built resilient, structured code to scale and maintain one of the largest Splunk Clusters ever developed. Single-handedly constructed a crucial Intermediary Forwarding layer to cut down endpoint throughput connections into the Splunk Cluster from 20,000 down to 25 with no drops in data or speed along the route and simplifying the overall firewall structure.",
                    "category":"work",
                    "skills":"Splunk,Python,Bash Scripting,Ansible,Git,Google Cloud Platform(GCP),Data Ingestion Pipelines,Data Engineering"
                },
                {
                    "date": "2020",
                    "title": "Promotion to Site Reliability Engineer",
                    "description": "I achieved my second promotion after working at FedEx for two years, pivoting from software engineering to a site reliability engineering role.",
                    "details": "I was offered a position that was a promotion to site reliability engineering on the same team supporting the FedEx enterprise Splunk instance as it became the enterprise standard tool for log and metric ingestion. I was the Technical Support Lead for Splunk Production Build in Google Cloud Platform consisting of a cluster of hundreds of VMs built and maintained through automated scripts using Ansible and Bash. Developed an automated deployment pipeline to quickly and eﬃciently deploy applications to thousands of endpoints. Built resilient, structured code to scale and maintain one of the largest Splunk Clusters ever developed. Technical Lead responsible for infrastructure management that facilitates hundreds of terabytes of data-ingest a day. Developed high-level dashboards allowing for executive insight into data consumption and utilization.",
                    "category":"work",
                    "skills":"Splunk,Python,Bash Scripting,Ansible,Git,Google Cloud Platform(GCP),Data Ingestion Pipelines,Data Engineering"
                },
                {
                    "date": "2022",
                    "title": "Promotion to Senior Site Reliability Engineer",
                    "description": "I achieved my third promotion after working at FedEx for four years, expanding upon my role as a site reliability engineer to a Senior Site Reliability Engineer.",
                    "details": "I was offered a position that was a promotion to senior site reliability engineering on the same team supporting the FedEx enterprise Splunk instance as it became the enterprise standard tool for log and metric ingestion. I am the Technical Support Lead for Splunk SaaS supporting an enterprise environment ingesting over 200 terabytes of data daily. Primary technical lead for migrating from an on-prem environment of over 250 servers to a SaaS solution supported by Splunk Cloud. Taken the lead on multiple special projects associated with the platform in instrumenting network connectivity through an interconnect in the LAS CoLo Data Center. Migrated and managed the role-based access control for the Splunk platform and was a key interface with the Cloud Security Team to implement secure searching in the platform. Assisted in configuring Splunk Mobile App and migrating it through test levels to enable eﬀective mobile device usage with Splunk dashboards. Responsible for maintaining and upkeeping the data ingestion pipelines for logs and metrics into the enterprise data platform.",
                    "category":"work",
                    "skills":"Splunk,Python,Bash Scripting,Ansible,Git,Google Cloud Platform(GCP),Data Ingestion Pipelines,Data Engineering"
                },
                {
                    "date": "2023",
                    "title": "Began Masters Degree",
                    "description": "I began my masters degree in Computer Science at the University of Texas at Austin",
                    "details": "In order to further my education I began my masters degree in August 2023 to challenge myself and gain skills as a computer scientist. The coursework has been challenging and fulfilling and the program has been very enjoyable so far. The program has a heavy focus on Machine Learning and Data Science while also emphasizing the core tenets of computer science to form the foundation of a strong program. Est. completion date: Dec 2026.",
                    "category":"education",
                    "skills":"Python,PyTorch,Java,Kotlin,Sklearn,NLTK,Natural Language Processing,Deep Learning,Neural Networks,Data Science,Data Visualization,Machine Learning"
                }
            ]
        }
        return JsonResponse(data)