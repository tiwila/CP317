import React from 'react';
import './footer.css'; // Assuming styles.css is in the same directory

function Footer() {
  return (
    <footer className="footer">
      {/* Quick Links Section */}
      <div className="footer__links">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About Us</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </div>

      {/* Contact Section */}
      <div className="footer__contact">
        <h4>Contact Us</h4>
        <p>
          Email: <a href="mailto:info@example.com">info@example.com</a>
        </p>
        <p>
          Phone: <a href="tel:+1234567890">+1 (234) 567-890</a>
        </p>
        <p>Address: 123 Main St, Your City</p>
      </div>

      {/* Social Media Section */}
      <div className="footer__social">
        <h4>Follow Us</h4>
        <div className="footer__icons">
          <a href="#facebook" aria-label="Facebook">
            <img src="path/to/facebook-icon.png" alt="Facebook" />
          </a>
          <a href="#twitter" aria-label="Twitter">
            <img src="path/to/twitter-icon.png" alt="Twitter" />
          </a>
          <a href="#instagram" aria-label="Instagram">
            <img src="path/to/instagram-icon.png" alt="Instagram" />
          </a>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
