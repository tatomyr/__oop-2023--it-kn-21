import React from 'react';
import './Loader.scss';

export const Loader: React.FC<{ marginTop?: number }> = () => {
  return (
    <div className={`loader`}>
      <div className="container-loader">
        <div className="yellow point"></div>
        <div className="red point"></div>
        <div className="blue point"></div>
        <div className="violet point"></div>
      </div>
    </div>
  );
};
