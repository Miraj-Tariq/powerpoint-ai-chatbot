# Powerpoint AI ChatBot - Backend

## Description
This backend application serves as the foundation for the "PowerPoint AI ChatBot" frontend project, providing a comprehensive suite of REST APIs to support its functionality. It is designed to handle user interactions, process AI-powered queries, and manage the seamless integration of data and services required by the chatbot interface.

## Table of Contents
- [About the Project](#about-the-project) 📄
- [Features](#features) 🌟
- [Tech Stack](#tech-stack) 💻
- [Installation](#installation) 🛠️
- [Usage](#usage) 🚀
- [API Documentation](#api-documentation) 📖
- [Project Structure](#project-structure) 🗂️
- [Environment Variables](#environment-variables) 🔑

## About the Project
This project acts as the core backend for processing and executing user instructions received from the PowerPoint add-in frontend. It translates user prompts into actionable commands to create, update, or enhance PowerPoint presentations. By leveraging the python-pptx library, it ensures seamless integration with PowerPoint, enabling dynamic and efficient manipulation of slides, layouts, and content based on user input. This system is designed to streamline the workflow of generating presentations, bridging the gap between user intentions and tangible results.

## Features
- REST APIs for creating, updating, and managing PowerPoint presentations. ⚙️
- Integration with Azure OpenAI for AI-driven content generation and user instruction translation. 🤖
- Dynamic shape and text management within slides (e.g., text boxes, images, icons). 🎨
- Base64 encoding for PowerPoint file handling. 🗂️
- User-driven customizations, such as font styling, layout adjustments, and content generation. ✍️

## Tech Stack
- **Programming Language:** Python 🐍
- **Framework:** FastAPI 🌐
- **AI Integration:** Azure OpenAI 🤖
- **Libraries:**
  - python-pptx (1.0.2) for PowerPoint manipulations 🖼️
  - python-dotenv (1.0.1) for environment variable management 📦
  - uvicorn (0.32.1) as ASGI server 🚀
  - flake8 (7.1.1) for code linting ✅
  - openai (1.55.3) for OpenAI API integration 🧠
  
## Installation
### Prerequisites
- Python 3.12 🐍
- Virtual environment tool (e.g., venv or virtualenv) 🛠️

### Steps

1. Create and activate a virtual environment: 🖥️
   - **On Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Install dependencies: 📦
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and populate it with the required [environment variables](#environment-variables). 📝

## Usage
1. Start the development server: 🚀
   ```bash
   uvicorn main:app --reload
   ```

2. Access the FastAPI documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). 📖

## API Documentation
The project provides an interactive API documentation using FastAPI's built-in Swagger UI. Visit:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 🌐

## Project Structure
```
app/
    main.py
    constants.py
    routes/
        ppt.py
    services/
        ppt/
            actions.py
            context.py
    utils/
        openai.py
        prompt.py
    prompts/
        actions.py
        actions_update.py
    schemas/
        actions.py
    config/
        settings.py
```

## Environment Variables
The following environment variables need to be configured in a `.env` file:

- `LOCAL_PPT_FILENAME`: Local filename for storing PowerPoint presentations 🖼️
- `AZURE_OPENAI_KEY`: API key for Azure OpenAI 🔑
- `AZURE_OPENAI_ENDPOINT`: Endpoint for Azure OpenAI 🌐
- `AZURE_API_VERSION`: API version for Azure OpenAI 🗂️
- `GPT_MODEL`: GPT model to be used 🤖

