# PR1-web-scraping
## Finalidad
El repositorio actual contiene la Práctica 1 (Web Scraping) de la asignatura Tipología y ciclo de vida de los datos del Máster en Ciencia de Datos de la UOC. 
## Miembros del proyecto
Los miembros del proyecto son **Ferran Valverde Parera** y **Alejandro González Barberá**.
## Versiones
El proyecto está construido con Python 3.7.11 con las siguiente librerías:
- Python: 3.7.11
- Request version:  2.27.1
- BeautifulSoup version:  4.11.1
- csv version:  1.0
- Pandas version:  1.3.5
## Contenido del repositorio
- ./data/*: csv intermedios que contienen las estadísticas de las monedas en cada momento.
- ./dataset/CoinGecko.csv: contiene las 100 mejores monedas junto a algunos atributos tomados en el momento de ejecución.
- ./dataset/coins_dataset.csv: resultado del notebook Merge_csv.ipynb.
- ./source/Merge_csv.ipynb: notebook para juntar los csv del directorio data/ en uno.
- ./source/coins_dataset.csv: resultado del notebook Merge_csv.ipynb.
- ./source/web-scraping-full.ipynb: notebook que contiene la implementación del web scraping y del guardado de los csv.
- ./source/web-scraping-test.ipynb: notebook que contiene paso a paso la implmentación del anterior.
## DOI
El dataset también se puede encontrar en el siguiente repositorio de [Zenodo](https://doi.org/10.5281/zenodo.7339630)
