function movePhones(direction) {
  const phoneContainer = document.querySelector(".phone");
  const phoneWidth = document.querySelector(".inphone").offsetWidth + 20; // Includes margin between items
  if (direction === "left") {
    phoneContainer.scrollBy({ left: -phoneWidth, behavior: "smooth" });
  } else {
    phoneContainer.scrollBy({ left: phoneWidth, behavior: "smooth" });
  }
}

