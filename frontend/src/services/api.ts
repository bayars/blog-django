import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getPosts = () => api.get('/posts/');
export const getPost = (id: number) => api.get(`/posts/${id}/`);

export const getProjects = () => api.get('/projects/');
export const getProject = (id: number) => api.get(`/projects/${id}/`);

export const getAlbums = () => api.get('/albums/');
export const getAlbum = (id: number) => api.get(`/albums/${id}/`);
export const getPhotos = () => api.get('/photos/');
export const getPhoto = (id: number) => api.get(`/photos/${id}/`);

export const getProfile = () => api.get('/profile/');
export const getExperiences = () => api.get('/experiences/');
export const getEducation = () => api.get('/education/');
export const getSkills = () => api.get('/skills/');
export const getCertifications = () => api.get('/certifications/');

export default api; 