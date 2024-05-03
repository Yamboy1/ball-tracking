export async function serve_backend(req: Request): Promise<Response> {
  const url = new URL(req.url);

  if (url.pathname == "/api/upload") {
    const formdata = await req.formData();
    const file = formdata.get("file");


    if (file == null || typeof file === "string") throw new Error("Must upload a file");
    await Bun.write("uploaded_file.png", file);
    return new Response("Success");
  }

  return new Response("Not found", { status: 404 });
}
