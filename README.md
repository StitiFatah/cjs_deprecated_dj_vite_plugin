# Steps to Reproduce

```bash
python -m venv venv`
source venv/bin/activate`
pip install -r requirements.txt
cd mysite
npm init --yes
npm install
python manage.py runserver
npm run dev
```

Although everything is working it should give the `The CJS build of Vite's Node API is deprecated. See https://vitejs.dev/guide/troubleshooting.html#vite-cjs-node-api-deprecated for more details.` error.

As long as there is

```js
import { djangoVitePlugin } from "django-vite-plugin
```

inside `vite.config.mjs` the error is displayed.
