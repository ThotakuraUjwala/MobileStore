function movePhones(direction) {
  const phoneContainer = document.querySelector(".phone");
  const phoneWidth = document.querySelector(".inphone").offsetWidth + 20; // Includes margin between items
  if (direction === "left") {
    phoneContainer.scrollBy({ left: -phoneWidth, behavior: "smooth" });
  } else {
    phoneContainer.scrollBy({ left: phoneWidth, behavior: "smooth" });
  }
}

// offers
function moveProducts(direction) {
  const container = document.querySelector('#productContainer');
  const scrollAmount = 300; // Adjust as per required scroll step
  const offset = direction === 'left' ? -scrollAmount : scrollAmount;
  container.scrollBy({ left: offset, behavior: 'smooth' });
}

