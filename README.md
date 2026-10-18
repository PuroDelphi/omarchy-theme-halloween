# Halloween para Omarchy

Tema oscuro de Halloween: naranja calabaza, amatista, marfil y verde de poción sobre superficies casi negras. **12 fondos: 10 imágenes descargadas con licencia redistribuible y 2 ilustraciones originales en 4K**; sin sonidos, servicios en segundo plano ni sustos automáticos.

![Halloween en una sesión real de Omarchy: terminal, Neovim y fondo Calabaza y farol](preview.png)

Captura real, sin montaje de ventanas ni datos privados. [Segunda captura con la mansión original](previews/desktop-mansion.png) · [WebP del catálogo, 1200 × 675](previews/halloween.webp).

## Diseño y colores

`colors.toml` es la fuente de verdad. Omarchy genera las configuraciones de terminales, Hyprland, Neovim, Helix, btop, navegador, editores y shell a partir de sus plantillas. No hace falta mantener copias de esas configuraciones dentro del tema. Las aplicaciones instaladas y las plantillas locales determinan qué integraciones se aplican.

| Papel | Color | Uso |
| --- | --- | --- |
| Noche | `#121016` | Fondo principal |
| Vacío | `#08070C` | Superficie más profunda |
| Berenjena | `#251D2D` | Superficies elevadas |
| Calabaza | `#FF9A3C` | Acento, foco y acciones |
| Amatista | `#BB9AF7` | Extremo del borde activo y violeta |
| Marfil | `#F5E9D3` | Texto principal |
| Hueso | `#FFF4DF` | Texto brillante y cursor generado |
| Lavanda gris | `#9B8DA8` | Texto atenuado |
| Ciruela | `#4B2E53` | Selección, con texto `#FFF4DF` |
| Carmesí | `#FF667A` | Errores y alertas |
| Poción | `#B5D66F` | Éxito y verde ANSI |
| Vela | `#FFD166` | Advertencias y amarillo ANSI |
| Luna azul | `#A5B4FC` | Azul ANSI |
| Rosa espectral | `#ED96C3` | Magenta ANSI |
| Ectoplasma | `#7ED6C4` | Cian ANSI |

Borde activo: degradado calabaza → amatista a 45°. Borde inactivo: `#4B3A55`. El degradado es una declaración de color, no una animación. Los colores ANSI brillantes están definidos por separado. `icons.theme` selecciona **Yaru**, la variante naranja disponible de serie según el manual.

Contrastes calculados con luminancia relativa sRGB (WCAG): texto/fondo **15,73:1**, atenuado/fondo **6,09:1**, acento/fondo **8,94:1**, selección **10,61:1**. Son relaciones entre colores sólidos: no certifican texto superpuesto a cualquier parte de una imagen ni todas las transparencias de las aplicaciones.

## Organización instalable

La raíz del repositorio es la raíz del tema, sin una carpeta contenedora adicional:

```text
omarchy-theme-halloween/
├── colors.toml              # Paleta semántica
├── icons.theme              # Yaru
├── backgrounds/             # 10 descargados + 2 originales PNG 4K
├── artwork/                 # Fuentes SVG de los 2 originales
├── preview.png              # Captura real de escritorio, 16:9
├── previews/                # Segunda captura, WebP, arte y planchas
├── tools/                   # Regeneración del arte
├── LICENSE                  # MIT: configuración, herramientas y documentación
├── ARTWORK-LICENSE          # CC0 1.0: solo arte original
├── SOURCES.md               # Autor, fuente y licencia de cada descarga
├── sources/                 # Metadatos de procedencia
└── README.md
```

Los doce archivos finales van en `backgrounds/`: no hay miniaturas ni fuentes SVG mezcladas en el selector. Los descargados se conservan a su resolución de origen, sin ampliarlos artificialmente. Consulta [`SOURCES.md`](SOURCES.md) para sus títulos, autores, dimensiones y licencias, y [`previews/contact-sheet.png`](previews/contact-sheet.png) para ver los doce juntos.

### Dos ilustraciones originales adicionales

Los archivos **11** y **12** son creaciones procedurales propias del proyecto, no descargas ni recolores de fotografías. Sus fuentes SVG editables están en `artwork/` y sus PNG finales tienen **3840 × 2160 píxeles**. La plancha [`previews/originals-contact-sheet.png`](previews/originals-contact-sheet.png) muestra exclusivamente esas dos obras; [`previews/theme-art-preview.png`](previews/theme-art-preview.png) conserva su presentación artística separada de las capturas reales.

- **11 — Campo de calabazas:** cosecha nocturna, luz de vela y siluetas de Halloween.
- **12 — Mansión del cuervo:** arquitectura embrujada, ventanas cálidas y cielo amatista.

### Regenerar las ilustraciones

Los PNG ya están incluidos; esto es solo para desarrollar el arte. Requiere **Python 3** y **`rsvg-convert`**, del paquete Arch `librsvg`. No necesita red ni paquetes Python adicionales.

```bash
python tools/render-wallpapers.py
```

El comando vuelve a generar únicamente los dos originales: sus fuentes SVG, los PNG 3840 × 2160 y sus vistas artísticas en `previews/`. **No sobrescribe `preview.png` ni las capturas reales.** No descarga, sustituye ni borra las diez fotografías. Para generar una escena a otra resolución en un directorio independiente:

```bash
python tools/render-wallpapers.py --scene 11 --width 1920 --height 1080 --output-dir /tmp/halloween-art
```

`--sources-only` genera solo las fuentes; `--help` describe las opciones. Conserva los dos PNG originales a 4K al distribuir el tema. El escritorio ajusta la imagen recortándola para llenar cada monitor, por lo que otras proporciones pueden ocultar detalles de los bordes.


## Instalación local

Desde la raíz de este proyecto:

```bash
mkdir -p "$HOME/.config/omarchy/themes"
ln -sT -- "$PWD" "$HOME/.config/omarchy/themes/theme-halloween"
omarchy theme set theme-halloween
```

Si ya existe `~/.config/omarchy/themes/theme-halloween`, `ln -sT` no lo sustituye: revisa ese destino antes de continuar. El enlace permite editar el proyecto y reaplicar el tema sin copiar archivos. **El último comando cambia el escritorio activo.** No se necesita `sudo`, modificar `/usr/share/omarchy/` ni reiniciar la sesión.

Para recorrer los doce fondos:

```bash
omarchy theme bg next
```

Para volver, consulta `omarchy theme list` y aplica el nombre de tu tema anterior con `omarchy theme set`. Instalar o crear este repositorio por sí solo no cambia tu escritorio.

## Instalación desde GitHub

```bash
omarchy theme install https://github.com/PuroDelphi/omarchy-theme-halloween
```

Este comando descarga **y aplica** el tema. Para seleccionarlo otra vez:

```bash
omarchy theme set theme-halloween
```

El repositorio solicitado se llama `omarchy-theme-halloween`: Omarchy elimina el prefijo `omarchy-`, de modo que su identificador instalado es **`theme-halloween`**, no `halloween`. Se conserva el nombre del repositorio elegido por su propietario aunque difiera de la convención recomendada `omarchy-[nombre]-theme`.

## Distribución y aprobación

1. Repositorio de distribución: **[PuroDelphi/omarchy-theme-halloween](https://github.com/PuroDelphi/omarchy-theme-halloween)**. La raíz contiene directamente la paleta y `backgrounds/`.
2. Comprueba la instalación desde esa URL con **Install → Style → Theme** o el comando anterior. El identificador resultante debe ser `theme-halloween`.
3. `preview.png` contiene una captura real con terminal y Neovim; `previews/desktop-mansion.png` muestra una segunda escena. Se revisaron antes de publicar para evitar ventanas privadas, nombres de usuario, notificaciones y cursor de ratón.
4. Propuesta enviada al catálogo del sitio: **[omacom/omarchy-site#586](https://github.com/omacom/omarchy-site/pull/586)**, con la captura WebP y la entrada alfabética requeridas.

**Instalable ≠ aceptado en el catálogo ≠ incluido de serie.** El manual ofrece la vía del catálogo de temas comunitarios; no promete convertir una propuesta en tema oficial de la distribución. La aceptación depende de los mantenedores. Publicar en GitHub no supone haber enviado ni obtenido aprobación del catálogo.

El tema usa el formato semántico de la instalación de referencia **Omarchy 4.0.0.alpha**. No se garantiza compatibilidad con ediciones anteriores basadas en otros formatos de configuración.

### Envíos comunitarios

- **Catálogo del sitio:** [PR #586](https://github.com/omacom/omarchy-site/pull/586). La propuesta pasó localmente build, lint, tipos, **51 pruebas Node + 45 Python**, paridad estática y comprobación visual del catálogo en navegador. Estas comprobaciones locales no equivalen a checks remotos ni a aprobación de un mantenedor.
- **Registro del marketplace:** [solicitud #128](https://github.com/omacom/omarchy-theme-registry/issues/128), con URL, nombre, confirmaciones de derechos/privacidad y capturas reales. La cuenta no tiene permiso para añadir la etiqueta `submission`; se solicitó al mantenedor que la aplique y active la validación. No se afirma que el validador remoto haya aprobado el tema.
- Las dos propuestas se enviaron como **tema estático, sin sustos automáticos**. Consulta sus enlaces para conocer la decisión actual de los mantenedores; el envío no implica aparición inmediata en los catálogos.


### Catálogo del sitio: requisitos concretos

Según [“Adding your theme” del sitio](https://github.com/omacom/omarchy-site#adding-your-theme), el PR debe incluir:

- Una **captura real 16:9** con terminal, editor y un fondo del tema; sin cursor, notificaciones ni información privada. Una ilustración o un escritorio vacío no sustituye esa captura.
- La captura convertida a WebP en `assets/themes/halloween.webp`, objetivo **1200 × 675** y aproximadamente **menos de 100 KB**, sin ampliar una captura pequeña.
- Un bloque `<figure class="themes__theme">` en **`themes/index.html`**, en orden alfabético. Imagen y título deben enlazar a `https://github.com/PuroDelphi/omarchy-theme-halloween`.

El sitio genera sus datos desde ese HTML: no editar `src/data/themes.json` como fuente de la propuesta. Un PR sin captura no puede integrarse. `previews/halloween.webp` es la captura real preparada para ese envío: **1200 × 675, 91.640 bytes**. La vista artística separada no debe confundirse con la captura.

### Marketplace: vía de registro separada

También existe [themes.omarchy.org](https://themes.omarchy.org), con [registro e instrucciones propios](https://github.com/omacom/omarchy-theme-registry). Su formulario [Submit a theme](https://github.com/omacom/omarchy-theme-registry/issues/new?template=submit-theme.yml) solicita la URL, permite indicar **Halloween** como nombre visible y exige confirmar autoría/permisos y ausencia de datos privados. El bot valida y propone un PR; la decisión final sigue correspondiendo a un mantenedor.

El registro pide paleta y fondos en la raíz del tema y `preview.png` 16:9 de al menos 1000 píxeles de ancho. Rechaza enlaces simbólicos, imágenes mayores de 50 MB o 40 megapíxeles y repositorios mayores de 400 MB, entre otros errores. README, LICENSE y el topic `omarchy-theme` son recomendados. Un nombre de repositorio no convencional y herramientas de generación pueden producir **advertencias**, no necesariamente errores. El enlace local de la sección de instalación no forma parte del repositorio ni de su descarga.

El registro puede asignar otro identificador si ya está ocupado. Su instalación por nombre/commit validado pertenece a ese sistema; en la instalación local verificada se usa la **URL Git completa**, sin asumir que `omarchy theme install halloween` esté disponible.

### Inclusión de serie

Los temas integrados están en `themes/` del [proyecto Omarchy](https://github.com/omacom/omarchy). No se encontró una política específica que garantice aceptar un tema nuevo en ese conjunto. El proyecto dirige las sugerencias a [Discussions](https://github.com/omacom/omarchy/discussions), en lugar de usar issues de bugs para propuestas. La publicación y los catálogos comunitarios no equivalen a esa inclusión.


### Lo que un tema descargado no debe necesitar

En la versión consultada, un tema clonado con `omarchy theme install` no puede aportar Lua, configuraciones de terminal (`alacritty.toml`, `foot.ini`, `ghostty.conf`, `kitty.conf`) ni `vscode.json`: Omarchy los excluye del staging y los regenera desde la paleta. No se incluyen aquí. Tampoco hay instalador ejecutable, hooks de autoinicio o extensiones obligatorias.

## Movimiento y sustos

Un tema de colores no es un programa de efectos. El degradado de bordes y los fondos incluidos son estáticos. Las animaciones de ventanas y las transiciones de fondo que tenga configuradas el escritorio pertenecen al compositor y al shell, no a las ilustraciones de este repositorio.

En **esta instalación 4.0.0.alpha**, el plugin de fondo usa nodos Qt Quick `Image` y una transición de revelado de **420 ms**. El selector enumera PNG, JPG/JPEG, GIF, BMP y WebP. Aceptar un GIF como archivo **no significa reproducir sus fotogramas**: el nodo `Image` es estático; Qt ofrece `AnimatedImage` para esa función. No hay un reproductor de vídeo en ese renderer ni MP4/WebM en sus filtros.

Hay una diferencia de versiones importante: el [manual remoto de la rama `quattro`](https://github.com/omacom/omarchy/blob/quattro/manual/39-backgrounds.md) documenta fondos animados/vídeo y OWE. Eso no prueba que estén presentes en el código instalado aquí. Antes de añadir movimiento, hay que comprobar el renderer y la versión efectivos; no basta con cambiar la extensión de un fondo.


Para introducir apariciones, sonido o temporizadores haría falta una extensión/automatización aparte, instalada de forma explícita. No debe ocultarse código en un tema ni intentar saltarse el filtrado del instalador. Un hook `theme-set` puede reaccionar a un cambio de tema, pero no convierte una imagen en animación ni se instala automáticamente desde este repositorio.

La arquitectura disponible permite un plugin Quickshell de tipo **overlay**, con manifiesto y QML bajo `~/.config/omarchy/plugins/`, activado por separado. Puede animar opacidad/desplazamiento o mostrar `AnimatedImage`; es código de confianza del usuario, no una propiedad de `colors.toml`. Esta es una posibilidad técnica investigada, **no una extensión incluida o probada en este proyecto**. Vídeo/animación continua exige más recursos que una imagen fija; no se midió su consumo.


Cualquier extensión de sustos debería ser **opt-in**, tener una salida inmediata y desinstalación clara, evitar destellos/estrobos, permitir silenciarla, limitar recursos y no aparecer sobre bloqueo, autenticación o trabajo sensible. Este tema no implementa ni activa sustos.

## Verificación realizada

Sobre **Omarchy 4.0.0.alpha**, primero en aislamiento y después en una sesión gráfica real:

- Decodificación completa de los **12 fondos**, comprobación de dimensiones y ausencia de duplicados binarios: correcta.
- **10 descargados** en su resolución de origen, entre 3264 y 6000 píxeles de ancho; **2 originales** a 3840 × 2160.
- Ejecución real del generador para la escena 11 a **1920 × 1080** en un directorio temporal: correcta.
- Instalación real con `omarchy theme install` desde un repositorio Git temporal del contenido del proyecto, usando **HOME y rutas XDG aislados** y `OMARCHY_THEME_HEADLESS=1`: salida 0, identificador **`theme-halloween`**, los 12 fondos disponibles y enlace de fondo válido.
- **19 configuraciones** generadas por las plantillas instaladas, sin variables sin resolver; salidas JSON/TOML analizadas correctamente.
- `foot --check-config` sobre su configuración generada: salida **0**.
- Revisión visual de los dos originales, de la presentación artística y de la plancha de los doce fondos.
- Instalación desde la URL pública y aplicación real en Hyprland: **Theme Halloween**, con el fondo **Calabaza y farol** activo; `hyprctl configerrors` sin errores.
- Comprobación visual real de **Foot, Neovim, bordes y fondo**, con dos capturas de escritorio. No se han probado visualmente todas las demás aplicaciones.
- Las capturas proceden del monitor nativo **1366 × 768**, con un recorte mínimo de 3 píxeles por lado y 1/2 píxeles arriba/abajo hasta **1360 × 765**, sin ampliación ni deformación. El WebP se redujo a **1200 × 675**.
- Durante la aplicación y los cambios de fondo **no aparecieron sustos**. El tema no contiene una extensión, sonido ni temporizador que los implemente: esa función **no está incluida**.

Los fondos suman **26,12 MiB**. Se mantienen los originales sin compresión adicional: esto supera ligeramente el umbral orientativo de advertencia de 25 MiB del registro, pero cada imagen cumple sus límites duros de 50 MB y 40 megapíxeles. Una solicitud comunitaria no supone aceptación ni inclusión de serie.


## Fuentes primarias

- [Manual: crear y distribuir un tema](https://omarchy.org/manual/making-your-own-theme/).
- [Catálogo de temas comunitarios](https://omarchy.org/themes/).
- [Repositorio de Omarchy](https://github.com/omacom/omarchy): comandos `omarchy-theme-install`, `omarchy-theme-set`, `omarchy-theme-set-templates` y `omarchy-theme-color`.
- [Repositorio del sitio](https://github.com/omacom/omarchy-site): vía de contribución del catálogo. El manual puede conservar enlaces con un nombre antiguo de organización; el catálogo enlaza a `omacom`.
- [Instrucciones exactas del catálogo](https://github.com/omacom/omarchy-site#adding-your-theme) y [registro del marketplace](https://github.com/omacom/omarchy-theme-registry).
- [Qt Quick Image](https://doc.qt.io/qt-6/qml-qtquick-image.html#details): diferencia entre imágenes estáticas y animadas.

## Licencias y procedencia

Configuración, herramientas y documentación: [MIT](LICENSE). Los **dos originales**, sus fuentes SVG y sus vistas artísticas: [CC0 1.0 Universal](ARTWORK-LICENSE). Las **diez imágenes descargadas y sus miniaturas** conservan sus licencias y atribuciones individuales, documentadas en [SOURCES.md](SOURCES.md); **no se relicencian bajo MIT ni CC0**. La plancha conjunta es una colección de esas obras, no una renuncia a sus derechos. Instalar el tema no ejecuta el generador ni requiere sus dependencias.

Las atribuciones obligatorias, los enlaces de licencia y la dedicación de los originales también están incluidos en **`LICENSE`**, para que acompañen a los fondos incluso si un instalador selectivo no copia `SOURCES.md` o `ARTWORK-LICENSE`.
