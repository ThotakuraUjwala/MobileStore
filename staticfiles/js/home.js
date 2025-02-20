function movePhones(direction, button) {
  const phoneContainer = button.closest(".phone-container").querySelector(".phone");
  const phoneWidth = phoneContainer.querySelector(".inphone").offsetWidth + 20;

  if (direction === "left") {
    phoneContainer.scrollBy({ left: -phoneWidth, behavior: "smooth" });
  } else {
    phoneContainer.scrollBy({ left: phoneWidth, behavior: "smooth" });
  }
}
