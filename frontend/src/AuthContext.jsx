import { createContext, useContext, useState, useEffect } from "react";
import PropTypes from "prop-types";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [isAuth, setisAuth] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("access_token")) {
      setisAuth(true);
    }
  }, []);
  return (
    <AuthContext.Provider value={{ isAuth, setisAuth }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}

AuthProvider.propTypes = {
  children: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.node),
    PropTypes.node,
  ]).isRequired,
};
