# RentCast Testing Project

This project focuses on applying both UI and API testing for the RentCast website. The project is structured into two main folders: **API Testing** and **UI Testing**, each containing relevant files and scripts.

---

## Project Outline

### API Testing

The **API Testing** folder contains the following:

- **collection.json**: A Postman collection summarizing the implemented API tests.
- **responses**: A folder containing detailed responses for the Postman requests.

List of API requests tested:
1. Generate PDF Report
2. Get Rental Listings
3. Market Statistics
4. Property Records
5. Rent Estimate
6. Rental Listing by ID
7. User Login
8. Value Estimation

---

### UI Testing

The **UI Testing** folder is organized into two subcategories:

#### **Negative Test Scenarios**
Scripts testing invalid or unexpected inputs:
- `EmptyFieldSignIn.py`
- `EmptySearchBox.py`
- `InvalidEmailSignup.py`
- `NegativeArea.py`
- `NegativeChangePassword.py`
- `TestBrokenLinks-Negative.py`
- `TestInvalidAPIKeyCreation-Negative.py`

#### **Positive Test Scenarios**
Scripts verifying expected behavior for valid inputs:
- `APIDashboardWithSignIn.py`
- `ValidPropertySearch.py`
- `ContactSupport.py`
- `HelpCenter.py`
- `NotificationButton.py`
- `SignIn.py`
- `SignInMyPortfolio.py`
- `SignUp.py`

---

This comprehensive setup ensures robust testing coverage for both API endpoints and the website's user interface, identifying and addressing potential issues effectively. 

