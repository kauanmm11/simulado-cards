// Menu abrie e fechar
const menu = document.querySelector("#menu-toggle");

if (localStorage.getItem("menuAberto") === "true") {
  menu.checked = true;
}

menu.addEventListener("change", () => {
  localStorage.setItem("menuAberto", menu.checked);
});

// ativar anotacoes, cards e questoes --> em materia
const links = document.querySelectorAll("nav button");
const conteudos = document.querySelectorAll(".conteudo");

function ativarAba(link) {
  links.forEach((item) => {
    item.classList.remove("ativo");
  });

  conteudos.forEach((item) => {
    item.classList.remove("ativo");
  });

  link.classList.add("ativo");

  const id = link.dataset.aba;

  const conteudo = document.getElementById(id);

  if (conteudo) {
    conteudo.classList.add("ativo");
  }
}

links.forEach((link) => {
  link.addEventListener("click", () => {
    ativarAba(link);

    // Coloca o ID da aba na URL
    window.location.hash = link.dataset.aba;
  });
});

function carregarAbaPelaURL() {
  const hash = window.location.hash;

  if (!hash) {
    return;
  }

  const nomeAba = hash.substring(1);

  const link = document.querySelector(`[data-aba="${nomeAba}"]`);

  if (link) {
    ativarAba(link);
  }
}
carregarAbaPelaURL();

// filtragem no anotacoes
const campoBusca = document.querySelector("#buscar-materia");
const filtroMateria = document.querySelector("#filtro-materia");
const cards = document.querySelectorAll(".card-conector");

function filtrar() {
  const pesquisa = campoBusca.value.toLowerCase().trim();
  const materiaSelecionada = filtroMateria.value.toLowerCase().trim();

  cards.forEach((card) => {
    const titulo = card.dataset.titulo.toLowerCase();
    const conteudo = card.dataset.conteudo.toLowerCase();
    const tags = card.dataset.tags.toLowerCase();

    const materia = card.dataset.materia.toLowerCase();

    const encontrouPesquisa =
      titulo.includes(pesquisa) ||
      conteudo.includes(pesquisa) ||
      tags.includes(pesquisa);

    const encontrouMateria =
      materiaSelecionada === "" || materia === materiaSelecionada;

    if (encontrouPesquisa && encontrouMateria) {
      card.classList.remove("oculto");
    } else {
      card.classList.add("oculto");
    }
  });
}

campoBusca.addEventListener("input", filtrar);

filtroMateria.addEventListener("change", filtrar);
