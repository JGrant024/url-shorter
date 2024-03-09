import { createBrowserRouter, RouterProvider } from "react-router-dom";
import ErrorPage from "./pages/ErrorPage";
import HomePage from "./HomePage";
import Login from "./Login";
import LogOut, { loader as Logoutloader } from "./LogOut";
import UrlForm from "./UrlForm";
import { AuthProvider } from "./AuthContext";
const router = createBrowserRouter([
  {
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/homepage",
        element: <HomePage />,
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/logout",
        element: <LogOut />,
        loader: Logoutloader,
      },
      {
        path: "/urlForm",
        element: <UrlForm />,
      },
    ],
  },
]);

import "./App.css";

function App() {
  return (
    <>
      <AuthProvider>
        <RouterProvider router={router} />
        {/* <h1>Url Shorter! </h1> */}
      </AuthProvider>
    </>
  );
}

export default App;
