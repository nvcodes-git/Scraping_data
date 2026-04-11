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

---

# Task 2 — RAWG API Analysis

This task consumes the [RAWG API](https://rawg.io) to extract, analyze, and compare video game data using Python inside a Jupyter Notebook.

## What does the project do?

The notebook (`api/tarea_rawg_api.ipynb`) queries the RAWG video game database API to:

- **Part A — General Exploration**: retrieve the total number of games registered in RAWG.
- **Part B — Category Analysis**: find the top 5 highest-rated games of all time (by Metacritic score) and the 10 best games available on Steam.
- **Part C — Comparisons**: compare top games across platforms (PC vs PS5), build comparison tables for famous games, analyze average ratings by genre, compare best games across different release years, and export the top 20 games of all time to a CSV file.
- **Part D — Insights & Conclusions**: personal analysis and conclusions drawn from the data.

## How to install the dependencies

Run the following command:

```
pip install requests pandas jupyter
```

You will also need a RAWG API key:

1. Go to [https://rawg.io](https://rawg.io) and create an account.
2. Visit [https://rawg.io/apidocs](https://rawg.io/apidocs) and click **Get API Key**.
3. Store the key in a local variable inside the notebook — do **not** upload it to GitHub.

## How to run the script

Open the notebook with Jupyter:

```
jupyter notebook api/tarea_rawg_api.ipynb
```

Run all cells in order. Each section contains Markdown cells explaining the steps and code cells with visible output.

## What does the output contain?

- **`api/output/top20_rawg.csv`** — CSV file with the top 20 games of all time, containing the columns: `name`, `rating`, `metacritic`, `release_date`, `main_genre`.
