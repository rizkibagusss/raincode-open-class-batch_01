const transactions = [];

const form = document.querySelector("#transaction-form");
const rows = document.querySelector("#transaction-rows");
const emptyState = document.querySelector("#empty-state");
const count = document.querySelector("#count");
const arrayOutput = document.querySelector("#array-output");
const message = document.querySelector("#form-message");

function formatCurrency(value) {
  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    maximumFractionDigits: 2,
  }).format(value);
}

function renderTable() {
  rows.innerHTML = transactions.map((item) => `
    <tr>
      <td><span class="id-chip">${item.id}</span></td>
      <td>${item.nama}</td>
      <td>${formatCurrency(item.total)}</td>
      <td><button class="remove" data-id="${item.id}" aria-label="Hapus ${item.nama}">×</button></td>
    </tr>
  `).join("");

  emptyState.hidden = transactions.length > 0;
  count.textContent = transactions.length;
  arrayOutput.textContent = JSON.stringify(transactions, null, 2);
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const nama = form.nama.value.trim();
  const total = Number(form.total.value);

  if (!nama || !Number.isFinite(total) || total < 0) {
    message.textContent = "Periksa kembali nama dan total.";
    return;
  }

  transactions.push({
    id: transactions.length ? Math.max(...transactions.map((item) => item.id)) + 1 : 1,
    nama,
    total,
  });

  form.reset();
  form.nama.focus();
  message.textContent = "Object masuk ke array. Sekarang coba refresh browser.";
  renderTable();
});

rows.addEventListener("click", (event) => {
  const button = event.target.closest("[data-id]");
  if (!button) return;
  const index = transactions.findIndex((item) => item.id === Number(button.dataset.id));
  if (index !== -1) transactions.splice(index, 1);
  renderTable();
});

renderTable();
