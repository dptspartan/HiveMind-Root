import React, { useState, createContext } from 'react';

export const AuthContext = createContext();

export const UserAuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(-1);

  return (
    <AuthContext.Provider value={{isAuthenticated, setIsAuthenticated, user, setUser}}>
      {children}
    </AuthContext.Provider>
  );
};