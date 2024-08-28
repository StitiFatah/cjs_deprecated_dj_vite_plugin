import { defineConfig } from "vite";
import { djangoVitePlugin } from "django-vite-plugin";
//
export default defineConfig({
  plugins: [djangoVitePlugin(["appone/css/movies.css", "appone/js/movies.js"])],
});
