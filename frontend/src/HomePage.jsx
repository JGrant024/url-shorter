import { useAuth } from "./AuthContext";

const HomePage = () => {
  const { isAuth } = useAuth();
  return (
    <>
      <h1>Hey There! Make yourself at home</h1>
      {isAuth ? <p>Logged In</p> : <p>Not Logged In</p>}
      <button type="submit">Login</button>
    </>
  );
};

export default HomePage;
