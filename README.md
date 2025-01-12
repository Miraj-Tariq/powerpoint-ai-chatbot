# PowerPoint AI ChatBot

## Overview
PowerPoint AI ChatBot is a full-stack application designed to simplify PowerPoint slide creation and management using AI-driven commands and intuitive user interfaces. The project is divided into two main parts:

1. **Backend**: Built using Python and FastAPI to provide REST APIs for AI-powered PowerPoint slide manipulation. ⚙️
2. **Frontend**: A React-based PowerPoint add-in that offers a seamless user experience for managing and generating slides directly within PowerPoint. 🖥️

This document provides an overview of the project and references the individual README files for the backend and frontend components.

## Table of Contents
- [Overview](#overview) 📄
- [Tech Stack](#tech-stack) 💻
- [Features](#features) 🌟
- [Setup and Installation](#setup-and-installation) 🛠️
- [Scripts](#scripts) 📝
- [References](#references) 🔗

## Tech Stack
### Backend
- **Programming Language:** Python 🐍
- **Framework:** FastAPI 🌐
- **AI Integration:** Azure OpenAI 🤖
- **Key Libraries:**
  - python-pptx 🖼️
  - uvicorn 🚀
  - openai 🧠

### Frontend
- **Framework:** React ⚛️
- **UI Library:** Material-UI 🎨
- **Languages:** JavaScript, TypeScript 🛠️
- **API Calls:** Axios 🌐
- **PowerPoint Integration:** Office.js 🏢

## Features
### Backend
- REST APIs for slide creation and modification. 🛠️
- Integration with Azure OpenAI for natural language processing. 🤖
- Support for text, shapes, and image manipulations. 🎨
- Base64 encoding for PowerPoint file handling. 🗂️

### Frontend
- Interactive slide selection and management. 🖼️
- AI-powered command input for slide customization. ✍️
- Tab-based navigation and intuitive UI. 🗂️
- Seamless PowerPoint integration. 📊

## Setup and Installation
### Prerequisites
- **Node.js (v16.x or higher)** and npm for the frontend. 🔧
- **Python 3.12** and virtual environment tools for the backend. 🐍
- PowerPoint (Office 365 or 2019) with support for add-ins. 📄

### Steps
1. **Clone the repository**: 📥
   ```bash
   git clone https://github.com/Miraj-Tariq/powerpoint-ai-chatbot.git
   ```
2. **Set up the backend**: ⚙️
   ```bash
   npm run build.be
   npm run start.be
   ```
3. **Set up the frontend**: 🖥️
   ```bash
   npm run install.fe
   npm run start.fe
   ```

## Scripts
The `package.json` file defines useful scripts for managing the project:

- **Backend:**
  - `npm run build.be`: Installs Python dependencies and sets up a virtual environment. 🛠️
  - `npm run start.be`: Starts the backend development server. 🚀

- **Frontend:**
  - `npm run install.fe`: Installs dependencies for the frontend. 📦
  - `npm run start.fe`: Starts the frontend development server. 🖥️
  - `npm run build.fe`: Builds the frontend for production. 📦

## References
For more detailed information, refer to the individual README files:

- [Backend README](backend/README.md) 📄
- [Frontend README](frontend/README.md) 📄

## Data Flow
1. Frontend sends query to Backend
   - **IMPROVEMENT:** Frontend UI can be improved by adding categorizing user prompts into some basic and general actions like Insert, Update, Delete, Rewrite, Resize, Reformat etc. Moreover, content enhancement should be segregated from the slide formatting i.e. first content enhancement should be done and validated by user and then enhanced content should be formatted on slide.
2. Backend improve user prompt, adds slide context in prompt before sending it to ChatGPT AI for processing
   - **IMPROVEMENT:** Assistant feature can be used in ChatGPT API to improve the results further. Furthermore, ChatGPT can also be provided information in terms of slide matrix i.e. telling GPT which areas of the slide are empty and hence can be utilized. To improve results further, trained GPT model should be used which has the full knowledge and training for working with Powerpoint presentations.
3. OpenAI converts natural language to structured JSON
   - **IMPROVEMENT:** The structured JSON output format can be enhanced and improved further but for current use cases it is already quite generic and complete.
4. Python-PPTX library converts JSON to PowerPoint actions
   - **IMPROVEMENT:** A lot more icons, bullet points, fonts can be added to improve the formatting. Moreover, audit database or record should be maintained to revert back and forth to different state or versions.
5. Python-PPTX executes actions on local PowerPoint file
6. Modified PowerPoint file is saved locally
7. Backend encodes PowerPoint file to base64
8. Base64-encoded file is returned to Frontend