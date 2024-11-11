window.onload = function() {
    const modal = document.getElementById('welcomeModal');
    const closeBtn = document.querySelector('.close-btn');
    modal.style.display = 'block';
    closeBtn.onclick = function() {
        modal.style.display = 'none';
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    };
};

window.onload = function() {
    const form = document.getElementById('feedbackForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Evita el envío inmediato del formulario

        // Captura los valores seleccionados
        const selectedPageLike = document.querySelector('input[name="Te_gusta_la_pagina"]:checked');
        const selectedGenre = document.querySelector('input[name="Genero"]:checked');
        const selectedFrequency = document.querySelector('input[name="Frecuencia"]:checked');
        const selectedPlatform = document.querySelector('input[name="Plataforma"]:checked');
        const selectedLearnMore = document.querySelector('input[name="Aprender"]:checked');

        // Verifica que todos los campos están seleccionados
        if (selectedPageLike && selectedGenre && selectedFrequency && selectedPlatform && selectedLearnMore) {
            // Genera las respuestas para el archivo de texto
            const responses = `Te gusta la página: ${selectedPageLike.value}\n` +
                              `Género: ${selectedGenre.value}\n` +
                              `Frecuencia: ${selectedFrequency.value}\n` +
                              `Plataforma: ${selectedPlatform.value}\n` +
                              `Aprender más: ${selectedLearnMore.value}\n`;

            // Crea y descarga el archivo de texto
            const blob = new Blob([responses], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'respuestas.txt'; 
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a); 
            URL.revokeObjectURL(url);

            // Asigna los valores seleccionados a los campos ocultos
            document.getElementById('hiddenTeGustaLaPagina').value = selectedPageLike.value;
            document.getElementById('hiddenGenero').value = selectedGenre.value;
            document.getElementById('hiddenFrecuencia').value = selectedFrequency.value;
            document.getElementById('hiddenPlataforma').value = selectedPlatform.value;
            document.getElementById('hiddenAprender').value = selectedLearnMore.value;

            // Envía el formulario
            form.submit(); // Ahora el formulario se envía con los valores correctamente asignados
        } else {
            alert("Por favor responde todas las preguntas antes de enviar.");
        }
    });
};


