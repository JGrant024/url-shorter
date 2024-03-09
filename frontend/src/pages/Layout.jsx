import { Outlet } from "react-router-dom";
import Navigation from "../components/Navigation";

const primaryNav = [
  { title: "Home", url: "/HomePage" },
  { title: "Login", url: "/Login" },
  { title: "Logout", url: "/LogOut" },
];

const Layout = () => {
  return (
    <>
      <Navigation navItems={primaryNav} />
      <Outlet />
    </>
  );
};

export default Layout;
