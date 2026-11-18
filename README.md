# Sistemas dinámicos en Quarto

Haz doble clic en **Presentar.cmd** y conserva abierta la terminal durante la exposición. El lanzador regenera las diapositivas y abre la presentación en el navegador con Python disponible en tu PC.

Cada uno de los cinco apartados tiene una diapositiva con la celda original completa, una explicación y el botón **▶ Ejecutar código**. Cada clic ejecuta la celda con sus importaciones en un entorno nuevo y abre su salida. En 1.1 también se generan las dos gráficas. Avanza con la flecha derecha o regresa al código con la izquierda.

También puedes abrir `presentacion.html` directamente y pulsar **Ver salida guardada** sin conexión. En el HTML abierto directamente y en la vista previa de Quarto, **Ejecutar código** usa Python en el navegador y requiere conexión para cargar sus bibliotecas. Con **Presentar.cmd**, la ejecución usa el Python instalado en esta PC. Para editar, modifica `presentacion.qmd` y vuelve a iniciar el lanzador.

## Durante la exposición

Usa las flechas para avanzar o retroceder, **F** para pantalla completa y **S** para abrir las notas del presentador en otra ventana. Permite la ventana emergente si el navegador la bloquea. Para presentar con dos pantallas, proyecta la ventana de las diapositivas y conserva las notas en tu monitor.

## Ejecución desde PowerShell

Abre una terminal en esta carpeta y ejecuta:

~~~powershell
quarto preview presentacion.qmd
~~~

Guarda los cambios para actualizar la vista previa. Usa Ctrl+C para detenerla. Para regenerar el HTML y terminar, ejecuta `quarto render`. Las celdas de Python se ejecutan al renderizar. Esta PC tiene Quarto y un kernel de Jupyter con NumPy, SciPy, SymPy y Matplotlib. Puedes verificar el entorno con `quarto check jupyter`.

## Material de la exposición

- Notebook `SD_Variaciones_Control_PD.ipynb`, apartados 0.6, 0.7, 0.8, 0.9 y 1.1.
- Miguel Flores, `Sistemas_dinamicos_variaciones_control_PD.pdf`, diapositivas 13–18 y 22–23.

## Referencias para la presentación

- Quarto. [Presentaciones](https://quarto.org/docs/presentations/), [Revealjs](https://quarto.org/docs/presentations/revealjs/) y [quarto preview](https://quarto.org/docs/cli/preview.html).
- Emil Hvitfeldt. [Slidecrafting](https://slidecrafting-book.com/) y [Workshop Slidecrafting](https://github.com/EmilHvitfeldt/workshop-slidecrafting).
