document.addEventListener("DOMContentLoaded", () => {
    const currentYearElement = document.getElementById("currentYear");
    if (currentYearElement) {
        currentYearElement.textContent = new Date().getFullYear();
    }
    checkForSuccessMessage();
});

const showRegisterForm = () => {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('register-form').style.display = 'block';
}

const showLoginForm = () => {
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
}

const checkForSuccessMessage = () => {
    const messageModalElement = document.getElementById('messageModal');
    if (messageModalElement) {
        const messageModal = new bootstrap.Modal(messageModalElement);
        messageModal.show();
    }
}
