import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import homepage from './pages/Homepage';
import Events from './pages/Events';
import Navbar from './components/navbar';
import Footer from './components/footer';

const App = () => (
  <Router>
    <Navbar />
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/events" element={<Events />} />
    </Routes>
    <Footer />
  </Router>
);
export default App;
