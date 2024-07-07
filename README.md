# Simple Ecommerce Website

<!-- - ### add urls for  -->
 <!-- - ## Tasks TODO:    
    
    - #### JWT authentication to ensure many users can interact with it.
    - #### all request to be through JWT auth.
    - #### Integration with third-party api's (Razorpay, Stripe, Paypal).
    - #### Ability to register new users.
    - #### Shopping cart management.
    - #### Product listings.
    - #### Ability to create and edit products in the database. -->


> #### JWT Authentication
<!-- > #### Responsibilities: -->

<!-- - JWT token creation upon user login
- JWT token validation for secure endpoints
Steps: -->

- Implement user login endpoint **Done**
- Generate JWT token upon successful login **Done**
- Middleware to validate JWT tokens for protected routes **Done**
> #### User Management
<!-- Responsibilities: -->

<!-- Create new users
Manage user details
Steps: -->

- User registration endpoint
- User profile management endpoints
> #### Shopping Cart Management
<!-- Responsibilities:

Add products to the cart
Remove products from the cart
View cart items
Checkout process with payment gateway integration
Steps: -->

- Endpoints to add, remove, and view cart items 
- Checkout endpoint that integrates with Stripe for payments
> #### Product Listings
<!-- Responsibilities:

Display list of products
View product details
Steps: -->

- Endpoint to list products **Done**
- Endpoint to view individual product details **Done**
> #### Product Management
<!-- Responsibilities:

Create new products
Edit existing products
Delete products
Steps: -->

- Endpoints to create, edit, and delete products **Done**