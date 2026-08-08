const steps = [
  ["01 · INPUT", "Frontend mengumpulkan data", "HTML menyediakan dua field. JavaScript boleh memberi feedback awal sebelum data dikirim."],
  ["02 · REQUEST", "HTTP membawa pesan", "Browser mengirim POST /transactions beserta nama dan total belanja. HTTP membawa data, bukan menyimpannya."],
  ["03 · PROCESS", "Backend mengontrol data", "Flask memilih route. Python membersihkan input, memvalidasi aturan, lalu menentukan query yang aman."],
  ["04 · QUERY", "Connector menjadi penerjemah", "mysql-connector-python membuka connection dan mengirim SQL serta parameter secara terpisah."],
  ["05 · PERSIST", "MySQL menyimpan row", "Database memeriksa schema dan constraint, memberi primary key, lalu commit membuat perubahan permanent."],
  ["06 · RESULT", "Data pulang sebagai result", "SELECT/fetch mengubah row MySQL menjadi dictionary Python yang dapat diproses backend."],
  ["07 · OUTPUT", "User melihat hasil", "Flask merender HTML atau mengirim JSON. Browser menampilkan row baru pada table."],
];

let current = 0;
const items = [...document.querySelectorAll("[data-step]")];
const next = document.querySelector("#next");
const reset = document.querySelector("#reset");

function paint() {
  items.forEach((item) => {
    const step = Number(item.dataset.step);
    item.classList.toggle("active", step === current);
    item.classList.toggle("done", step < current);
  });

  if (current === 0) {
    document.querySelector("#step-label").textContent = "SIAP MULAI";
    document.querySelector("#step-title").textContent = "Data tidak teleport.";
    document.querySelector("#step-description").textContent = "Klik tombol untuk melihat siapa melakukan apa pada setiap langkah.";
    next.innerHTML = "Mulai perjalanan data <span>→</span>";
    return;
  }

  const [label, title, description] = steps[current - 1];
  document.querySelector("#step-label").textContent = label;
  document.querySelector("#step-title").textContent = title;
  document.querySelector("#step-description").textContent = description;
  next.innerHTML = current === steps.length ? "Ulangi perjalanan <span>↻</span>" : "Langkah berikutnya <span>→</span>";
}

next.addEventListener("click", () => {
  current = current >= steps.length ? 1 : current + 1;
  paint();
});
reset.addEventListener("click", () => { current = 0; paint(); });
items.forEach((item) => item.addEventListener("click", () => { current = Number(item.dataset.step); paint(); }));
paint();
