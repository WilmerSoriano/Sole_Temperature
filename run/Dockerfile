# Start from a small Linux image that already has Python 3.11 installed
FROM python:3.11-slim

# Install system dependencies for PyQt GUI
   #  Package:	                What it does:
   #  libgl1	                OpenGL rendering
   #  libxkbcommon-x11-0	    keyboard input
   #  libxcb-*	                window system communication
   #  qtbase5-dev	             Qt runtime

RUN apt-get update && apt-get install -y \
    libgl1 \
    libxkbcommon-x11-0 \
    libxcb-xinerama0 \
    libxcb-cursor0 \
    qtbase5-dev \
    && rm -rf /var/lib/apt/lists/*
    # ^ Cleans cached package lists => reduces image size.
WORKDIR /app

   # 1st. move requirements.txt into container
   # 2nd. install Python libraries

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy my code
COPY . .

# Allow GUI forwarding (WSLg), because windows... they like it displayed at :0 specefically ...
ENV DISPLAY=:0

CMD ["python", "src/app.py"]
