FROM python:3.9-slim-buster

ENV DISPLAY=:99
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    libgbm1 \
    xvfb \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/chrome.zip https://storage.googleapis.com/chrome-for-testing-public/135.0.7000.0/linux64/chrome-linux64.zip && \
    unzip /tmp/chrome.zip -d /opt/ && \
    mv /opt/chrome-linux64 /opt/chrome && \
    ln -s /opt/chrome/chrome /usr/bin/google-chrome && \
    rm /tmp/chrome.zip

RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/135.0.7000.0/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver.zip -d /opt/chromedriver && \
    mv /opt/chromedriver/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip /opt/chromedriver

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["sh", "-c", "Xvfb :99 -screen 0 1280x1024x16 & python main.py"]