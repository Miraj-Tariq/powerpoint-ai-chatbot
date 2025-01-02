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

