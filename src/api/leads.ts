import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export interface LeadData {
  name: string;
  mobile: string;
  email?: string;
  vehicleType: string;
  state: string;
  serviceType: string;
  comments?: string;
}

export const createLead = async (leadData: LeadData) => {
  try {
    const response = await axios.post(`${API_URL}/leads`, leadData);
    return response.data;
  } catch (error) {
    throw new Error('Failed to submit lead');
  }
};