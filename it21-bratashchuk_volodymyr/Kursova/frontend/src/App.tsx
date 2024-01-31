// файл: App.tsx
import { observer } from 'mobx-react-lite';
import { appStore } from './stores/AppStore';
import { Authentication } from './components/Authentication/Authentication';

const App = observer(() => {
  switch (appStore.appState) {
    case 'login':
      return <Authentication />;

    case 'main':
      return <MainContent />;

    case 'error':
      return <ErrorDisplay message={appStore.errorMessage} />;

    default:
      return <div>Loading...</div>;
  }
});

export default App;
