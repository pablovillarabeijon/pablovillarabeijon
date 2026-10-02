# Pablo Villar-Abeijón — web en Quarto

Proyecto preparado a partir del Google Site público el 2 de octubre de 2026. Mantiene sus seis páginas, textos en inglés, referencias, enlaces profesionales, fotografía personal, imágenes de investigación y CV de agosto de 2026.

## Publicarla sin instalar Quarto ni usar la terminal

1. En GitHub, crea un repositorio **público** llamado exactamente `TU_USUARIO.github.io`, sustituyendo `TU_USUARIO` por tu nombre de usuario de GitHub. Usa `main` como rama principal. Puedes marcar «Add a README file» para inicializarlo. No hace falta comprar un dominio.
2. Descomprime el ZIP y abre la carpeta `pablo-quarto`. En el repositorio, elige **Add file → Upload files**. Arrastra **el contenido de la carpeta**, no la carpeta exterior ni el ZIP. Incluye las carpetas `assets` y `scripts`, todos los `.qmd`, `_quarto.yml`, `styles.css`, `site.js`, `footer.html` y `robots.txt`. Confirma con **Commit changes** en `main`.
3. Los sistemas operativos suelen ocultar la carpeta `.github`. Para asegurarte de incluirla, abre **Add file → Create new file**. Escribe como nombre `.github/workflows/publish.yml`. Copia dentro todo el contenido del archivo visible `PUBLICAR_EN_GITHUB.yml` incluido en este proyecto y confirma con **Commit changes**. Si ya has subido la carpeta `.github` mediante GitHub Desktop o Git, omite este paso.
4. En **Settings → Pages → Build and deployment → Source**, selecciona **GitHub Actions**. Este proyecto usa GitHub Actions, no «Deploy from a branch» ni `gh-pages`.
5. Abre **Actions → Publish Quarto website → Run workflow → main → Run workflow**. Esto fuerza una nueva ejecución después de activar Pages. Espera a que `build` y `deploy` aparezcan en verde. Si una ejecución anterior falló porque Pages aún no estaba activado, usa esta nueva ejecución.
6. La dirección publicada aparecerá en **Settings → Pages**. Para el repositorio recomendado será `https://TU_USUARIO.github.io/`. Abre esa dirección y comprueba las seis páginas.

GitHub instalará Quarto y generará la web por ti. No necesitas R, Python ni Quarto en tu ordenador para publicarla o editar texto desde GitHub. El proceso configura automáticamente la URL canónica, las vistas previas sociales, `sitemap.xml` y la referencia al sitemap en `robots.txt` usando la dirección real de GitHub Pages.

Si el repositorio ya contiene una web que quieres conservar, crea primero otro repositorio y usa su URL de proyecto; no sobrescribas el existente. La configuración automática también admite `https://TU_USUARIO.github.io/NOMBRE_REPOSITORIO/`.

## Qué archivo editar

| Página | Archivo |
|---|---|
| Inicio / About me | `index.qmd` |
| Research lines | `research-lines.qmd` |
| CV | `cv.qmd` y `assets/files/cv_august26.pdf` |
| Publications | `publications.qmd` |
| Presentations & Conferences | `presentations-conferences.qmd` |
| Teaching & Supervision | `teaching-superv.qmd` |
| Colores, tamaños y disposición | `styles.css` |
| Menú y configuración general | `_quarto.yml` |
| Perfiles profesionales y correo al pie | `footer.html` |

En GitHub, abre el archivo, pulsa el lápiz, modifica el texto y confirma el cambio. Cada cambio en `main` vuelve a generar y publicar la web automáticamente. Mantén los bloques `:::` que delimitan las columnas.

Las imágenes y el PDF están dentro del proyecto. Para renovar el CV, sube el nuevo PDF usando el mismo nombre `assets/files/cv_august26.pdf`; así se conservan los enlaces. Si cambias el nombre, modifica también `cv.qmd`.

`PUBLICAR_EN_GITHUB.yml` es solo una copia visible para facilitar la configuración. GitHub ejecuta únicamente `.github/workflows/publish.yml`; si luego editas la automatización, edita este último.

## Verla y editarla localmente

Opcional: instala Quarto desde https://quarto.org/docs/get-started/ y, en la terminal de esta carpeta, ejecuta:

```bash
quarto preview
```

Para generar el HTML:

```bash
quarto render
```

La carpeta `_site` contiene el HTML generado. Se ha incluido una copia de esa carpeta en el paquete para inspección local. No hace falta subirla a GitHub: el workflow la vuelve a generar. Si abres `_site/index.html` directamente en el navegador, el buscador y la navegación a la raíz pueden funcionar de forma distinta que en la web publicada; `quarto preview` es la comprobación local adecuada.

Para que una generación local incluya sitemap y URL canónica, añade tu dirección real como `website.site-url` en `_quarto.yml` o ejecuta:

```bash
python scripts/configure_site.py https://TU_USUARIO.github.io/
quarto render --profile ci
```

## Fidelidad respecto al Google Site

Se mantienen la paleta oliva, los resaltados, títulos con serif, marcos de los encabezados, columnas de la portada y alternancia de imágenes y texto en Research lines. Se ha añadido un menú superior visible y una adaptación a pantallas pequeñas.

Hay dos diferencias pendientes:

- Las fotografías de fondo de los encabezados de Inicio y Presentations & Conferences no pudieron descargarse. Se usan fondos lisos de la misma paleta. `styles.css` contiene un ejemplo comentado para recuperar la fotografía cuando dispongas del archivo original.
- El carrusel contiene tres mapas recuperados de Research lines: proximidad/alquileres, ciudades gallegas y peatonalización/turismo. No se recuperaron sus cuatro archivos específicos del carrusel original. Falta el mapa independiente de calles peatonalizadas de 2012–2020, y los otros tres pueden tener un encuadre diferente. Puedes sustituir las imágenes y añadir una cuarta diapositiva en `index.qmd`; el contador se adapta automáticamente al número de diapositivas.

La fuente de texto Open Sans está incluida. Los títulos usan Cambria si está disponible y Georgia como alternativa; puede haber pequeñas diferencias tipográficas entre sistemas. El mapa interactivo sigue siendo el mismo contenido externo de Flourish, por lo que necesita conexión y que Flourish siga disponible. El visor del PDF depende de las capacidades del navegador y siempre ofrece un enlace para abrirlo.

Los textos y la lista de publicaciones reflejan lo que figuraba en la web original; no se han añadido artículos posteriores ni corregido afirmaciones académicas.

## Aparecer en Google

Una vez publicada, añade **la nueva URL** a Google Search Console como propiedad de prefijo de URL. Sigue el método de verificación que te proporcione Google: si eliges archivo HTML, inclúyelo como recurso del proyecto para que Quarto lo copie a `_site`; si eliges etiqueta HTML, inclúyela en la cabecera con `include-in-header`.

Después envía `sitemap.xml` y solicita la indexación de la portada. Actualiza los enlaces de ORCID, Google Scholar, LinkedIn y tu perfil universitario para apuntar a la nueva web. Mantén de momento el Google Site y añade allí un enlace a la nueva dirección. Publicar correctamente y enviar el sitemap facilita el descubrimiento, pero no garantiza la inclusión en Google.

## Fuentes técnicas

- Quarto websites: https://quarto.org/docs/websites/
- Quarto social metadata and website tools: https://quarto.org/docs/websites/website-tools.html
- Quarto and GitHub Pages: https://quarto.org/docs/publishing/github-pages.html
- GitHub Pages workflows: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Comprobaciones realizadas

Generación con Quarto 1.10.18; comprobación de las seis páginas y de la página 404; presencia del contenido; resolución de enlaces internos, imágenes, hojas de estilo, scripts y PDF; comprobación de sitemap y URL canónica con una configuración de publicación de prueba. El workflow está preparado, pero no se ha ejecutado en tu cuenta de GitHub ni se ha publicado una web.
