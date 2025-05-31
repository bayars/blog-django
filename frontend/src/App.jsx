import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import About from './pages/About';
import Contact from './pages/Contact';
import Gallery from './pages/Gallery';
import AlbumDetail from './pages/AlbumDetail';
import PhotoSeriesDetail from './pages/PhotoSeriesDetail';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/gallery" element={<Gallery />} />
            <Route path="/gallery/:slug" element={<AlbumDetail />} />
            <Route path="/gallery/:albumSlug/:seriesSlug" element={<PhotoSeriesDetail />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App; 