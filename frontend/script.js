const form = document.getElementById("form-busqueda");
const resultados = document.getElementById("resultados");
const fidelizacion = document.getElementById("fidelizacion");

form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const tipo = document.getElementById("tipo_documento").value;
    const numero = document.getElementById("numero_documento").value;

    const url = `http://127.0.0.1:8000/api/clientes/?numero_documento=${numero}`;

    const respuesta = await fetch(url);
    if (!respuesta.ok) {
        alert("Cliente no encontrado.");
        return;
    }

    const data = await respuesta.json();

    // Llenar datos en HTML
    document.getElementById("res-nombre").textContent = data.nombres;
    document.getElementById("res-apellido").textContent = data.apellidos;
    document.getElementById("res-correo").textContent = data.correo;
    document.getElementById("res-telefono").textContent = data.telefono;

    // Mostrar total del último mes (si lo quieres traer desde la API avanzada)
    document.getElementById("res-total").textContent = data.total_compras_ultimo_mes || "No disponible";

    resultados.style.display = "block";

    // Verificar fidelización
    if (data.total_compras_ultimo_mes >= 5000000) {
        fidelizacion.style.display = "block";
    } else {
        fidelizacion.style.display = "none";
    }

    // Botón exportar
    document.getElementById("btn-exportar").onclick = () => {
        window.location.href =
            `http://127.0.0.1:8000/api/exportar-cliente/?numero_documento=${numero}&formato=csv`;
    };

    document.getElementById("btn-reporte-fidelizacion").onclick = () => {
        window.location.href = "http://127.0.0.1:8000/api/reporte-fidelizacion/";
    };
});
