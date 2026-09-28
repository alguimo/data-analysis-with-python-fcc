# Data Analysis with Python

Soluciones de los proyectos del curso [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python)
de freeCodeCamp, agrupados en un único repositorio.

Cada proyecto es una carpeta independiente con su propio `requirements.txt` y sus
propios tests de freeCodeCamp (`test_module.py`).

## Proyectos

| Proyecto | Descripcion | Dependencias | Repositorio original |
| --- | --- | --- | --- |
| [Demographic-Data-Analyzer](Demographic-Data-Analyzer/) | Analisis del censo de adultos: distribucion por raza, edad media, porcentaje de-education, pais con mas ingresos | pandas | [alguimo/Demographic-Data-Analyzer](https://github.com/alguimo/Demographic-Data-Analyzer) |
| [medical-data-visualizer](medical-data-visualizer/) | Visualizaciones de datos medicos: masa corporal, colesterol, glucosa y correlaciones | pandas, seaborn | [alguimo/medical-data-visualizer](https://github.com/alguimo/medical-data-visualizer) |
| [Page-View-Time-Series-Visualizer](Page-View-Time-Series-Visualizer/) | Series temporales de visitas al foro de freeCodeCamp, con limpieza de outliers y dos box plots | pandas, seaborn, matplotlib | [alguimo/Page-View-Time-Series-Visualizer](https://github.com/alguimo/Page-View-Time-Series-Visualizer) |
| [sea-level-predictor](sea-level-predictor/) | Prediccion del nivel del mar con regresion lineal sobre datos de la EPA | pandas, numpy, scipy, matplotlib | [alguimo/sea-level-predictor](https://github.com/alguimo/sea-level-predictor) |
| [Mean-Variance-Standard-Deviation-Calculator](Mean-Variance-Standard-Deviation-Calculator/) | Calculo de media, varianza y desviacion estandar de una lista de numeros | numpy | [alguimo/Mean-Variance-Standard-Deviation-Calculator](https://github.com/alguimo/Mean-Variance-Standard-Deviation-Calculator) |

## Estado de los tests

Resultado de `python -m unittest test_module.py` en cada proyecto, verificado contra
Python 3.9 con `pandas==1.5.3`, `numpy==1.24.4`, `scipy==1.10.1`, `seaborn==0.13.2`:

| Proyecto | Resultado | Detalle |
| --- | --- | --- |
| Demographic-Data-Analyzer | 10/10 | pasa |
| sea-level-predictor | 4/4 | pasa |
| Page-View-Time-Series-Visualizer | 10/11 | falla `test_box_plot_2_labels`: el box plot 2 no expone las etiquetas de los meses |
| medical-data-visualizer | 1/4 | 2 errores: el test espera un `Axes` y el modulo devuelve un `ndarray`. 1 fallo: el heat map imprime `-0.0` en vez de `0.0` |
| Mean-Variance-Standard-Deviation-Calculator | 0/3 | **sin resolver**: `mean_var_std.py` conserva el boilerplate de freeCodeCamp y `calculate` no esta implementada (`NameError: name 'calculations' is not defined`) |

Los tres ultimos fallan igual en los repositorios individuales de origen, asi que son
pendientes preexistentes y no reelaciones de este repositorio. El heat map de
medical-data-visualizer es el caso tipico de un problema de version: las versiones
modernas de matplotlib formatean el cero con signo.

## Uso

Cada proyecto se ejecuta de forma independiente, desde dentro de su carpeta:

```bash
cd sea-level-predictor
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py
python -m unittest test_module.py
```

Los dos CSV grandes que usan los tests se versionan en este repositorio
(`adult.data.csv`, `medical_examination.csv`) para que se puedan ejecutar sin
descargar nada.

## Nota sobre los datos

`adult.data.csv` (3.5 MB) y `medical_examination.csv` (2.9 MB) provienen del
repositorio del curso de freeCodeCamp. Se incluyen aqui para que los tests sean
reproducibles offline.
