# ---- stage 1: build CSS ----
FROM python:3.14-slim AS css
WORKDIR /build

RUN pip install --no-cache-dir pytailwindcss==0.4.2

# copy templates for tailwind to scan
COPY templates/ templates/
COPY static/css/input.css static/css/input.css

RUN tailwindcss -i static/css/input.css -o static/css/output.css --minify


# ---- stage 2: runner ----
FROM python:3.14-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# copy the minified css from the css builder
COPY --from=css /build/static/css/output.css static/css/output.css

CMD ["gunicorn", "-b", "0.0.0.0:5001", "-w", "2", "app:app"]
