import { ReactNode } from "react";

export function Layout({
  title,
  children,
}: {
  title: string;
  children: ReactNode;
}) {
  return (
    <html>
      <head>
        <title>{title}</title>
        <meta
          name="description"
          content="A demo app using Bun + HTMX + TailwindCSS + DaisyUI, based on danawoodman/bun-htmx"
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta charSet="utf-8" />
        {/*<link rel="stylesheet" href="/tailwind.css" /> */}
        <script src="https://unpkg.com/hyperscript.org@0.9.12"></script>
        <script src="https://unpkg.com/htmx.org@1.9.12"></script>
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}
