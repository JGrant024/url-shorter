import { Form, redirect } from "react-router-dom";

export async function action({ request }) {
  const formData = await request.formData();
  const email = formData.get("email");
  const password = formData.get("password");
  const data = { email, password };

  const url = "http://localhost:8000/login";

  const loginFunction = await fetch(url, {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify(data),
  }).then((response) => response.json());

  console.log("login function", loginFunction);
  return redirect("/home");
}

const Login = () => {
  return (
    <Form method="POST">
      <label>
        Email
        <input
          type="email"
          id="email"
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
      <button type="button">Submit</button>
    </Form>
  );
};

export default Login;
