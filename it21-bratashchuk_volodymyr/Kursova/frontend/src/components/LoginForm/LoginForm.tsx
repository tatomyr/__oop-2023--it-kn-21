import { useState } from 'react';
import { authStore } from '../../stores/AuthStore';
import { observer } from 'mobx-react-lite';

const LoginForm = observer(() => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async () => {
    authStore.login(username, password);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Вхід</h2>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Ім'я користувача"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Пароль"
        required
      />
      <button type="submit" disabled={authStore.isAuthenticating}>
        {authStore.isAuthenticating ? 'Вхід...' : 'Увійти'}
      </button>
    </form>
  );
});

export default LoginForm;
