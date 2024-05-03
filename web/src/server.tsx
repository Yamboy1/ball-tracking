import { serve_backend } from "./backend";
import { HomePage } from "./components/HomePage";
import { html, serve_static } from "./response";

// Configuration
const port = process.env?.PORT ? Number(process.env.PORT) : 3000;

export function start() {
  const server = Bun.serve({
    port,
    fetch(req) {
      console.log(`[request]: ${req.method}: ${req.url}`);
      const url = new URL(req.url);

      // Handle backend paths
      if (url.pathname.startsWith("/api/")) return serve_backend(req);

      if (url.pathname.startsWith("/data/")) {
        return serve_static("../", req);
      }

      // Handle routes
      if (url.pathname == "/") return html(<HomePage />);

      // Fallback to serving public files
      return serve_static("public", req);
    },
  });

  console.log(`Listening on http://0.0.0.0:${server.port}...`);
}
