function handleKeyPress(event) {
  let query = document.getElementById("search").value.trim();
  if (event.key === "Enter" && query !== "") {
      window.location.href = `/search-results/?q=${query}`; // Redirect to results page
  }
}