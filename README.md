# Construire une API de calcul analytics avec FastAPI + TimeSeries Potgres

## Docker

-   `docker build -t analytics-api -f Dockerfile .`
-   `docker run analytics-api`

becomes

-   `docker compose up --watch`
-   `docker compose down` or `docker compose down -v` (to remove volumes)
-   `docker compose run app /bin/bash` or `docker compose run app /bin/bash`
-   `uvicorn main:app --host 0.0.0.0 --port 8002 --reload`
