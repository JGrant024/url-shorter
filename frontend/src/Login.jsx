import { Form } from "react-router-dom";

export async function action({ request }) {
  const formData = await request.formData();
  const email = formData.get("email");
  const password = formData.get("password");
  const LoginData = { email, password };

  try {
    const url = `${import.meta.env.VITE_SOURCE_URL}/Login`;
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(LoginData),
    });

    const statusCode = response.status;
    const data = await response.json();

    const { access_token } = data;

    localStorage.clear();
    localStorage.setItem("access-token", access_token);
    return statusCode === 200 ? true : false;
  } catch (error) {
    console.error("ERROR:", error);
  }
}

const Login = () => {
  return (
    <>
      <h1>Login Form </h1>
      <Form method="POST">
        <label>
          Email
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Enter E-mail Address"
            required
          />
        </label>
        <br />
        <br />
        <label>
          Password
          <input
            type="text"
            id="password"
            name="password"
            minLength="8"
            placeholder="Enter Password"
            required
          />
        </label>
        <br />
        <br />
        <button type="submit">Submit</button>
      </Form>
    </>
  );
};

export default Login;
