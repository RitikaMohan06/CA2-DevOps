#  Student Feedback Registration Form 

##  Project Overview

This project is a **Student Feedback Registration Form** developed using:

* HTML
* CSS (Internal + External)
* JavaScript (Validation)
* Selenium (Automation Testing)
* Jenkins (CI/CD Automation)

The goal is to design a user-friendly form, validate inputs, automate testing, and execute tests using Jenkins.

---

##  Project Structure

```
StudentFeedbackForm/
│
├── index.html        # Main HTML form
├── styles.css        # External CSS styling
├── script.js         # JavaScript validation
├── test_form.py      # Selenium test script
├── chromedriver.exe  # Chrome driver (required for Selenium)
```

---

##  Features

###  Form Fields

* Student Name
* Email ID
* Mobile Number
* Department (Dropdown)
* Gender (Radio Buttons)
* Feedback Comments
* Submit & Reset Buttons

---

###  UI Design

* Clean and simple layout
* Responsive structure
* Combination of internal and external CSS

---

###  Validation (JavaScript)

The form includes:

* Required field checks
* Email format validation
* Mobile number validation (10 digits)
* Gender selection validation
* Department selection validation
* Feedback must contain at least 10 words

---

##  Selenium Test Cases

The automation script (`test_form.py`) performs:

1.  Page load verification
2.  Valid form submission
3.  Empty field validation
4.  Invalid email check
5.  Invalid mobile number check
6.  Dropdown functionality
7.  Reset button functionality

---

##  Setup Instructions

###  1. Install Python

Check installation:

```bash
python --version
```

---

###  2. Install Selenium

```bash
pip install selenium
```

---

###  3. Setup ChromeDriver

* Download matching ChromeDriver version
* Place `chromedriver.exe` inside project folder

---

###  4. Run Selenium Test

```bash
python test_form.py
```

---

##  Jenkins Integration

### Steps Performed:

1. Installed Jenkins
2. Created Pipeline Job
3. Configured pipeline script
4. Executed Selenium tests

---

###  Jenkins Pipeline Script

```groovy
pipeline {
    agent any

    stages {
        stage('Install Selenium') {
            steps {
                bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install selenium'
            }
        }

        stage('Run Test') {
            steps {
                dir('D:\\DevOps\\CA 2 DevOps (Latest)\\StudentFeedbackForm') {
                    bat '"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" test_form.py'
                }
            }
        }
    }
}
```

---

##  How It Works

1. User fills the form
2. JavaScript validates inputs
3. Selenium automates test cases
4. Jenkins runs tests automatically
5. Build result shows success/failure

---

## Expected Output

* Successful form validation
* Automated browser testing
* Jenkins build status:

  *  SUCCESS
  *  FAILURE (if errors exist)
<img width="1113" height="287" alt="image" src="https://github.com/user-attachments/assets/e2359914-ef83-4498-a8cb-a7c09c2e3abc" />
<img width="1080" height="1092" alt="image" src="https://github.com/user-attachments/assets/9a8b8b98-48f1-4a2e-8834-d1ae7eae48bc" />


---

## Common Issues

* Incorrect file path in Jenkins
* Python not configured in Jenkins
* ChromeDriver version mismatch
* Missing files in project folder

---

## Conclusion

This project demonstrates:

* Frontend development
* Client-side validation
* Automation testing using Selenium
* Continuous Integration using Jenkins

---

## Author

**Ritika Mohan**

---
