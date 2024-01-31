/* eslint-disable @typescript-eslint/no-explicit-any */
const BASE_URL = 'http://localhost:3001';

async function postRequest(path: string, data: any) {
  try {
    const response = await fetch(`${BASE_URL}${path}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    return response.json();
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

async function getRequest(path: string) {
  const token = localStorage.getItem('jwtToken'); // Припустимо, що токен зберігається тут
  try {
    const response = await fetch(`${BASE_URL}${path}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
    });
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    return response.json();
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

export const apiService = {
  async register(username: string, email: string, password: string) {
    return postRequest('/register', { username, email, password });
  },

  async login(username: string, password: string) {
    return postRequest('/login', { username, password });
  },

  async getEquipmentUsageStats() {
    return getRequest('/equipment-usage-stats');
  },

  async createEquipment(name: string, type: string) {
    return postRequest('/create_equipment', { name, type });
  },

  async rentEquipment(equipmentId: string) {
    return postRequest('/rent_equipment', { equipment_id: equipmentId });
  },

  async deleteEquipment(equipmentId: string) {
    return postRequest('/delete_equipment', { equipment_id: equipmentId });
  },

  // Можете додати інші методи, якщо потрібно
};
