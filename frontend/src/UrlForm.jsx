import { Form } from "react-router-dom";

export async function action({ request }) {
  const urlData = await request.formData();
  const title = urlData.get("title");
  const original_url = urlData.get("original_url");
  const shortend_url = url.get("short_url");
  const data = { title, original_url, shortend_url };

  const url = "http://localhost:8000/url/create";
  const addUrl = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).then((response) => response.json());
  console.log("URL function to add urls(create)", addUrl);
  return addUrl;
}

const UrlForm = () => {
  return (
    <Form>
      <label>
        Title
        <input
          type="text"
          name="title"
          placeholder="Enter URL Title"
          required
        />
      </label>
      <label>
        Original URL:
        <input
          type="text"
          name="original_url"
          placeholder="Please enter URL"
          required
        />
      </label>
      <label>
        Shortend URL:
        <input
          type="text"
          name="shortend_url"
          placeholder="Short URL"
          required
        />
      </label>
      <br />
      <br />
      <button type="button">Submit URL</button>
    </Form>
  );
};
export default UrlForm;
