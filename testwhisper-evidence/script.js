// ======================================================
// BASE DE DADOS
// ======================================================

let configs = [];
let ativaId = null;
let evidencias = {};

function byId(id) { return document.getElementById(id); }

function salvarLocal() {
    localStorage.setItem("configs", JSON.stringify(configs));
    localStorage.setItem("ativaId", ativaId);
    localStorage.setItem("evidencias", JSON.stringify(evidencias));
}

function carregarLocal() {
    configs = JSON.parse(localStorage.getItem("configs") || "[]");
    ativaId = localStorage.getItem("ativaId");
    evidencias = JSON.parse(localStorage.getItem("evidencias") || "{}");
}

// ======================================================
// INDICADOR
// ======================================================

function atualizarSecaoAtivaInfo() {
    const box = byId("secaoAtivaInfo");
    const btn = byId("capturarBtn");

    const cfg = configs.find(c => c.id === ativaId);
    if (!cfg) {
        box.textContent = "Nenhuma seção ativa";
        btn.textContent = "Capturar Screenshot";
        return;
    }

    box.textContent = `Seção ativa: ${cfg.tarefa || "(sem nome)"}`;
    btn.textContent = `Capturar Screenshot (Seção: ${cfg.tarefa || "?"})`;
}

// ======================================================
// NOVA CONFIG
// ======================================================

function novaConfigObj() {
    return {
        id: Date.now().toString(),
        tarefa: byId("tarefa").value,
        executor: byId("executor").value,
        ambiente: byId("ambiente").value,
        navegador: byId("navegador").value,
        so: byId("so").value,
        sprint: byId("sprint").value,
        tags: byId("tags").value,
        pre: byId("pre").value,
        cenario: byId("cenario").value
    };
}

function limparFormulario() {
    ["tarefa","executor","ambiente","navegador","so","sprint","tags","pre","cenario"]
        .forEach(id => byId(id).value = "");
}

byId("btnSalvarCfg").onclick = () => {
    const obj = novaConfigObj();
    configs.push(obj);
    ativaId = obj.id;
    evidencias[obj.id] = [];
    salvarLocal();
    atualizarSecaoAtivaInfo();
    alert("Configuração salva e definida como ativa!");
};

byId("btnCancelar").onclick = limparFormulario;
byId("btnLimpar").onclick = limparFormulario;

byId("btnNovaCfg").onclick = () => {
    ativaId = null;
    limparFormulario();
    atualizarSecaoAtivaInfo();
    alert("Nova configuração iniciada.");
};

// ======================================================
// CAPTURA
// ======================================================

function capturarTela() {
    if (!ativaId) return alert("Nenhuma configuração ativa!");

    html2canvas(document.body).then(canvas => {
        evidencias[ativaId].push({
            id: Date.now(),
            screenshot: canvas.toDataURL("image/png"),
            timestamp: new Date().toLocaleString(),
            origem: "captura"
        });

        salvarLocal();
        atualizarGaleria();
        alert("Screenshot capturado!");
    });
}

byId("capturarBtn").onclick = capturarTela;

// ======================================================
// IMPORTAR IMAGENS
// ======================================================

byId("importarBtn").onclick = () => {
    if (!ativaId) return alert("Nenhuma configuração ativa.");

    const input = document.createElement("input");
    input.type = "file";
    input.accept = "image/*";

    input.onchange = e => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.onload = () => {
            evidencias[ativaId].push({
                id: Date.now(),
                screenshot: reader.result,
                timestamp: new Date().toLocaleString(),
                origem: "upload"
            });
            salvarLocal();
            atualizarGaleria();
        };
        reader.readAsDataURL(file);
    };

    input.click();
};

document.addEventListener("paste", e => {
    if (!ativaId) return;

    for (const item of e.clipboardData.items) {
        if (!item.type.startsWith("image")) continue;
        const blob = item.getAsFile();
        const reader = new FileReader();
        reader.onload = () => {
            evidencias[ativaId].push({
                id: Date.now(),
                screenshot: reader.result,
                timestamp: new Date().toLocaleString(),
                origem: "clipboard"
            });
            salvarLocal();
            atualizarGaleria();
        };
        reader.readAsDataURL(blob);
    }
});

// ======================================================
// GALERIA
// ======================================================

function atualizarGaleria() {
    const g = byId("listaEvidencias");
    g.innerHTML = "";

    if (!ativaId || !evidencias[ativaId]) return;

    evidencias[ativaId].forEach(ev => {
        const card = document.createElement("div");
        card.className = "card-evidencia";

        card.innerHTML = `
            <img src="${ev.screenshot}" class="thumb">
            <p><strong>Data:</strong> ${ev.timestamp}</p>
            <p><strong>Origem:</strong> ${ev.origem}</p>
        `;

        g.appendChild(card);
    });
}

// ======================================================
// NORMALIZAR IMAGEM
// ======================================================

async function loadImg(dataUrl) {
    return new Promise(resolve => {
        const img = new Image();
        img.onload = () => resolve(img);
        img.src = dataUrl;
    });
}

// ======================================================
// PDF — A4 LANDSCAPE — 2 EVIDÊNCIAS POR PÁGINA (LADO A LADO)
// ======================================================

byId("gerarPdf").onclick = async () => {

    if (!configs.length)
        return alert("Nenhuma configuração salva.");

    const { jsPDF } = window.jspdf;
    const pdf = new jsPDF({
        orientation: "landscape",
        unit: "mm",
        format: "a4"
    });

    let firstSection = true;

    for (const cfg of configs) {
        const lista = evidencias[cfg.id] || [];

        // Página da seção
        if (!firstSection) pdf.addPage();
        firstSection = false;

        pdf.setFontSize(20);
        pdf.text(cfg.tarefa || "Sem título", 10, 20);

        pdf.setFontSize(12);
        pdf.text(`Executor: ${cfg.executor}`, 10, 35);
        pdf.text(`Ambiente: ${cfg.ambiente}`, 10, 42);
        pdf.text(`Navegador: ${cfg.navegador}`, 10, 49);
        pdf.text(`SO: ${cfg.so}`, 10, 56);
        pdf.text(`Sprint: ${cfg.sprint}`, 10, 63);
        pdf.text(`Tags: ${cfg.tags}`, 10, 70);

        pdf.text("Pré-requisitos:", 10, 85);
        pdf.text(cfg.pre || "-", 10, 92, { maxWidth: 260 });

        pdf.text("Cenário:", 10, 110);
        pdf.text(cfg.cenario || "-", 10, 117, { maxWidth: 260 });

        pdf.line(10, 130, 287, 130);

        pdf.setFontSize(15);
        pdf.text("Evidências:", 10, 145);

        // --------------------------------------------------------
        //             2 evidências por página (lado a lado)
        // --------------------------------------------------------

        for (let i = 0; i < lista.length; i += 2) {
            pdf.addPage();

            const ev1 = lista[i];
            const ev2 = lista[i + 1];

            // posição da esquerda
            if (ev1) {
                const img1 = await loadImg(ev1.screenshot);
                pdf.setFontSize(14);
                pdf.text(`Evidência #${i + 1}`, 10, 20);
                pdf.addImage(img1, "PNG", 10, 30, 130, 130);
            }

            // posição da direita
            if (ev2) {
                const img2 = await loadImg(ev2.screenshot);
                pdf.setFontSize(14);
                pdf.text(`Evidência #${i + 2}`, 150, 20);
                pdf.addImage(img2, "PNG", 150, 30, 130, 130);
            }
        }
    }

    pdf.save(`evidencias_${Date.now()}.pdf`);
};

// ======================================================
// JSON
// ======================================================

byId("gerarJson").onclick = () => {
    const blob = new Blob([JSON.stringify({ configs, evidencias }, null, 2)], {
        type: "application/json"
    });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `evidencias_${Date.now()}.json`;
    a.click();
};

// ======================================================
// INIT
// ======================================================

function init() {
    carregarLocal();
    atualizarSecaoAtivaInfo();
    atualizarGaleria();
}

init();

// ======================================================
// BOTÃO LIMPAR TUDO
// ======================================================

byId("btnLimparTudo").onclick = () => {
    if (!confirm("Deseja realmente limpar tudo?")) return;
    configs = [];
    evidencias = {};
    ativaId = null;
    salvarLocal();
    atualizarSecaoAtivaInfo();
    atualizarGaleria();
    alert("Dados apagados.");
};
