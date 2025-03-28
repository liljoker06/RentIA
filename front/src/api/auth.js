import axiosInstance from '../config/axiosInstance'

export const register = async (name, email, password) => {
    try {
        const response = await axiosInstance.post('/api/users', {name, email, password});
        return response.data;
    } catch (error) {
        console.log(error);
        throw new Error('Erreur lors de l\'inscription');
    }
};

export const login = async (email, password) => {
    try {
        const response = await axiosInstance.post('/api/auth', {email, password});
        localStorage.setItem('token', response.data.token);
        return response.data;
    } catch (error) {
        console.log(error);
        throw new Error('Erreur lors de la connexion');
    }
};

export const logout = () => {
    localStorage.removeItem('token'); 
    window.location.href = '/login'; 
  };