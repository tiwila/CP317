import React from 'react';
import './Header.css'; // Assuming Header.css is in the same directory

function LongHeader() {
  return (
    <header className="longheader">
      {/* Navigation Links */}
      <nav className="header__nav">
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#concerts">Concerts</a></li>
          <li><a href="#mytickets">My Tickets</a></li>
          <li><a href="#help">Help</a></li>
        </ul>
      </nav>

      {/* Logo Section */}
      <div className="header__logo">
        <img src="../Assets/images/logo1.png" alt="Logo" />
      </div>
      
      {/* Actions (e.g., Button) */}
      <div className="header__actions">
        <button className="header__btn">Login/Register</button>
      </div>
    </header>
  );
}

export default LongHeader;
