function handleKeyPress(event) {
  let query = document.getElementById("search").value.trim();
  if (event.key === "Enter" && query !== "") {
      window.location.href = `/search-results/?q=${query}`; // Redirect to results page
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const menuButton = document.querySelector(".menu-btn"); // Hamburger icon
  const mobileMenu = document.querySelector(".mobile-menu");
  const closeButton = document.querySelector(".close-menu");

  // Open the mobile menu
  menuButton.addEventListener("click", function (event) {
      event.stopPropagation(); // Prevents click event from bubbling up
      mobileMenu.classList.add("active");
  });

  // Close the mobile menu when clicking the close button
  if (closeButton) {
      closeButton.addEventListener("click", function (event) {
          event.stopPropagation(); // Prevents event bubbling
          mobileMenu.classList.remove("active");
      });
  }

  // Close menu when clicking outside
  document.addEventListener("click", function (event) {
      if (!mobileMenu.contains(event.target) && !menuButton.contains(event.target)) {
          mobileMenu.classList.remove("active");
      }
  });
});
