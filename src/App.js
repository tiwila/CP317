import React from 'react';
import Footer from './Components/footer';
import LongHeader from './Components/LongHeader';
function App() {

  return (
    <div>
       {/* Header Component */}
       <LongHeader />

        {/* Main Content */}
        <main>
          <h1>Welcome to My Website</h1>
          <p>
            Explore our amazing concerts and ticketing system. Browse through our events and 
            enjoy seamless experiences for all your favorite shows.
          </p>
        </main>

        {/* Footer Component */}
        <Footer />
    </div>
  )
}

export default App