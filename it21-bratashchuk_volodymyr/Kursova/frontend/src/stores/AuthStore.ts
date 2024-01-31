// файл: stores/AuthStore.ts
import { makeAutoObservable, runInAction } from 'mobx';
import { jwtDecode } from 'jwt-decode';
import { apiService } from '../services/apiService';
import { appStore } from './AppStore';

class AuthStore {
  isAuthenticated = false;
  isAuthenticating = false;
  token: string | null = null;
  role: 'admin' | 'user' = 'user';
  isError = false;
  errorMessage = '';

  constructor() {
    makeAutoObservable(this);
    this.loadToken();
  }

  async login(username: string, password: string) {
    try {
      this.setIsAuthenticating(true);
      const { token } = await apiService.login(username, password);

      runInAction(() => {
        this.token = token;
        this.isAuthenticated = true;
        localStorage.setItem('jwtToken', token);
        appStore.setAppState('main');
      });
    } catch (error) {
      runInAction(() => {
        appStore.setError('Something went wrong');
      });
    } finally {
      runInAction(() => {
        this.setIsAuthenticating(false);
      });
    }
  }

  logout() {
    this.isAuthenticated = false;
    this.token = null;
    localStorage.removeItem('jwtToken');
  }

  async register(username: string, email: string, password: string) {
    try {
      this.setIsAuthenticating(true);
      await apiService.register(username, email, password);
    } catch (error) {
      runInAction(() => {
        appStore.setError('Something went wrong');
      });
    } finally {
      runInAction(() => {
        this.setIsAuthenticating(false);
      });
    }
  }

  setIsAuthenticating(state: boolean) {
    this.isAuthenticating = state;
  }

  showError(message: string) {
    this.isError = true;
    this.errorMessage = message;
  }

  loadToken() {
    const token = localStorage.getItem('jwtToken');
    const decoded = jwtDecode(token as unknown as string) as { role: 'admin' | 'user'; username: string };
    this.role = decoded.role;
    if (token) {
      this.token = token;
      this.isAuthenticated = true;
      appStore.setAppState('main');
    } else {
      appStore.setAppState('login');
    }
  }
}

export const authStore = new AuthStore();
