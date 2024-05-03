import { readdirSync } from "node:fs";

import { Layout } from "./Layout";

export function HomePage() {
  const title = "Hello Bun";

  const data = readdirSync("../data");
  console.log(data);

  return (
    <Layout title={title}>
      <h1>{title}</h1>
      {/*<form id="form" data-hx-encoding="multipart/form-data" data-hx-post="/api/upload"
        _='on htmx:xhr:progress(loaded, total) set #progress.value to (loaded/total)*100'>
        <input type="file" name="file" />
        <button>Upload</button>
        <progress id="progress" value="0" max="100"></progress>
      </form>*/}
      <hr />
      <ul>
        {data.map(filename =>
        (<li key={filename}>
          <p>{filename}</p>
          <video width={200} height={200} src={`/data/${filename}`} controls />
        </li>)
        )}
      </ul>
    </Layout>
  );
}
