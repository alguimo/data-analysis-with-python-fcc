# Data Analysis with Python

Trabajo completado del curso [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python)
de freeCodeCamp, con los cinco proyectos agrupados en un unico repositorio.

Cada proyecto es una carpeta independiente con su propio `requirements.txt` y sus
propios tests del curso (`test_module.py`).

**Stack:** pandas, numpy, scipy, matplotlib, seaborn.

## Proyectos

| Proyecto | Que demuestra |
| --- | --- |
| [Demographic-Data-Analyzer](Demographic-Data-Analyzer/) | Analisis exploratorio sobre 32.563 registros del censo: distribucion categorica, filtros booleanos combinados, agregacion por grupo y maximo de un cociente entre dos `groupby` |
| [medical-data-visualizer](medical-data-visualizer/) | Feature engineering sobre 70.001 examenes: derivar el IMC, recodificar categoricas, reshape wide-to-long con `melt`, y matriz de correlacion con mascara triangular |
| [Page-View-Time-Series-Visualizer](Page-View-Time-Series-Visualizer/) | Series temporales: parseo de fechas como indice, filtrado de outliers por cuartiles, agregacion mensual con `groupby().unstack()` y comparacion de distribuciones con box plots |
| [sea-level-predictor](sea-level-predictor/) | Regresion lineal con `scipy.stats.linregress` y proyeccion de la tendencia hasta 2050, con una segunda regresion sobre el subconjunto posterior a 2000 para comparar pendientes |
| [Mean-Variance-Standard-Deviation-Calculator](Mean-Variance-Standard-Deviation-Calculator/) | Calculo estadistico con numpy y agregacion consciente del eje sobre una matriz 3x3, con validacion de entrada y tipos nativos en la salida |

## Uso

Cada proyecto se ejecuta por separado, desde dentro de su carpeta:

```bash
cd sea-level-predictor
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py
python -m unittest test_module.py
```

Los `requirements.txt` fijan las versiones de dependencias que usaba el curso en su
momento, algunas de 2020. En Python actuales pueden pedir `pip install --upgrade` o una
version mas nueva de numpy, pandas o seaborn.

## Nota sobre los datos

Los CSV que usan los tests vienen del repositorio del curso y se versionan aqui para
que todo sea reproducible sin descargar nada:

- `adult.data.csv` (3.5 MB, 32.563 registros)
- `medical_examination.csv` (2.9 MB, 70.001 registros)
- `fcc-forum-pageviews.csv` (22 KB, 1.305 registros)
- `epa-sea-level.csv` (5.9 KB, 134 registros)
