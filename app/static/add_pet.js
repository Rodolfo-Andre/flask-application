import { $d, showModalAddBreed, hiddeDivMesssage } from "./utils.js";

$d.addEventListener("DOMContentLoaded", () => {
  hiddeDivMesssage();

  const $btnAddBreed = $d.getElementById("btn-add-breed");

  $d.addEventListener("click", (e) => {
    if ($btnAddBreed === e.target) {
      showModalAddBreed();
    }
  });
});
