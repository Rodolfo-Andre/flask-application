const $d = document;

const insertModal = (modalContentString) => {
  const $modalContent = new DOMParser().parseFromString(
    modalContentString,
    "text/html"
  ).body.firstElementChild;

  $d.body.appendChild($modalContent);
};

const showModal = (idModal) => {
  const $modal = $d.getElementById(idModal),
    modalInstance = new bootstrap.Modal($modal);

  modalInstance.show();

  addHiddenEventModal($modal, modalInstance);
};

const addHiddenEventModal = ($modal, modalInstance) => {
  $modal.addEventListener("hidden.bs.modal", () => {
    modalInstance.dispose();
    $modal.remove();
  });
};

const hiddeDivMesssage = () => {
  const $divMessage = $d.querySelector("div[data-message]");

  setTimeout(() => {
    if ($divMessage) {
      $divMessage.remove();
    }
  }, 5000);
};

const showModalAddBreed = () => {
  const modalContentString = `
            <div class="modal fade" id="modalPetDelete" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="modalPetDeleteLabel" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="modalPetDeleteLabel">Agregar Raza</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <form method="POST" id="form-breed" action="/breed">
                      <div class="d-flex flex-wrap">
                        <label for="name">Raza: </label>
                        <input type="text" class="form-control" id="name" name="name" placeholder="Ingresa la raza" required maxlength="20"/>
                      </div>
                    </form>
                  </div>
                  <div class="modal-footer d-flex flex-wrap">
                    <input type="submit" class="btn btn-primary" style="flex-grow: 1;" form="form-breed" value="Añadir" />
                    <button type="button" class="btn btn-danger" data-bs-dismiss="modal" style="flex-grow: 1;">Cancelar</button>
                  </div>
                </div>
              </div>
            </div>
  `;

  insertModal(modalContentString);
  showModal("modalPetDelete");
};

export { $d, insertModal, showModal, showModalAddBreed, hiddeDivMesssage };
