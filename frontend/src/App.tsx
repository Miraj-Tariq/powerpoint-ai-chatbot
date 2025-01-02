import React from 'react';
// import logo from './logo.svg';
import './App.css';
import Header from "./components/Header";
import MainPage from "./components/MainPage";

function App() {
  return (
      <div style={{backgroundColor: "#F9F9F9", minHeight: "100vh"}}>
        <Header/>
        <MainPage/>
      </div>
  );
}

export default App;
