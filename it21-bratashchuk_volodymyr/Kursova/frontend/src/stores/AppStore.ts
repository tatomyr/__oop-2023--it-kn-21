// файл: stores/AppStore.ts
import { makeAutoObservable } from 'mobx';

type AppState = 'login' | 'main' | 'error';

class AppStore {
  appState: AppState = 'login';
  errorMessage: string = '';

  constructor() {
    makeAutoObservable(this);
  }

  setAppState(state: AppState) {
    this.appState = state;
  }

  setError(message: string) {
    this.errorMessage = message;
    this.appState = 'error';
  }

  clearError() {
    this.errorMessage = '';
  }

  // Додаткові методи та логіка додатку
}

export const appStore = new AppStore();
