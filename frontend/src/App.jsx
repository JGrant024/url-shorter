import { createBrowserRouter, RouterProvider } from "react-router-dom";
import ErrorPage from "../pages/ErrorPage";
import Home from "./Home";
import Login from "./Login";
import UrlForm from "./UrlForm";
const router = createBrowserRouter([
  {
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/login",
        element: <Login />,
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
      <RouterProvider router={router} />
      {/* <h1>Url Shorter! </h1> */}
    </>
  );
}

export default App;
