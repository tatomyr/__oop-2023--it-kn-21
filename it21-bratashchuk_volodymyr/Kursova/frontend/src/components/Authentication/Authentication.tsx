import { useState } from 'react';
import RegisterForm from '../RegisterForm/RegisterForm';
import LoginForm from '../LoginForm/LoginForm';

export const Authentication = () => {
  const [isRegistering, setIsRegistering] = useState(true);

  return (
    <div>
      {isRegistering ? (
        <>
          <RegisterForm />
          <p>
            Вже зареєстровані? <button onClick={() => setIsRegistering(false)}>Увійти</button>
          </p>
        </>
      ) : (
        <>
          <LoginForm />
          <p>
            Ще не зареєстровані? <button onClick={() => setIsRegistering(true)}>Реєстрація</button>
          </p>
        </>
      )}
    </div>
  );
};
