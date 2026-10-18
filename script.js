document.querySelectorAll(".chip").forEach((button) => {
  button.addEventListener("click", () => {
    const input = document.getElementById("movieInput");
    input.value = button.dataset.title;
    input.focus();
  });
});
