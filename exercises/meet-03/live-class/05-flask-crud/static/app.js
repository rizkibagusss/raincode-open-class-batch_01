let transactions = [];
const form = document.querySelector("#form");
const idInput = document.querySelector("#transaction-id");
const rows = document.querySelector("#rows");
const message = document.querySelector("#message");
const status = document.querySelector("#status");

const money = (value) => new Intl.NumberFormat("id-ID", {style:"currency",currency:"IDR"}).format(value);

async function api(url, options = {}) {
  const response = await fetch(url, {headers:{"Content-Type":"application/json"}, ...options});
  const data = response.status === 204 ? null : await response.json();
  if (!response.ok) throw new Error(data?.error || `HTTP ${response.status}`);
  return data;
}

async function load() {
  try {
    transactions = await api("/api/transactions");
    rows.innerHTML = transactions.map((item) => `<tr><td><i>${item.id}</i></td><td>${item.nama}</td><td>${money(item.total)}</td><td><button data-edit="${item.id}">Edit</button><button data-delete="${item.id}" class="danger">Delete</button></td></tr>`).join("");
    document.querySelector("#empty").hidden = transactions.length > 0;
    document.querySelector("#count").textContent = `${transactions.length} ROW`;
    status.textContent = "● MySQL connected · data permanent";
  } catch (error) { status.textContent = `● ${error.message}`; status.classList.add("error"); }
}

function resetForm() {
  form.reset(); idInput.value = ""; document.querySelector("#form-mode").textContent = "CREATE · POST";
  document.querySelector("#form-title").textContent = "Transaksi baru"; document.querySelector("#cancel").hidden = true;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const payload = {nama:form.nama.value,total:form.total.value};
  const id = idInput.value;
  try {
    await api(id ? `/api/transactions/${id}` : "/api/transactions", {method:id?"PATCH":"POST",body:JSON.stringify(payload)});
    message.textContent = id ? "UPDATE berhasil dan di-commit." : "INSERT berhasil dan di-commit.";
    resetForm(); await load();
  } catch (error) { message.textContent = error.message; }
});

rows.addEventListener("click", async (event) => {
  const editId = event.target.dataset.edit;
  const deleteId = event.target.dataset.delete;
  if (editId) {
    const item = transactions.find((row) => row.id === Number(editId));
    idInput.value=item.id; form.nama.value=item.nama; form.total.value=item.total;
    document.querySelector("#form-mode").textContent="UPDATE · PATCH"; document.querySelector("#form-title").textContent=`Edit row #${item.id}`; document.querySelector("#cancel").hidden=false;
  }
  if (deleteId && confirm(`DELETE row #${deleteId}?`)) {
    try { await api(`/api/transactions/${deleteId}`, {method:"DELETE"}); message.textContent="DELETE berhasil dan di-commit."; await load(); }
    catch (error) { message.textContent=error.message; }
  }
});
document.querySelector("#cancel").addEventListener("click", resetForm);
load();
