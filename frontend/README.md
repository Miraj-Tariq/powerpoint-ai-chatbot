# Powerpoint AI ChatBot - Frontend

## Description
This project is a **PowerPoint Context Add-in** built with **React** and **Office.js** to manage and search slides. The add-in allows users to open a popup window, search for slides, and add them to a deck.

The application focuses on two key functionalities:

1. **Slide Selection Popup**: 🖼️ An intuitive interface that allows users to browse and select from previously created slides seamlessly.
2. **Instruction Form**: ✍️ A user-friendly text input form where users can provide instructions to transform their ideas into concrete PowerPoint actions, enabling efficient and automated slide generation.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [About the Project](#about-the-project)
3. [Features](#features)
4. [Tech Stack](#tech-stack)
5. [Getting Started](#getting-started)
6. [Installation](#installation)
7. [Usage](#usage)
8. [PowerPoint Configuration](#powerpoint-configuration)
9. [Testing the Add-in](#testing-the-add-in)
10. [Project Structure](#project-structure)
11. [Dependencies](#dependencies)
12. [Environment Variables](#environment-variables)
13. [Troubleshooting](#troubleshooting)

## Prerequisites
Make sure you have the following tools installed:

1. **Node.js (v16.x or higher)**: 🔧 [Download Node.js](https://nodejs.org/)
2. **npm (v7.x or higher)**: 📦 Comes with Node.js installation.
3. **PowerPoint (Office 365 or 2019)**: 📄 with support for add-ins.

## About the Project
This project integrates seamlessly into PowerPoint as a task pane add-in. By leveraging React and Material-UI, the application offers a visually appealing and functional user interface. Unique features like a highly interactive slide selection mechanism and customizable AI-powered commands make this project stand out. The chatbot's ability to act on user instructions to modify slides is a significant innovation.

## Features
- **Slide Search and Selection**: 🔍 Effortlessly browse and select slides through an intuitive popup interface.
- **Custom Instruction Input**: ✍️ Provide instructions in a form to automate slide transformations.
- **Tab-Based Navigation**: 🗂️ Organize slides into categories like "Recent Slides," "Most Common Files," and "Favorites."
- **Interactive Pagination**: ⏩ Easily navigate through a large number of slides.
- **Seamless PowerPoint Integration**: 📊 Operates within PowerPoint for enhanced user experience.

## Tech Stack
- **Framework**: 🖥️ React (v18.3.1)
- **UI Library**: 🎨 Material-UI
- **Languages**: 🛠️ TypeScript, JavaScript
- **Build Tool**: 🔧 React Scripts
- **API Calls**: 🌐 Axios
- **Testing**: 🧪 Jest, React Testing Library
- **State Management**: 🔄 React Context API

## Getting Started

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Install Type Definitions for Office.js (Optional for TypeScript)**:
   ```bash
   npm install --save-dev @types/office-js
   ```

3. **Set up Environment Variables**:
   `.env` file in the root of the project with the following content:

   - `HTTPS`: Set HTTPS communication True or False 🌐
   - `NODE_OPTIONS`: Setting NodeJS options e.g. --max_old_space_size=4096 🛠️ 

5. **Start the Development Server**:
   ```bash
   npm start
   ```

   The application will run on:
   ```
   https://localhost:3000
   ```

6. **Trust the Self-Signed Certificate**:
   When you start the server for the first time, you might get a security warning. Follow these steps:
   - Open https://localhost:3000 in your browser.
   - Accept the self-signed certificate.

## Installation
Follow these steps to set up the project:

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```

## Usage
1. **Enable HTTPS** for your local development server as described above.
2. Open PowerPoint and load the manifest file (`manifest.xml`) to add the custom task pane add-in.
3. Interact with the chatbot using the slide selection popup or the instruction form.

## PowerPoint Configuration
### Load the Add-in in PowerPoint

1. **Insert the Add-in in PowerPoint**:
   - Open PowerPoint.
   - Go to Insert > My Add-ins > Upload My Add-in.
   - Select the manifest.xml file.

2. **Verify the Add-in**:
   - Go to the Home tab.
   - Click the PowerPoint AI ChatBot button to open the task pane.

## Testing the Add-in
1. **Run the Add-in**:
   - Click "Search Slides" in the task pane.
   - Confirm that a popup appears asking for permission to open a new window.
   - Click "Allow".

2. **Verify the Popup**:
   - Ensure the popup displays the search bar, tabs, images grid (3 images per row), and pagination.
   - Test the "Add to Deck" button to confirm functionality.

## Project Structure
```
package.json
tsconfig.json
.env
public/
    index.html
    dialog.html
    manifest.json
    manifest.xml
src/
    components/
        Header.tsx
        MainPage.tsx
        Popup.tsx
    index.tsx
    index.css
    app.tsx
    app.css
```

## Dependencies
Key dependencies used in this project:
- **React**: ⚛️ JavaScript library for building user interfaces.
- **Material-UI**: 🎨 UI component library for React.
- **Office.js**: 🏢 Microsoft Office JavaScript API.

Install dependencies:
```bash
npm install react @mui/material @mui/icons-material
```
Install type definitions (for TypeScript):
```bash
npm install --save-dev @types/react @types/office-js
```

## Environment Variables
Ensure the following environment variables are set in the `.env` file:

- `HTTPS=true`: 🔒 Enables secure HTTPS connections for the development server.
- `NODE_OPTIONS=--max_old_space_size=4096`: 🚀 Prevents memory issues during development.

## Troubleshooting
1. **Self-Signed Certificate Issues**:
   - If the browser blocks the connection, manually trust the certificate as described above.

2. **PowerPoint Add-in Not Loading**:
   - Verify the manifest.xml file and ensure all paths are correct.
   - Check that the development server is running on `https://localhost:3000`.

