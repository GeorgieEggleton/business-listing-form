
# Introduction
Mandens is a business transfer agents and valuers specialising in the sale of Fish & Chip businesses across the UK.  Established over 50 years ago they are now the leading agent in this sector. 

In order to list a new business for sale the first step of the process is to collect the owners information and some basic trading information of the business in order to generate the legal paperwork. Often collecting this information takes several calls with the owner while they check various pieces of information. 

In order for Mandens to have a more efficient use of the agents time the business listing site developed here will allow the owners of a business to register an account and upload their (or the legal owner of the business) details as well as the business details from home when they have all the information to hand. They will also be able to log back in at any time to view, update or delete the business information if needed. 

The admin (Mandens) will be able to log in and see a full list of all the businesses that are due to be listed with all the required information to generate the legal paperwork needed. 


#####Login Details:
To login and see an example vendor with current businesses listed please use

Username: JohnsFishandChips
Password: FishShop123

To login as admin and see information of all businesses please use:

Username: Admin
Password: Firefly2


Live site
A link to the live site can be found here - https://online-disposal-form-c3c0cc829bfc.herokuapp.com/


*** Mock Up ****



# Features

### Favicon
A favicon is used to help the user identify the correct site when they have multiple tabs open. I have used a custom image which is part of the main Mandes logo. 
![Favicon Screenshot](/docs/readme-images/favicon.png)




### Home Page
On first loading the website the user is directed to the homepage. This is styled to look very similar the homepage of the main Mandens website to keep the brand styling continuity and ensure it is easily recognisable to the user. The user has two options, if this is their first time visiting the site they can register and account, or if they have previously done that they can login to edit or delete their business details. 
![Home Page Screenshot](/docs/readme-images/home.png)


### Registration
If the user is coming to the site for the first time they will click on the “Register” button. This will direct them to the signup page were they will be able to create their account details. 
![Registration Screenshot](/docs/readme-images/registration.png)

### Login
If the user is returning to the site having already previously set up their account they will click the “Log In” button. This will redirect them to the singing page where they will just need to enter their username and password. There is also an option to click “Remember Me” it speed up further sign in’s if they are working from the safety of their own private computer. 
![Login Screenshot](/docs/readme-images/login.png)

### Vendor Details
After registering for an account the user will then be re-directed to the Vendor Input page. This is where the user will be asked to input the details of the legal owner and vendor of the business. All fields in this section are mandatory fields as all this information will be required by the Admin in order to complete the legal paperwork to sell the business. Once they Have done this and clicked “Submit” They will be re-directed to their own personal overview page. 
![Vendor Input Screenshot](/docs/readme-images/vendor-input.png)

### Overview Page
The overview page will display to the user all of their personal and business information. In the first instance it will only show the vendor details and below where the businesses will appear is a large button to add a new business. 
![Overview Vendor Details Screenshot](/docs/readme-images/overview-vendor-details.png)

Once the user has added one or more businesses these will all be displayed on the overview page. I have used accordians to list all the businesses as it is possible that one user could have many businesses for sale. The accordions assure that the page is easy to read and manage. When the accordion for each business is clicked it opens and displays the relevant business information. 
![Overview Screenshot](/docs/readme-images/overview.png)

![Open Accordian Screenshot](/docs/readme-images/open-business.png)

### Admin Overview Page
If you are logged in as the admin the overview page will show all businesses loaded by all users. Instead of loading at the top of the page as per the normal overview page, the Vendor details for each business will be added to each business individually so that the admin can have a complete overview of all the new businesses being added and deal with the appropriate paperwork. 
![Open Accordian Screenshot](/docs/readme-images/admin-overview.png)


# Wireframes
The heart of the project and the main functionality is the overview page. This is the main area where both the customer and the admin can access, edit, and delete their details.
![Wireframe](/docs/readme-images/main-design.png) 


# Testing
![home Page Test](/docs/readme-images/home-page-test.png) 
![login Page Test](/docs/readme-images/login-page-test.png)
![registration Page Test](/docs/readme-images/registration-page-test.png)
![overview Page Test](/docs/readme-images/overview-page-test.png)

The Lighthouse testing was not as good as hoped on the prefeormance section. Due to time restraints I was not able to fix this. It was noted this was due to image size. Perhaps in futrue limit size of images user can upload. 
![Lighthouse Test](/docs/readme-images/lighthouse-test.png)


On the HTML Validator there is still one error I was unable to remove before submitting. However the site seems to work as expected. 
![HTML Validator Test](/docs/readme-images/html-validator.png)

All tests passed on css validator
![CSS Validator Test](/docs/readme-images/css-validator.png)


# Agile Methodologies
Throughout the project I used an agile methodology using GitHub’s KanBan board to plan, manage and complete each milestone within the assignment. 


# Technologies Used
#### Languages
* HTML5
* CSS3
* Python 


#### Libraries and Frameworks
* Django
* Cloudinary
* CrispyForms
* Gunicorn
* Psycopg2
* Google Fonts
* Bootstrap


#### Tools
* GitPod
* GitHub
* Git
* Heroku
* ElephantSQL
* SQLite3
* FontAwesome
* Balsamiq
* W3C Validator
* W3C CSS Validator
* Lighthouse
* WhiteNoise


# Future Features

I would have like to have added confirmation of deleting a business before its deleted via a model. However due to time restraints this was not possible at this time. 






