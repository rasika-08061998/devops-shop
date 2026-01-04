# 1️⃣ Base image: lightweight Python
FROM python:3.12-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy dependency file first (for caching)
COPY requirements.txt .

# 4️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy application code
COPY app.py .
COPY static ./static

# 6️⃣ Expose application port
EXPOSE 5000

# 7️⃣ Start Flask app
CMD ["python", "app.py"]

