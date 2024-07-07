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

## `Backend Tasks`

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

- User registration endpoint   **Done**
- User profile management endpoints   **Done**
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


---

## `Frontend Tasks`

> ####  Home Page
<!-- Responsibilities:

Display featured products or categories.
Provide navigation to other sections of the site. -->
<!-- `Logic` -->

- Fetch and display featured products or categories from the backend.
- Implement navigation to other sections like product listings, user login/register, etc.
> ####  Product Listing Page
<!-- Responsibilities:

Display a list of products.
Allow users to filter and sort products.
Logic: -->

- Fetch product data from the backend.
- Implement filtering and sorting logic.
- Navigation to individual product detail pages.
> #### Product Detail Page
<!-- Responsibilities:

Display detailed information about a product.
Allow users to add the product to the cart.
Logic: -->

- Fetch product details based on product ID from the backend.
- Implement "Add to Cart" functionality.
> #### Cart Page
<!-- Responsibilities:

Display products added to the shopping cart.
Allow users to modify cart items (quantity, remove items).
Logic: -->

- Fetch cart items from the backend.
- Implement logic to update item quantities and remove items.
- Navigation to checkout page.
> #### Checkout Page
<!-- Responsibilities:

Collect user payment and shipping information.
Process the payment using the Stripe integration.
Logic: -->

- Display cart summary and total amount.
- Collect payment details and shipping address.
- Implement Stripe payment processing.
- Handle payment success and failure responses.
> #### User Registration Page
<!-- Responsibilities:

Allow new users to create an account.
Logic: -->

- Collect user details (username, password, etc.).
- Implement form validation.
- Send registration request to the backend.
- Handle success and error responses.
> #### User Login Page
<!-- Responsibilities:

Allow existing users to log in.
Logic: -->

- Collect user credentials (username, password).
- Implement form validation.
- Send login request to the backend.
- Handle JWT token on successful login and store it for authenticated requests.
> #### User Profile Page
<!-- Responsibilities:

Display and allow users to update their profile information.
Display order history.
Logic: -->

- Fetch user profile and order history from the backend.
- Implement logic to update user profile details.
> #### Admin Dashboard
<!-- Responsibilities:

Allow administrators to manage products (create, edit, delete).
Logic: -->

- Implement product management functionalities (create, edit, delete).
- Fetch and display product data for management.
- Handle form submissions for product updates.