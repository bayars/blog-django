import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const Gallery = () => {
  const [albums, setAlbums] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAlbums = async () => {
      try {
        const response = await axios.get('/api/v1/gallery/albums/');
        setAlbums(response.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to load albums');
        setLoading(false);
      }
    };

    fetchAlbums();
  }, []);

  if (loading) return <div className="flex justify-center items-center min-h-screen">Loading...</div>;
  if (error) return <div className="text-red-500 text-center">{error}</div>;

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8">Gallery</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {albums.map((album) => (
          <Link
            key={album.id}
            to={`/gallery/${album.slug}`}
            className="group relative overflow-hidden rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300"
          >
            <div className="aspect-w-16 aspect-h-9">
              {album.cover_image ? (
                <img
                  src={album.cover_image}
                  alt={album.title}
                  className="object-cover w-full h-full transform group-hover:scale-105 transition-transform duration-300"
                />
              ) : (
                <div className="bg-gray-200 w-full h-full flex items-center justify-center">
                  <span className="text-gray-400">No cover image</span>
                </div>
              )}
            </div>
            <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent p-4">
              <h2 className="text-white text-xl font-semibold">{album.title}</h2>
              {album.description && (
                <p className="text-gray-200 text-sm mt-1 line-clamp-2">{album.description}</p>
              )}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Gallery; 