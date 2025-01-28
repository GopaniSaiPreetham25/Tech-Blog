// function login() {
//     const email = document.getElementById('email').value;
//     const password = document.getElementById('password').value;
//     if (!email || !password) {
//         alert('Please fill in all fields');
//         return;
//     }
//     alert('Logging in...');
//     // Add login functionality here
// }
// function createAccount() {
//     alert('Redirecting to account creation...');
//     // Add create account functionality here
// }
function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    if (!email || !password) {
        alert('Please fill in all fields');
        return;
    }
    // alert('Logging in...');
    // Add login functionality here
}
function createAccount() {
    alert('Redirecting to account creation...');
    // Add create account functionality here
}
function createAccount() {
    // Redirect to the Create Account page
    window.location.href = '/create-account/';
}
