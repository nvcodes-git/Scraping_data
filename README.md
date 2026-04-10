# Scraping Data
This project extracts the admission exam results from the UNMSM website using Python. The script enters the main results page, collects the links of all careers, visits each career page, and gathers the information of all applicants. Finally, it consolidates all the extracted data into a single Excel file called "resultados_sanmarcos.xlsx".

## How to install the dependencies

Run the following command:

```
pip install pandas selenium openpyxl
```

You will also need to install the system chromedriver. We use the system-installed chromedriver (via apt) instead of `webdriver-manager` because this project runs on Linux with Chromium installed as a snap package. The snap version of Chromium has sandbox restrictions that prevent `webdriver-manager` from launching it correctly. Installing chromedriver via apt avoids this conflict:

```
sudo apt install chromium-driver
```

## How to run the script

```
python scraper.py
```

The script runs in headless mode (no browser window) and prints progress for each career as it scrapes.

## What does the output contain?

The output is an Excel file located at `output/resultados_sanmarcos.xlsx`. It contains one sheet with all applicants from every career, with the following columns:

- **Código**: applicant ID
- **Apellidos y Nombres**: full name
- **Escuela**: career/school they applied to
- **Puntaje**: exam score
- **Mérito E.P**: merit ranking within the career
- **Observación**: result status — rows where the applicant was admitted ("ALCANZÓ VACANTE") are highlighted in green
