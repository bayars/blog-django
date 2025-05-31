import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

const AlbumDetail = () => {
  const { slug } = useParams();
  const [album, setAlbum] = useState(null);
  const [series, setSeries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAlbumData = async () => {
      try {
        const [albumResponse, seriesResponse] = await Promise.all([
          axios.get(`/api/v1/gallery/albums/slug/${slug}/`),
          axios.get(`/api/v1/gallery/series/?album_id=${albumResponse.data.id}`)
        ]);
        setAlbum(albumResponse.data);
        setSeries(seriesResponse.data);
        setLoading(false);
      } catch (err) {
        setError('Failed to load album data');
        setLoading(false);
      }
    };

    fetchAlbumData();
  }, [slug]);

  if (loading) return <div className="flex justify-center items-center min-h-screen">Loading...</div>;
  if (error) return <div className="text-red-500 text-center">{error}</div>;
  if (!album) return <div className="text-center">Album not found</div>;

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <Link to="/gallery" className="text-blue-500 hover:text-blue-700 mb-4 inline-block">
          ← Back to Gallery
        </Link>
        <h1 className="text-4xl font-bold mt-4">{album.title}</h1>
        {album.description && (
          <p className="text-gray-600 mt-2">{album.description}</p>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {series.map((photoSeries) => (
          <Link
            key={photoSeries.id}
            to={`/gallery/${album.slug}/${photoSeries.slug}`}
            className="group relative overflow-hidden rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300"
          >
            <div className="aspect-w-16 aspect-h-9">
              {photoSeries.photos && photoSeries.photos[0] ? (
                <img
                  src={photoSeries.photos[0].file_path}
                  alt={photoSeries.title}
                  className="object-cover w-full h-full transform group-hover:scale-105 transition-transform duration-300"
                />
              ) : (
                <div className="bg-gray-200 w-full h-full flex items-center justify-center">
                  <span className="text-gray-400">No photos</span>
                </div>
              )}
            </div>
            <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black to-transparent p-4">
              <h2 className="text-white text-xl font-semibold">{photoSeries.title}</h2>
              {photoSeries.description && (
                <p className="text-gray-200 text-sm mt-1 line-clamp-2">{photoSeries.description}</p>
              )}
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default AlbumDetail; 