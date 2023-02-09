const $d = document;

$d.addEventListener("DOMContentLoaded", () => {
  const $listBtnDelete = $d.querySelectorAll("a[data-delete-id]");

  $d.addEventListener("click", (e) => {
    if (Array.prototype.indexOf.call($listBtnDelete, e.target) !== -1) {
      console.log("hola");
      const $btnDelete = e.target,
        id = $btnDelete.dataset.deleteId,
        $trPet = $d.getElementById(`pet-${id}`),
        data = [];

      $trPet.childNodes.forEach((child) => {
        if (
          child.nodeType === 1 &&
          !["Acciones", "Creado hace", "Actualizado hace"].includes(
            child.dataset.label
          )
        ) {
          data.push({ title: child.dataset.label, value: child.textContent });
        }
      });

      const modalContentString = `
            <div class="modal fade" id="modalPetDelete" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="modalPetDeleteLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="modalPetDeleteLabel">¿Estás seguro de eliminar a la mascota?</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    ${data
                      .map(
                        (item) => `
                      <div>
                        <div class="d-flex flex-wrap justify-content-center gap-3 mb-4">
                          <h5 class="m-0 align-self-end">${item.title} :</h5>
                          <div class="border-bottom border-1 text-center" style="flex-grow: 1">
                            <span>${item.value} </span>
                          </div>
                        </div>
                      </div>
                    `
                      )
                      .join("")}
                  </div>
                  <div class="modal-footer d-flex flex-wrap">
                    <a class="btn btn-danger" style="flex-grow: 1;" href="/pet/${id}/delete">Eliminar</a>
                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal" style="flex-grow: 1;">Cancelar</button>
                  </div>
                </div>
              </div>
            </div>
          `;

      const $modalContent = new DOMParser().parseFromString(
        modalContentString,
        "text/html"
      ).body.firstElementChild;

      $d.body.appendChild($modalContent);

      const $modal = $d.getElementById("modalPetDelete"),
        modalInstance = new bootstrap.Modal($modal);

      modalInstance.show();

      $modal.addEventListener("hidden.bs.modal", () => {
        modalInstance.dispose();
        $d.body.removeChild($modal);
      });
    }
  });
});
