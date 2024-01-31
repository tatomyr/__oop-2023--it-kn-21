import { makeAutoObservable, runInAction } from 'mobx';
import { apiService } from '../services/apiService';

class MainContentStore {
  isLoading = true;
  isCreating = false;
  isDeleting = false;
  stats: { equipment_id: string; name: string; rental_count: number; type: string }[] = [];

  constructor() {
    makeAutoObservable(this);
  }

  async loadStats() {
    const stats = await apiService.getEquipmentUsageStats();

    runInAction(() => {
      this.stats = stats;
      this.isLoading = false;
    });
  }

  async rentEquipment() {}

  async createEquipment(name: string, type: string) {
    this.isCreating = true;
    try {
      const { id } = await apiService.createEquipment(name, type);

      runInAction(() => {
        this.stats.push({ equipment_id: id, name, rental_count: 0, type });
      });
    } catch (error) {
      alert('failed to create equipment');
    } finally {
      runInAction(() => {
        this.isCreating = false;
      });
    }
  }

  async deleteEquipment(id: string) {
    try {
      this.isDeleting = true;
      await apiService.deleteEquipment(id);

      runInAction(() => {
        this.stats = this.stats.filter((equopment) => equopment.equipment_id !== id);
      });
    } catch (error) {
      alert('failed to delete user');
    } finally {
      runInAction(() => {
        this.isDeleting = false;
      });
    }
  }
}

export const mainContentStore = new MainContentStore();
