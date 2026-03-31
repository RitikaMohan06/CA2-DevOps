document.getElementById("feedbackForm").addEventListener("submit", function(e) {

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let mobile = document.getElementById("mobile").value.trim();
    let dept = document.getElementById("department").value;
    let comments = document.getElementById("comments").value.trim();
    let gender = document.querySelector('input[name="gender"]:checked');

    let error = document.getElementById("error");
    error.innerText = "";

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    let mobilePattern = /^[0-9]{10}$/;

    if (name === "") {
        error.innerText = "Name cannot be empty";
        e.preventDefault();
        return;
    }

    if (!email.match(emailPattern)) {
        error.innerText = "Invalid Email format";
        e.preventDefault();
        return;
    }

    if (!mobile.match(mobilePattern)) {
        error.innerText = "Invalid Mobile Number";
        e.preventDefault();
        return;
    }

    if (!dept) {
        error.innerText = "Please select a department";
        e.preventDefault();
        return;
    }

    if (!gender) {
        error.innerText = "Please select gender";
        e.preventDefault();
        return;
    }

    let wordCount = comments.split(/\s+/).length;
    if (comments === "" || wordCount < 10) {
        error.innerText = "Feedback must be at least 10 words";
        e.preventDefault();
        return;
    }

    alert("Form submitted successfully!");
});