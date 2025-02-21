<h1 align="center">LAWYER WEBSITE</h1>

## Overview
This repository contains the code and program for a fully functional lawyer website. Designed by BITS College students with modern web development technologies.  
The website is user-friendly, ensuring responsiveness, accessibility, and much more. It is tailored for lawyers to manage their agendas, monitor contact information, and promote themselves effectively. For clients, the site is easy to use, understand, and access. They can book appointments, pay fees, and much more.

Overall, this repository provides the source code for a professional lawyer website, created to showcase the services, team, and legal expertise of a law firm. It’s fully responsive, offering a seamless experience across most devices. The website provides essential information for potential clients, such as service offerings, team member profiles, contact details, and legal services.

---

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


---

## 1. Installation
...

Follow these steps to set up the **Lawyer Connect** project on your local machine.

### Prerequisites
Before you begin, ensure you have the following software installed on your computer:
- **Python 3.x** or higher
- **Git** (for cloning the repository)
- **pip** (Python package manager)

### Steps to Install

1. **Clone the Repository**  
   Clone the repository to your local machine using the following command:
```bash
   git clone https://github.com/ABELMATHIOS/Lawyer-Connect.git 
```

2. Navigate to the Project Directory
   Change your current directory to the project folder:
```bash
   cd Lawyer-Connect
```

3. Create a Virtual Environment
create a virtual environment for the project to avoid conflicts with other Python projects:
```bash
   python -m venv venv 
```
   
4. Activate Virtual environment
   A. windows
```bash
   venv\Scripts\activate
```
   B. macos/linux
```bash
   source venv/bin/activate
```

5. Install dependencies
```bash
   pip install -r requirements.txt
```

6. configure environment
```bash
   FLASK_APP=app.py
   SECRET_KEY=your_secret_key
   PAYPAL_CLIENT_ID=your_paypal_client_id
```

7. run the application
```bash
   flask run
```
8. testing
```bash
   pytest
```


# 2. Usage


The website will display the homepage, where you can explore features like booking appointments, checking out attorney profiles, and paying fees. Depending on the user role (lawyer or client), the available features will differ.
Available Routes
Login Page

Route: `/login`
Access the login page to authenticate users.
Register Page

Route: `/register`
New users can register an account here.
Add User

Route: `/adduser`
Admins can add new users to the system.
Add Team

Route: `/addteam`
Admins can add new members to the legal team.
Meeting Booking

Route: `/bookmeeting`
Clients can book a meeting with a lawyer.
View Meetings

Route: `/viewmeetings`
View all scheduled meetings.
Update Meetings

Route: `/updatemeeting`
Admins or users can update meeting details.
Delete Meetings

Route: `/deletemeeting`
Admins or users can delete meetings from the system.
Log Out

Route: `/logout`
Log out of the current session.
Payment Options
The app integrates with PayPal and Stripe for online payments. Once a meeting is scheduled, clients can make payments via these methods.

PayPal: Clients can use their PayPal account or card to pay for a meeting.
Stripe: A secure way to pay using a credit/debit card.

# 3. Technologies Used

# 3.1 Frontend

`HTML/CSS`: The website's structure and styling are built using HTML5 and CSS ensuring responsiveness across various devices.

`JavaScript`: Used for dynamic interactions, including forms, appointment bookings, and integrating features like the Owl Carousel for testimonials.

`Owl Carousel`: A responsive carousel used to showcase testimonials and client feedback.


# 3.2 Backend

The backend is powered by `Python`, specifically using the Flask web framework. Flask provides a simple yet powerful way to handle routes, user authentication, meeting scheduling, and integration with payment gateways like PayPal and Stripe.

# 3.3 Database

For this project, `SQLite` is used as the database (although you can configure other databases if needed). The database stores data related to users, attorneys, appointments, and payment details. It is lightweight and ideal for local development, though it can be switched out for more robust solutions in production.

# 3.4 Other Technologies

`PayPal API`: Integrated to handle payments and donations for clients booking consultations with attorneys.

`Stripe API`: Used for credit card payments, offering an additional payment option for clients.


# # 4. Features

# 4.1 Lawyer Features

The lawyer side of the website includes several key features to help manage their professional profile and workload:

1. `Professional Bio/Attorney Profiles`: Lawyers can create and manage their professional bio, displaying their legal expertise, qualifications, and practice areas.


2. `Monitor Activity (Track)`: Attorneys can track their scheduled appointments and view upcoming client bookings.


3. `Receive Payment`: The website integrates payment gateways, allowing attorneys to receive payments securely for services rendered.


4. `Contact Information`: Attorneys can display and update their contact information, making it easier for clients to reach them.


5. `Online Appointment Booking`: Clients can directly book appointments with attorneys, with options to select dates and times based on availability.


6. `Showcase Social Media`: Lawyers can link to their social media profiles, providing additional ways for clients to connect and learn more about their work.



# 4.2 Client Features

The client side focuses on ease of use and accessibility:

1. `Contact Information`: Clients can view detailed contact information for attorneys, including email addresses, phone numbers, and office locations.


2. `Book Appointments`: Clients can easily schedule appointments with attorneys through an intuitive online booking system.


3. `Pay Lawyer Fees`: Clients can pay their lawyer fees securely through integrated payment gateways (PayPal and Stripe).


4. `Seek Help`: Clients can fill out contact forms or reach out directly to attorneys for legal advice and services.



