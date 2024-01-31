import React, { useState } from 'react';
import { observer } from 'mobx-react-lite';
import { authStore } from '../../stores/AuthStore';

const RegisterForm = observer(() => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    authStore.register(username, email, password);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      <button type="submit" disabled={authStore.isAuthenticating}>
        {authStore.isAuthenticating ? 'Вхід...' : 'Увійти'}
      </button>
    </form>
  );
});

export default RegisterForm;
