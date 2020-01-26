## Note on this respository
This repository contains all of the source code from all of our other repositories. Due to the size of the frontend's NODE_MODULES folder, that folder has been excluded. Please see the frontend's dedicated repository to compile it.

Frontend repo: https://github.com/Lihael/water-you-using
Backend repo: https://gitlab.com/TechyMitch1/water-you-using-backend


## What it does
Our platform provides users with the ability to precisely and effectively analyze their water consumption trends over time. Water You Using uses a network of custom-programmed water sensors that can be integrated directly into a building's water conduits to accurately measure the water usage of any of its faucets, showers, toilets, and other fixtures over time. Through our robust web application, users can learn more about which of their fixtures use the most water and when their peak water-usage times are - two very useful resources in determining how to save water.


## How we built it
We split the development process into three distinct sub-processes: backend, frontend, and hardware.

The backend was built in Python using Flask to handle all HTTP requests, and it serves as the backbone of the web app where all user-data is saved and all raw information is generated for use by the client and hardware components.

The frontend was built in ReactJS, and it processes the data provided by the backend into a format that users can easily understand.

The hardware component of our platform consists of a water sensor assembly that calculates the amount of water utilized during any given period of time from a specific device using a custom formula based on the flow time and the readings from our moisture sensor.


## Challenges we ran into
Among all four of us, the biggest issue we faced was communicating our ideas on how we would be transferring and representing our data between the client, server, and hardware. After (several) hours of refactoring, however, we were able to resolve these issues and successfully combine all of the components of our project.

Mitchell: "The biggest challenge I faced when developing the backend was working around Python's syntax. Since this was my first time developing a full backend infrastructure in Python rather than using the Java-based backend stacks that I'm more familiar with, I had to spend a lot of time the first night just working around dynamic typing and Pythons odd syntactic restrictions. Once I worked around that, though, I was able to finish the backend pretty quickly, which allowed me to help out more with some of the issues the frontend team ran into."

Sabrina: "My biggest challenge during this project was learning how to create a react app. I have never work with a front-end language before or had developed a web application. It was a rough first five hours, but I eventually learned and was able to format and create graphs, buttons, along other things. I really enjoyed the process and coming out of this experience, I feel much more comfortable with front-end programming."



## Accomplishments that we're proud of
Above all else, we're extremely proud of the fact that we were actually able to build a finished and functional product that could potentially have a positive effect on the environment (and users' wallets) with so many moving parts in such a short amount of time. We're also proud of the fact that we all branched out and learned much more about various different development platforms and workflows outside of our comfort zones.


## What we learned
All of us had to learn something new for this project to be successful. For the frontend, we had to spend an ungodly amount of time figuring out how to get our animations to work properly with React, but we all learned more about designing effective user interfaces in the process. The backend's development process was incredibly useful too since it taught us more about Python and how to properly configure servers with Flask. The most important things we learned from the hardware development process were how to interface with Bluetooth devices in low-energy mode and properly preventing leaks in our measurement system.


## What's next for Water You Using?
Water You Using would be a great platform for water companies to offer as an incentive for their customers. Since it provides meaningful information to customers that can make water usage monitoring much easier, it could easily be used to allow customers to save money by using less water, which would in-turn make water companies appear more favorably. Most importantly, though, it can help save resources, which would benefit all of us.