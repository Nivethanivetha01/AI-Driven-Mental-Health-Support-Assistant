function validateForm() {
    const password = document.getElementById("password").value;
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;

    //if (!passwordRegex.test(password)) {
       // alert("Password must be at least 8 characters long, contain at least one uppercase letter, and one number.");
//return false;
   // }

    // Redirect to index.html after successful validation
    window.location.href = "index.html";
    return false; // Prevent actual form submission to keep the redirect
}
