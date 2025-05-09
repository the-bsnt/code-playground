function togglePassword() {
  const passwordInput = document.getElementById("id_password");
  const toggleIcon = document.querySelector(".toggle-password i");
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    toggleIcon.classList.remove("fa-eye");
    toggleIcon.classList.add("fa-eye-slash");
  } else {
    passwordInput.type = "password";
    toggleIcon.classList.remove("fa-eye-slash");
    toggleIcon.classList.add("fa-eye");
  }
}

setTimeout(function () {
  var msg = document.getElementById("popup-msg");

  if (msg) {
    msg.style.animation = "fadeOut 0.5s ease forwards";
  }
}, 3000); // 3000ms = 3 seconds
