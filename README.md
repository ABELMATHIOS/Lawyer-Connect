N, [2/21/2025 11:45 PM]
<h1 align="center">LAWYER WEBSITE</h1>

## Overview
This repository contains the code and program for a fully functional lawyer website. Designed by BITS College students with modern web development technologies.  
The website is user-friendly, ensuring responsiveness, accessibility, and much more. It is tailored for lawyers to manage their agendas, monitor contact information, and promote themselves effectively. For clients, the site is easy to use, understand, and access. They can book appointments, pay fees, and much more.

Overall, this repository provides the source code for a professional lawyer website, created to showcase the services, team, and legal expertise of a law firm. It’s fully responsive, offering a seamless experience across most devices. The website provides essential information for potential clients, such as service offerings, team member profiles, contact details, and legal services.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Technologies Used](#technologies-used)
   - [Frontend](#frontend)
   - [Backend](#backend)
   - [Database](#database)
   - [Other Technologies](#other-technologies)
4. [Features](#features)
   - [Lawyer Features](#lawyer-features)
   - [Client Features](#client-features)
5. [FolderStructure](#folderstructure)
6. [Commonissues](#commonissues)
7. [Contactinfo](#contactinformation)
8. [Acknowledgement](#acknowledgement)
9. [Contributers](#contributers)
---

## 1. Installation
<a id="installation"></a>
Follow these steps to set up the Lawyer Connect project on your local machine.

### 1.1. Prerequisites
Before you begin, ensure you have the following software installed on your computer:
- Python 3.x or higher
- Git (for cloning the repository)
- pip (Python package manager)

### 1.2. Steps to Install

1. Clone the Repository  
   Clone the repository to your local machine using the following command:
   git clone https://github.com/ABELMATHIOS/Lawyer-Connect.git 

2. Navigate to the Project Directory
   Change your current directory to the project folder:
   cd Lawyer-Connect

3. Create a Virtual Environment
create a virtual environment for the project to avoid conflicts with other Python projects:
   python -m venv venv 
   
4. Activate Virtual environment

    A. windows
   venv\Scripts\activate
   B. macos/linux
   source venv/bin/activate

5. Install dependencies
   pip install -r requirements.txt

6. configure environment
   FLASK_APP=app.py
   SECRET_KEY=your_secret_key
   PAYPAL_CLIENT_ID=your_paypal_client_id

7. run the application
   flask run
8. testing
   pytest
...

## 2. Usage
<a id="usage"></a>
The website will display the homepage, where you can explore features like booking appointments, checking out attorney profiles, and paying fees. Depending on the user role (lawyer or client), the available features will differ.
Available Routes

About us
Route: /about
Access the login page to authenticate users.
Register Page

List of Available Lawyers
Route: /attorneys
New users can register an account here.
Add User

Latest news route
Route: /news
Admins can add new users to the system.
Add Team

Contact us 
Route: /contact
Admins can add new members to the legal team.


Lawyers Details
Route: /attorneys_single
Clients can book a meeting with a lawyer.

Users Registrations
Route: /user-r
View all scheduled meetings.

Lawyers Registrations
Route: /lawyer-r
View all scheduled meetings.

Login Page for Users
Route: /login-u
User login route


Login Page for Lawyers
Route: /login-l
Lawyers can login in if registered

Log out
Route: /logout-u
Log out of the current session.

Users Dashboard
Route: /dashboard-u
Users dashboard.

Lawyer Dashboard
Route: /dashboard-l
Lawyers dashboard.

Admin route
Route: /admin
Only accessable to admins.

Payment Options
The app integrates with PayPal and Stripe for online payments. Once a meeting is scheduled, clients can make payments via these methods.

PayPal: Clients can use their PayPal account or card to pay for a meeting.
Stripe: A secure way to pay using a credit/debit card.
...

## 3. Technologies Used
<a id="technologies-used"></a>

### 3.1. Frontend
<a id="frontend"></a>
HTML/CSS: The website's structure and styling are built using HTML5 and CSS ensuring responsiveness across various devices

JavaScript: Used for dynamic interactions, including forms, appointment bookings, and integrating features like the Owl Carousel for testimonials

N, [2/21/2025 11:45 PM]
### 3.1.1. Backend
<a id="backend"></a>
The backend is powered by Python, specifically using the Flask web framework. Flask provides a simple yet powerful way to handle routes, user authentication, meeting scheduling, and integration with payment gateways like PayPal and Stripe.

### 3.2.2. Database
<a id="database"></a>
For this project, SQLite is used as the database (although you can configure other databases if needed). The database stores data related to users, attorneys, appointments, and payment details. It is lightweight and ideal for local development, though it can be switched out for more robust solutions in production.

### 3.3.3. Other Technologies
<a id="other-technologies"></a>

PayPal API: Integrated to handle payments and donations for clients booking consultations with attorneys.

Stripe API: Used for credit card payments, offering an additional payment option for clients.

## 4. Features
<a id="features"></a>

### 4.1 Lawyer Features
<a id="lawyer-features"></a>
The lawyer side of the website includes several key features to help manage their professional profile and workload:

1. Professional Bio/Attorney Profiles: Lawyers can create and manage their professional bio, displaying their legal expertise, qualifications, and practice areas.


2. Monitor Activity (Track): Attorneys can track their scheduled appointments and view upcoming client bookings.


3. Receive Payment: The website integrates payment gateways, allowing attorneys to receive payments securely for services rendered.


4. Contact Information: Attorneys can display and update their contact information, making it easier for clients to reach them.


5. Online Appointment Booking: Clients can directly book appointments with attorneys, with options to select dates and times based on availability.


6. Showcase Social Media: Lawyers can link to their social media profiles, providing additional ways for clients to connect and learn more about their work.


### 4.2. Client Features
<a id="client-features"></a>
The client side focuses on ease of use and accessibility:

1. Contact Information: Clients can view detailed contact information for attorneys, including email addresses, phone numbers, and office locations.


2. Book Appointments: Clients can easily schedule appointments with attorneys through an intuitive online booking system.


3. Pay Lawyer Fees: Clients can pay their lawyer fees securely through integrated payment gateways (PayPal and Stripe).


4. Seek Help: Clients can fill out contact forms or reach out directly to attorneys for legal advice and services.

## 5. Folder Structure 
<a id="folderstructure"></a>
The folder structure for the Lawyer-Connect project is organized for simplicity and scalability. It uses a Flask setup with separate folders for templates, static files, and other components.

![The folder structure](https://github.com/user-attachments/assets/208d3a6c-6259-463e-abc8-ecf41898a6d7)

## 6. Common Issues 
---
<a id="commonissues"></a>
Here are some Issues you may encounter with Lawyer connect as well as their solutions 

### Common Issues When Accessing the Lawyer-Connect Repository

1. User Login Issues
   - Solution:
      Ensure login details are correct. Reset password if needed. Check backend authentication config.
   

2. Stripe and PayPal Payments Not Working
   - Solution:
      Verify API keys in .env. Test in sandbox environment.
   

3. Page Not Loading Properly
   - Solution:
      Clear cache, check for 404 errors, ensure static files and routing are correct.
   

4. Admin Access Issues
   - Solution:
      Verify admin privileges, check user role and permissions in database.
   

5. "Repository Not Found" or "403 Forbidden" Error
   - Solution:
      Check repository URL, ensure correct permissions or collaborator access.
   

6. Failed to Clone the Repository
   - Solution:
      Set up Git environment, add SSH keys, or use HTTPS for cloning.
   

7. Outdated or Missing Dependencies
   - Solution:
      Run pip install -r requirements.txt, ensure Python and dependencies are updated.

N, [2/21/2025 11:45 PM]
8. Code Not Running as Expected
   - Solution:
      Double-check .env file and server configurations, ensure correct environment selected.
   

---


## 7. Contact information 
<a id="contactinformation"></a>
We, the team from Lawyer-Connect, are always happy about your feedback on our project or ideas for future collabortaion, we welcome your input. Your thoughts and suggestions will help us grow and improve this platform. We believe in the power of collaboratioin and would be exicited to explore potential partnerships for future projects.

Contact us through Github: [Lawyer-Connect Repository](https://github.com/ABELMATHIOS/Lawyer-Connect/)

####contributers
1. Abel Mathios: [https://github.com/ABELMATHIOS](https://github.com/ABELMATHIOS)
2. Siraj Abdulkadir: [https://github.com/Siraj-Abdulkadir](https://github.com/Siraj-Abdulkadir)
3. Nathenael Tamirat: [https://github.com/NathenaelTamirat](https://github.com/NathenaelTamirat)
4. Menilek Ayele: [https://github.com/MenilekAyele](https://github.com/MenilekAyele)
5. Haileyesus Dagne: [https://github.com/Haile-Eyesus](https://github.com/Haile-Eyesus).

WE ARE EAGER TO GROW AND LEARN!

## 8. Acknowledgement 
<a id="acknowledgement"></a>

We would like to extend our heartfelt thanks to our programming teacher, Mr. Tadesse Melesse, at BITS College, for giving us the opportunity to work together and build this project. 

## 9. Contributers  
<a id="contributers"></a>


We always welcome contributers from all around the world to help, to comment, to use, to fork and also improve this project! To start, you should fork the repo and submit a pull request with your changes. Don’t forget to test your code before adding it. Here’s the steps to contribute:

1. Fork this repo.
2. Create a new branch for your fix or feature.
3. Make sure you write tests for your changes.
4. Submit your pull request to the main branch.
5. Wait for our feedback and try to be patient.

We appreciate your contributions! Thank you!

N, [2/21/2025 11:46 PM]
<h1 align="center">LAWYER WEBSITE</h1>

## Overview
This repository contains the code and program for a fully functional lawyer website. Designed by BITS College students with modern web development technologies.  
The website is user-friendly, ensuring responsiveness, accessibility, and much more. It is tailored for lawyers to manage their agendas, monitor contact information, and promote themselves effectively. For clients, the site is easy to use, understand, and access. They can book appointments, pay fees, and much more.

Overall, this repository provides the source code for a professional lawyer website, created to showcase the services, team, and legal expertise of a law firm. It’s fully responsive, offering a seamless experience across most devices. The website provides essential information for potential clients, such as service offerings, team member profiles, contact details, and legal services.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Technologies Used](#technologies-used)
   - [Frontend](#frontend)
   - [Backend](#backend)
   - [Database](#database)
   - [Other Technologies](#other-technologies)
4. [Features](#features)
   - [Lawyer Features](#lawyer-features)
   - [Client Features](#client-features)
5. [FolderStructure](#folderstructure)
6. [Commonissues](#commonissues)
7. [Contactinfo](#contactinformation)
8. [Acknowledgement](#acknowledgement)
9. [Contributers](#contributers)
---

## 1. Installation
<a id="installation"></a>
Follow these steps to set up the Lawyer Connect project on your local machine.

### 1.1. Prerequisites
Before you begin, ensure you have the following software installed on your computer:
- Python 3.x or higher
- Git (for cloning the repository)
- pip (Python package manager)

### 1.2. Steps to Install

1. Clone the Repository  
   Clone the repository to your local machine using the following command:
   git clone https://github.com/ABELMATHIOS/Lawyer-Connect.git 

2. Navigate to the Project Directory
   Change your current directory to the project folder:
   cd Lawyer-Connect

3. Create a Virtual Environment
create a virtual environment for the project to avoid conflicts with other Python projects:
   python -m venv venv 
   
4. Activate Virtual environment

    A. windows
   venv\Scripts\activate
   B. macos/linux
   source venv/bin/activate

5. Install dependencies
   pip install -r requirements.txt

6. configure environment
   FLASK_APP=app.py
   SECRET_KEY=your_secret_key
   PAYPAL_CLIENT_ID=your_paypal_client_id

7. run the application
   flask run
8. testing
   pytest
...

## 2. Usage
<a id="usage"></a>
The website will display the homepage, where you can explore features like booking appointments, checking out attorney profiles, and paying fees. Depending on the user role (lawyer or client), the available features will differ.
Available Routes
Login Page

Route: /login
Access the login page to authenticate users.
Register Page

Route: /register
New users can register an account here.
Add User

Route: /adduser
Admins can add new users to the system.
Add Team

Route: /addteam
Admins can add new members to the legal team.
Meeting Booking

Route: /bookmeeting
Clients can book a meeting with a lawyer.
View Meetings

Route: /viewmeetings
View all scheduled meetings.

Route: /logout
Log out of the current session.
Payment Options
The app integrates with PayPal and Stripe for online payments. Once a meeting is scheduled, clients can make payments via these methods.

PayPal: Clients can use their PayPal account or card to pay for a meeting.
Stripe: A secure way to pay using a credit/debit card.
...

## 3. Technologies Used
<a id="technologies-used"></a>

### 3.1. Frontend
<a id="frontend"></a>
HTML/CSS: The website's structure and styling are built using HTML5 and CSS ensuring responsiveness across various devices

JavaScript: Used for dynamic interactions, including forms, appointment bookings, and integrating features like the Owl Carousel for testimonials

N, [2/21/2025 11:46 PM]
### 3.1.1. Backend
<a id="backend"></a>
The backend is powered by Python, specifically using the Flask web framework. Flask provides a simple yet powerful way to handle routes, user authentication, meeting scheduling, and integration with payment gateways like PayPal and Stripe.

### 3.2.2. Database
<a id="database"></a>
For this project, SQLite is used as the database (although you can configure other databases if needed). The database stores data related to users, attorneys, appointments, and payment details. It is lightweight and ideal for local development, though it can be switched out for more robust solutions in production.

### 3.3.3. Other Technologies
<a id="other-technologies"></a>

PayPal API: Integrated to handle payments and donations for clients booking consultations with attorneys.

Stripe API: Used for credit card payments, offering an additional payment option for clients.

## 4. Features
<a id="features"></a>

### 4.1 Lawyer Features
<a id="lawyer-features"></a>
The lawyer side of the website includes several key features to help manage their professional profile and workload:

1. Professional Bio/Attorney Profiles: Lawyers can create and manage their professional bio, displaying their legal expertise, qualifications, and practice areas.


2. Monitor Activity (Track): Attorneys can track their scheduled appointments and view upcoming client bookings.


3. Receive Payment: The website integrates payment gateways, allowing attorneys to receive payments securely for services rendered.


4. Contact Information: Attorneys can display and update their contact information, making it easier for clients to reach them.


5. Online Appointment Booking: Clients can directly book appointments with attorneys, with options to select dates and times based on availability.


6. Showcase Social Media: Lawyers can link to their social media profiles, providing additional ways for clients to connect and learn more about their work.


### 4.2. Client Features
<a id="client-features"></a>
The client side focuses on ease of use and accessibility:

1. Contact Information: Clients can view detailed contact information for attorneys, including email addresses, phone numbers, and office locations.


2. Book Appointments: Clients can easily schedule appointments with attorneys through an intuitive online booking system.


3. Pay Lawyer Fees: Clients can pay their lawyer fees securely through integrated payment gateways (PayPal and Stripe).


4. Seek Help: Clients can fill out contact forms or reach out directly to attorneys for legal advice and services.

## 5. Folder Structure 
<a id="folderstructure"></a>
The folder structure for the Lawyer-Connect project is organized for simplicity and scalability. It uses a Flask setup with separate folders for templates, static files, and other components.

![The folder structure](https://github.com/user-attachments/assets/208d3a6c-6259-463e-abc8-ecf41898a6d7)

## 6. Common Issues 
---
<a id="commonissues"></a>
Here are some Issues you may encounter with Lawyer connect as well as their solutions 

### Common Issues When Accessing the Lawyer-Connect Repository

1. User Login Issues
   - Solution:
      Ensure login details are correct. Reset password if needed. Check backend authentication config.
   

2. Stripe and PayPal Payments Not Working
   - Solution:
      Verify API keys in .env. Test in sandbox environment.
   

3. Page Not Loading Properly
   - Solution:
      Clear cache, check for 404 errors, ensure static files and routing are correct.
   

4. Admin Access Issues
   - Solution:
      Verify admin privileges, check user role and permissions in database.
   

5. "Repository Not Found" or "403 Forbidden" Error
   - Solution:
      Check repository URL, ensure correct permissions or collaborator access.
   

6. Failed to Clone the Repository
   - Solution:
      Set up Git environment, add SSH keys, or use HTTPS for cloning.
   

7. Outdated or Missing Dependencies
   - Solution:
      Run pip install -r requirements.txt, ensure Python and dependencies are updated.

N, [2/21/2025 11:46 PM]
8. Code Not Running as Expected
   - Solution:
      Double-check .env file and server configurations, ensure correct environment selected.
   

---


## 7. Contact information 
<a id="contactinformation"></a>
We, the team from Lawyer-Connect, are always happy about your feedback on our project or ideas for future collabortaion, we welcome your input. Your thoughts and suggestions will help us grow and improve this platform. We believe in the power of collaboratioin and would be exicited to explore potential partnerships for future projects.

Contact us through Github: [Lawyer-Connect Repository](https://github.com/ABELMATHIOS/Lawyer-Connect/)

####contributers
1. Abel Mathios: [https://github.com/ABELMATHIOS](https://github.com/ABELMATHIOS)
2. Siraj Abdulkadir: [https://github.com/Siraj-Abdulkadir](https://github.com/Siraj-Abdulkadir)
3. Nathenael Tamirat: [https://github.com/NathenaelTamirat](https://github.com/NathenaelTamirat)
4. Menilek Ayele: [https://github.com/MenilekAyele](https://github.com/MenilekAyele)
5. Haileyesus Dagne: [https://github.com/Haile-Eyesus](https://github.com/Haile-Eyesus).

WE ARE EAGER TO GROW AND LEARN!

## 8. Acknowledgement 
<a id="acknowledgement"></a>

We would like to extend our heartfelt thanks to our programming teacher, Mr. Tadesse Melesse, at BITS College, for giving us the opportunity to work together and build this project. 

## 9. Contributers  
<a id="contributers"></a>


We always welcome contributers from all around the world to help, to comment, to use, to fork and also improve this project! To start, you should fork the repo and submit a pull request with your changes. Don’t forget to test your code before adding it. Here’s the steps to contribute:

1. Fork this repo.
2. Create a new branch for your fix or feature.
3. Make sure you write tests for your changes.
4. Submit your pull request to the main branch.
5. Wait for our feedback and try to be patient.

We appreciate your contributions! Thank you!

N, [2/21/2025 11:46 PM]
MIT License

Copyright (c) 2025 Abel Mathios 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

N, [2/21/2025 11:46 PM]
# GitHub Project Policy for Lawyer-Connect

Welcome to the Lawyer-Connect repository! By contributing to or using this project, you agree to follow these guidelines and policies to ensure a positive and productive environment.

## 1. Code of Conduct

We aim to maintain a welcoming, loving, and respectful community for all contributors. By participating in this project, you agree to:

- Be respectful to others.
- Avoid harassment, abusive language, or any harmful behavior.
- Address disagreements constructively.

Violating these guidelines may result in being removed from the project.

## 2. Repository Content

All code and content shared within this repository must adhere to the following:

- Legal Compliance: All code, assets, and materials must comply with applicable laws and intellectual property rights.
- No Malicious Code: The repository must not contain malicious code, harmful scripts, or viruses.

### License

Content in this repository is governed by the MIT License. You must follow the terms outlined in the repository's LICENSE file.

## 3. Contribution Guidelines

We welcome contributions from everyone. To ensure consistency, please follow these rules when submitting changes:

- Fork and Pull: Please fork the repository and submit a pull request for any changes or improvements.
- Issue Tracking: Before submitting a pull request, please check if there's an existing issue related to the change. If not, create a new issue to discuss your feature or fix.
- Commit Messages: Use clear and descriptive commit messages.
- Testing: Ensure that your code is properly tested and does not break existing functionality.

## 4. Privacy and Security

We respect your privacy and take security seriously:

- Personal Data: Do not store sensitive personal data (e.g., passwords, user info) in this repository.
- Security Vulnerabilities: If you discover a security vulnerability, please report it privately via helplawyerconnect@gmail.com rather than posting it publicly.

## 5. Use of GitHub Pages

If you're deploying this project using GitHub Pages:

- No Spamming: Don't use GitHub Pages for any form of advertising, spamming, or commercial purposes unrelated to the project.
- Content Restrictions: Avoid hosting illegal, harmful, or inappropriate content on GitHub Pages.

## 6. Repository Maintenance

This repository is actively maintained. If a contributor is inactive for a long period or violates the guidelines, we may remove them from the project. This is done to maintain quality and momentum.

## 7. Enforcement

If you fail to comply with any part of this policy, you may be banned or restricted from contributing to this project permanently.

## 8. License

By contributing to this project, you agree that your contributions are licensed under the terms of the project’s chosen license (MIT License).

### The MIT License:

```text
MIT License

Copyright (c) 2025 ABELMATHIOS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
