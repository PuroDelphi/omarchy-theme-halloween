# Halloween for Omarchy

A dark Halloween theme: pumpkin orange, amethyst, ivory and potion green on near-black surfaces. **14 still wallpapers: 10 licensed third-party downloads + 4 wallpapers created for this project**. The four project-created wallpapers are **2 procedural vector illustrations at 4K (11–12)** and **2 FLUX-generated photographic-style horror scenes at native 2048 × 1152 (13–14)**.

![Updated Halloween desktop: vivid pumpkin-orange terminal colors, orange bar, Foot, Neovim and Don't Look at the Glass wallpaper](preview.png)

Updated real desktop capture on **edge** with the **vivid ANSI palette**, unchanged **pumpkin-orange transparent bar**, **14-wallpaper collection** and **Don't Look at the Glass** background. Foot displays the actual generated orange, green, purple, red and cyan values; Neovim shows the real updated `colors.toml`. These are real application windows, not a montage. The wallpaper is fictional AI-generated artwork, not a photograph of a real person. [Earlier screenshot with Raven Manor](previews/desktop-mansion.png) · [Matching catalog WebP, 1200 × 675](previews/halloween.webp).

## Design and colors

`colors.toml` is the source of truth for the application palette. Omarchy generates configurations for terminals, Hyprland, Neovim, Helix, btop, browsers, editors and the shell from its templates. `shell.bar.toml` overrides only the bar's text color; the other shell surfaces keep their generated colors. Installed applications and local templates determine which integrations apply.

| Role | Color | Use |
| --- | --- | --- |
| Night | `#121016` | Main background |
| Void | `#08070C` | Deepest surface |
| Aubergine | `#251D2D` | Raised surfaces |
| Pumpkin | `#FF9A3C` | Unchanged bar text, accent, focus, actions and normal ANSI yellow |
| Border amethyst | `#BB9AF7` | Unchanged active-border endpoint |
| Spell purple | `#B06BF5` | Semantic purple and Foot's normal ANSI magenta slot |
| Ivory | `#F5E9D3` | Main text |
| Bone | `#FFF4DF` | Bright text and generated cursor |
| Gray lavender | `#9B8DA8` | Muted text |
| Plum | `#4B2E53` | Selection, with `#FFF4DF` text |
| Crimson | `#FF5263` | Errors and alerts |
| Potion | `#A8CF40` | Success and ANSI green |
| Flame | `#FFB05C` | Bright ANSI yellow, kept orange rather than cream |
| Blue moon | `#7F95F5` | ANSI blue |
| Spectral pink | `#E96AA9` | ANSI magenta in templates using the magenta token |
| Ectoplasm | `#3DCBB2` | ANSI cyan |

Active border: pumpkin → amethyst gradient at 45°. Inactive border: `#4B3A55`. The gradient is a color declaration, not an animation. Bright ANSI colors are defined separately. `icons.theme` selects **Yaru**, the orange variant available by default according to the manual.

The application palette now uses stronger, less pastel colored accents. Both normal and bright ANSI yellow stay pumpkin-orange; the top bar's **base setting** remains exactly `#FF9A3C`, with its native transparency and automatic contrast behavior preserved. Main ivory text, dark surfaces, selection and border colors are unchanged. Terminals receive these colors through Omarchy's normal generated templates, without global template overrides. Alacritty can reload the generated palette; open a new Foot window to use it. Wallpaper artwork, vector-art previews and the earlier Raven Manor screenshot retain their original artistic colors; no wallpaper was recolored. The main desktop preview now shows the revised application palette.

The clock and theme-aware monochrome bar icons use **pumpkin orange `#FF9A3C`** through the native `shell.bar.toml` section override. Application and popup text remains ivory; full-color application/tray icons retain their own artwork.

The normal transparency toggle is preserved. In transparent mode, **Omarchy's automatic contrast adjustment can replace orange with a dark color** when the sampled wallpaper strip is bright, including **The Last Corridor**. This theme does not disable that adjustment or force the bar to stay transparent. Orange is the base color, not a fixed-color guarantee over every wallpaper or window.

Contrast ratios calculated using sRGB relative luminance (WCAG): text/background **15.73:1**, muted/background **6.09:1**, accent/background **8.94:1**, selection **10.61:1**. These compare solid colors: they do not certify text over every part of an image or every application's transparency settings.

## Installable layout

The repository root is the theme root, without an additional enclosing directory:

```text
omarchy-theme-halloween/
├── colors.toml              # Semantic palette
├── icons.theme              # Yaru
├── shell.bar.toml           # Pumpkin-orange bar text; native contrast behavior retained
├── backgrounds/             # 10 downloads + 2 4K vector illustrations + 2 2K AI images
├── optional/                # Opt-in animated wallpaper; excluded from the default set
├── artwork/                 # SVG sources for the original vector illustrations
├── preview.png              # Real desktop screenshot, 16:9
├── previews/                # Second screenshot, WebP, artwork and contact sheets
├── tools/                   # Regeneration of the two vector illustrations
├── LICENSE                  # MIT: configuration, tools and documentation
├── ARTWORK-LICENSE          # CC0 dedication: four project-created works and listed derivatives
├── SOURCES.md               # Author, source and license for each download
├── sources/                 # Provenance metadata
└── README.md
```

All fourteen final files are in `backgrounds/`: thumbnails and source files do not appear in the wallpaper selector. Downloads retain their source resolution, without artificial upscaling. See [`SOURCES.md`](SOURCES.md) for titles, authors, dimensions and licenses, and [`previews/contact-sheet.png`](previews/contact-sheet.png) to view the collection.

## Four project-created wallpapers (11–14)

The project-created collection contains **four still wallpapers**, grouped by how they were made. The ten downloaded photographs are separate and retain their own licenses.

### Vector illustrations (11–12)

Files **11** and **12** are the project's own procedural creations, not downloads or recolored photographs. Their editable SVG sources are in `artwork/`, and their final PNGs are **3840 × 2160 pixels**. [`previews/originals-contact-sheet.png`](previews/originals-contact-sheet.png) shows only these two works; [`previews/theme-art-preview.png`](previews/theme-art-preview.png) keeps their artistic presentation separate from the real screenshots.

- **11 — Midnight Pumpkin Harvest:** a nighttime harvest, candlelight and Halloween silhouettes.
- **12 — Raven Manor:** haunted architecture, warm windows and an amethyst sky.

### FLUX-generated horror scenes (13–14)

Wallpapers **13 and 14** use a photographic rather than cartoon style. They were **generated with FLUX.1 [schnell]**, depicting unsettling faces, damp surfaces, decay and cold lighting. These are fictional scenes created for the theme: **not photographs of real people** or output from the SVG generator.

- **[13 — The Last Corridor](backgrounds/13-the-last-corridor.webp):** a dark-eyed presence with wet hair in an abandoned corridor, with fluorescent lighting and floor reflections.
- **[14 — Don't Look at the Glass](backgrounds/14-dont-look-at-the-glass.webp):** a threatening face beside wet glass, with a hand in the foreground.

Both FLUX-generated scenes are included as **original WebP files, 2048 × 1152, 16:9**, without artificial upscaling, retouching or recomposition. Together with the two vector illustrations, they make up the **four project-created wallpapers**; all ten downloaded photographs remain included.

![The two additional AI-generated horror wallpapers](previews/horror-contact-sheet.jpg)

They were generated using the [official public Black Forest Labs Space](https://huggingface.co/spaces/black-forest-labs/FLUX.1-schnell). Full prompts, seeds, model version, parameters and SHA-256 hashes are in [`sources/13-14-generated.json`](sources/13-14-generated.json). Installing or using the included wallpapers requires no connection, account, generator or model.

Apache-2.0 licenses the **model**; it is not presented as a guarantee of exclusive rights over its outputs. The project's contribution to these images is dedicated under CC0 to the extent rights exist; see `ARTWORK-LICENSE`.

### Regenerating the vector illustrations

The PNGs are already included; this is only for artwork development. It requires **Python 3** and **`rsvg-convert`**, from Arch's `librsvg` package. No network access or additional Python packages are needed.

```bash
python tools/render-wallpapers.py
```

The command regenerates only the two **vector originals, 11 and 12**: their SVG sources, 3840 × 2160 PNGs and artistic previews in `previews/`. **It does not overwrite `preview.png`, the real screenshots or wallpapers 13 and 14.** It does not download, replace or delete the ten photographs. To generate a scene at another resolution in a separate directory:

```bash
python tools/render-wallpapers.py --scene 11 --width 1920 --height 1080 --output-dir /tmp/halloween-art
```

`--sources-only` generates only the sources; `--help` describes the options. Keep the two original 4K PNGs when distributing the theme. The desktop crops the image to fill each monitor, so other aspect ratios may hide details near the edges.

## Local installation

From this project's root:

```bash
mkdir -p "$HOME/.config/omarchy/themes"
ln -sT -- "$PWD" "$HOME/.config/omarchy/themes/theme-halloween"
omarchy theme set theme-halloween
```

If `~/.config/omarchy/themes/theme-halloween` already exists, `ln -sT` will not replace it: inspect that destination before continuing. The link lets you edit the project and reapply the theme without copying files. **The last command changes the active desktop.** No `sudo`, changes to `/usr/share/omarchy/` or session restart are needed.

To cycle through the fourteen wallpapers:

```bash
omarchy theme bg next
```

To switch back, consult `omarchy theme list` and apply your previous theme's name with `omarchy theme set`. Installing or creating this repository alone does not change your desktop.

## Installation from GitHub

```bash
omarchy theme install https://github.com/PuroDelphi/omarchy-theme-halloween
```

This command downloads **and applies** the theme. To select it again:

```bash
omarchy theme set theme-halloween
```

The requested repository is named `omarchy-theme-halloween`: Omarchy removes the `omarchy-` prefix, so its installed identifier is **`theme-halloween`**, not `halloween`. The owner's chosen repository name is retained, although it differs from the recommended `omarchy-[name]-theme` convention.

## Optional animated edition

The **default edition** contains the fourteen still wallpapers above. The **animated edition** uses [`optional/halloween-jumpscare.webm`](optional/halloween-jumpscare.webm), a **15.042-second, 736 × 400, 24 fps, silent** VP9 video supplied by the repository owner: the figure from **13 — The Last Corridor** moves toward the viewer, ending in a close-up scare with reaching hands and broken-glass imagery. Scene 14 is not animated in this version. There is no executable installer, plugin, service or hook.

**Low-resolution source:** the export preserves all 361 frames at the supplied clip's native dimensions, without upscaling, cropping, interpolation or added transitions. Full-screen playback will look softer than the still wallpapers. Playback repeats with a visible reset; the ending does not match the opening, so this is **not a seamless loop**. The original MP4 remains unchanged locally; its audio and attached cover image are excluded from the wallpaper export.

**Created with Grok.** The repository owner generated this animation with Grok and authorized its publication. Grok's [output-ownership guidance](https://x.ai/legal/faq#who-owns-the-inputs-to-and-outputs-from-grok) says users own their outputs and may use them commercially; its [brand guidelines](https://x.ai/legal/brand-guidelines) request this attribution. This is an AI-generated fictional scene, not real footage or an endorsement by Grok. The supplied animation is not automatically relicensed under the still image's CC0 dedication; see [provenance and rights](SOURCES.md#optional-animated-wallpaper).

**Compatibility requirement:** use an Omarchy build with native **OWE video wallpaper support**, as documented in the [official background manual](https://github.com/omacom/omarchy/blob/quattro/manual/39-backgrounds.md). The tested stable **4.0.5-1** build cannot play this edition. Development builds on the **edge** channel include video support; the feature is tracked under the [4.5 milestone](https://github.com/omacom/omarchy/pull/6792). **Switching channels updates the system, not just the wallpaper, and development builds can break.** See the [official channel guidance](https://github.com/omacom/omarchy/blob/quattro/manual/30-updates.md). An experimental channel is not required for the static theme.

The video deliberately lives **outside `backgrounds/`**. Installing the theme does not enable it or add it to the wallpaper cycle. A marketplace install may omit `optional/` entirely; download the media explicitly using the instructions below.

### Enable

**Only users who want animation need to opt in.** Installing Halloween does not activate the video. With a compatible Omarchy build and **Halloween installed and selected**, download and select the silent WebM once:

```bash
video="$HOME/.config/omarchy/backgrounds/theme-halloween/halloween-jumpscare.webm"
mkdir -p "$HOME/.config/omarchy/backgrounds/theme-halloween"
curl --fail --location --output "$video" \
  https://raw.githubusercontent.com/PuroDelphi/omarchy-theme-halloween/main/optional/halloween-jumpscare.webm &&
  omarchy theme bg set "$video"
```

If you already cloned this repository, you can copy the same file instead of downloading it. Run this alternative **from the repository root**:

```bash
video="$HOME/.config/omarchy/backgrounds/theme-halloween/halloween-jumpscare.webm"
mkdir -p "$HOME/.config/omarchy/backgrounds/theme-halloween" &&
  cp optional/halloween-jumpscare.webm "$video" &&
  omarchy theme bg set "$video"
```

Use **`halloween-jumpscare.webm`**, not the original `pasillo.mp4`, which retains its audio. Once the WebM is in the user background folder, select it with **`Super + Ctrl + Space`** whenever you want it; you do not need to rerun the download or copy command.

**The last command immediately selects the animated wallpaper.** After installation, it also appears in the normal background picker/cycle. The effect stays behind application windows; it is not an on-top popup. Omarchy may preserve the selected wallpaper across logins and also display its video on the lock screen, depending on the version. Video consumes more power than a still; consumption has not been measured here.

### Stop playback and keep the video

Choose a still image with **`Super + Ctrl + Space`**, or return directly to the original corridor image:

```bash
omarchy theme bg set \
  "$HOME/.config/omarchy/themes/theme-halloween/backgrounds/13-the-last-corridor.webp"
```

Selecting a still stops video playback without changing the theme or deleting the optional file. The video remains available in the picker for later use.

The fourteen default wallpapers remain installed. No daemon, plugin, configuration entry or autostart needs removing.

### Remove the optional video

After selecting a still as shown above, remove the optional file only if you no longer want it offered when cycling backgrounds:

```bash
rm -f -- "$HOME/.config/omarchy/backgrounds/theme-halloween/halloween-jumpscare.webm"
```

### Listing policy

The [theme registry](https://github.com/omacom/omarchy-theme-registry#what-gets-checked) recognizes video backgrounds. Its [validator](https://github.com/omacom/omarchy-theme-registry/blob/master/packages/validator/src/validate.ts) issues a `BACKGROUND_VIDEO` resource warning for videos under `backgrounds/`, not an automatic rejection. This opt-in asset is outside that directory and needs no executable code. **Neither the manual nor the validator guarantees maintainer approval or inclusion among Omarchy's bundled themes.**

Source hashes, the exact production command and qualified artwork rights are documented in [`sources/optional-jumpscare.json`](sources/optional-jumpscare.json), [`SOURCES.md`](SOURCES.md) and [`ARTWORK-LICENSE`](ARTWORK-LICENSE).


## Distribution and approval

1. Distribution repository: **[PuroDelphi/omarchy-theme-halloween](https://github.com/PuroDelphi/omarchy-theme-halloween)**. Its root directly contains the palette and `backgrounds/`.
2. Check installation from that URL using **Install → Style → Theme** or the command above. The resulting identifier should be `theme-halloween`.
3. `preview.png` contains a real screenshot with a terminal and Neovim; `previews/desktop-mansion.png` shows a second scene. They were reviewed before publication to exclude private windows, usernames, notifications and the mouse pointer.
4. Website catalog submission: **[omacom/omarchy-site#586](https://github.com/omacom/omarchy-site/pull/586)**, with the required WebP screenshot and alphabetical entry.

**Installable ≠ accepted into the catalog ≠ bundled by default.** The manual provides a community-theme catalog route; it does not promise to make a submission an official distribution theme. Acceptance is up to the maintainers. Publishing on GitHub does not itself mean a catalog submission has been made or approved.

The theme uses the semantic format of the reference installation, **Omarchy 4.0.5-1**. Compatibility with earlier editions using other configuration formats is not guaranteed.

### Community submissions

- **Website catalog:** [PR #586](https://github.com/omacom/omarchy-site/pull/586). The submission locally passed build, lint, type checks, **51 Node + 45 Python tests**, static parity and visual browser inspection of the catalog. These local checks are not remote checks or maintainer approval.
- **Marketplace registry:** [submission #128](https://github.com/omacom/omarchy-theme-registry/issues/128), including the URL, name, rights/privacy confirmations and real screenshots. The account lacks permission to add the `submission` label; a maintainer was asked to apply it and trigger validation. No claim is made that the remote validator approved the theme.
- Both submissions describe the theme's included content. Follow their links for the maintainers' current decisions; submission does not imply immediate catalog listing.

### Website catalog: specific requirements

According to the site's [“Adding your theme” instructions](https://github.com/omacom/omarchy-site#adding-your-theme), the PR must include:

- A **real 16:9 screenshot** showing a terminal, editor and a theme wallpaper, without a cursor, notifications or private information. An illustration or empty desktop is not a substitute.
- That screenshot converted to WebP at `assets/themes/halloween.webp`, targeting **1200 × 675** and approximately **under 100 KB**, without upscaling a small screenshot.
- A `<figure class="themes__theme">` block in **`themes/index.html`**, in alphabetical order. Both image and title must link to `https://github.com/PuroDelphi/omarchy-theme-halloween`.

The site generates its data from that HTML: do not edit `src/data/themes.json` as the submission source. A PR without a screenshot cannot be merged. `previews/halloween.webp` is the refreshed real screenshot prepared for this submission: **1200 × 675, quality 80, 50,808 bytes**. The separate artistic preview must not be confused with the screenshot.

### Marketplace: a separate registration route

[themes.omarchy.org](https://themes.omarchy.org) also has its [own registry and instructions](https://github.com/omacom/omarchy-theme-registry). Its [Submit a theme](https://github.com/omacom/omarchy-theme-registry/issues/new?template=submit-theme.yml) form requests the URL, allows **Halloween** as the display name and requires confirmation of authorship/permissions and absence of private data. The bot validates and proposes a PR; the final decision remains with a maintainer.

The registry requires the palette and wallpapers at the theme root and a 16:9 `preview.png` at least 1000 pixels wide. It rejects symbolic links, images larger than 50 MB or 40 megapixels, and repositories larger than 400 MB, among other errors. README, LICENSE and the `omarchy-theme` topic are recommended. An unconventional repository name and generation tools may produce **warnings**, not necessarily errors. The local installation symlink is not part of the repository or its download.

The registry may assign a different identifier if the name is already taken. Installation by name/validated commit belongs to that system; the verified local installation uses the **full Git URL**, without assuming `omarchy theme install halloween` is available.

### Bundling by default

Bundled themes are in `themes/` in the [Omarchy project](https://github.com/omacom/omarchy). No specific policy was found guaranteeing acceptance of a new theme into that collection. The project directs suggestions to [Discussions](https://github.com/omacom/omarchy/discussions), rather than bug issues. Publication and community catalogs do not imply inclusion in the distribution.

### What a downloaded theme should not need

In the version consulted, a theme cloned with `omarchy theme install` cannot supply Lua, terminal configurations (`alacritty.toml`, `foot.ini`, `ghostty.conf`, `kitty.conf`) or `vscode.json`: Omarchy excludes them from staging and regenerates them from the palette. They are not included here. There is also no executable installer, autostart hook or mandatory extension.

## Verification performed

Initial validation environment: **stable Omarchy 4.0.5-1**, as reported by the installed package. The initial collection was tested in a real graphical session; the expansion to 14 wallpapers was additionally checked with an isolated installation. The current primary preview and vivid ANSI revision were captured and checked on **edge, Omarchy 4.0.0.r7080.g60f5b49-1**.

- Full decoding of all **14 wallpapers**, dimension checks and absence of binary duplicates: passed.
- **10 downloads** at their source resolution, between 3264 and 6000 pixels wide; **2 vector illustrations** at 3840 × 2160 and **2 AI-generated horror images** at native 2048 × 1152, without upscaling. The last two images' hashes match the generation record.
- Actual generator execution for scene 11 at **1920 × 1080** in a temporary directory: passed.
- Actual installation with `omarchy theme install` from a temporary Git repository containing the project, using **isolated HOME and XDG paths** and `OMARCHY_THEME_HEADLESS=1`: exit 0, identifier **`theme-halloween`** and all **14 wallpapers available**, including both new WebPs intact. It did not change the active desktop.
- During the initial installation: **19 configurations** generated by the installed templates, without unresolved variables; JSON/TOML outputs parsed successfully.
- `foot --check-config` on its generated configuration: exit **0**.
- Visual review of the two vector illustrations, the two AI-generated horror images and the **fourteen-wallpaper** contact sheet.
- Installation from the public URL and actual application in Hyprland: **Theme Halloween**; `hyprctl configerrors` reported no errors. The refreshed primary screenshot on edge shows **Don't Look at the Glass**, the unchanged orange transparent bar, Neovim displaying the actual revised `colors.toml`, and a Foot terminal displaying the installed development version, fourteen-wallpaper count and generated vivid palette values.
- Real visual inspection of **Foot, Neovim, borders and wallpaper**, with two desktop screenshots. Not all other applications have been visually tested.
- Screenshots came from the native **1366 × 768** monitor, minimally cropped by 3 pixels on each side and 1/2 pixels at the top/bottom to **1360 × 765**, without upscaling or distortion. The current WebP was reduced to **1200 × 675**, quality **80**, stripped metadata, **51,702 bytes**.
- English filename migration, local Markdown link targets and AI-image provenance hashes: checked. The translated renderer generated scene 11 successfully at 1920 × 1080.
- Repeated the isolated Omarchy installation after the English cutover: **14 still wallpapers**, with no optional video in the default background cycle or selected as the active background.
- Replacement optional WebM: all **361 frames** decoded, **736 × 400 / 24 fps / 15.042 seconds**, one VP9 video stream and **no audio**. A complete FFplay playback run with SDL's dummy output exited successfully, and sampled frames were visually reviewed. The supplied MP4 and all fourteen still wallpapers remain unchanged. Native OWE wallpaper playback was **not** tested on the installed stable build.
- Before the corridor-video replacement, ran the official registry's `validateTheme` implementation locally: **passed, zero errors**. It reported advisories for the unconventional repository name, palette keys unknown to that registry version, the 26.31 MiB still collection, and the existing development renderer. There was **no `BACKGROUND_VIDEO` warning** because the optional clip was outside `backgrounds/`; the replacement retains that layout. The registry validator has not been rerun for this replacement. Local validation is not remote acceptance or maintainer approval.
- Bar-only orange override: installed through the real Omarchy installer in an isolated HOME, confirming orange bar text with unchanged application, popup and control colors. Applied to the live desktop without changing the wallpaper or `shell.json`; the clock and monochrome icons were visually checked with transparency enabled. The native contrast helper kept orange for 13 of the 14 supplied wallpapers at a 1920 × 1080 top-bar sample and chose dark text for **The Last Corridor**, consistent with the retained automatic behavior.
- Vivid ANSI revision on **edge**: ran the real Omarchy template generator in an isolated HOME and passed `foot --check-config`. Applied the palette with `omarchy theme refresh` and visually inspected native ANSI output in a real Alacritty window: normal yellow is **`#FF9A3C`**, bright yellow is **`#FFB05C`**, and the other colored accents are stronger rather than near-white pastels. The revised colored accents have at least **5.64:1** contrast against the solid `#121016` background. The bar section, global `shell.json` and selected wallpaper remained unchanged. The temporary comparison window and private captures were removed; the user's windows were preserved.

The wallpapers total **26.31 MiB**. Originals are retained without additional compression: this slightly exceeds the registry's advisory 25 MiB warning threshold, but every image meets its hard limits of 50 MB and 40 megapixels. A community submission does not imply acceptance or bundling by default.

## Primary sources

- [Manual: making and distributing a theme](https://omarchy.org/manual/making-your-own-theme/).
- [Community theme catalog](https://omarchy.org/themes/).
- [Omarchy repository](https://github.com/omacom/omarchy): `omarchy-theme-install`, `omarchy-theme-set`, `omarchy-theme-set-templates` and `omarchy-theme-color` commands.
- [Website repository](https://github.com/omacom/omarchy-site): catalog contribution route. The manual may retain links using an older organization name; the catalog links to `omacom`.
- [Exact catalog instructions](https://github.com/omacom/omarchy-site#adding-your-theme) and [marketplace registry](https://github.com/omacom/omarchy-theme-registry).

## Licensing and provenance

The **14 still wallpapers** consist of **10 third-party downloads and 4 project-created works (11–14)**. The four project-created works are grouped below by provenance and licensing:

| Group | Files | License / dedication |
| --- | --- | --- |
| 2 procedural vector illustrations | 11–12, their SVG sources and vector previews | [CC0 1.0 Universal](ARTWORK-LICENSE) |
| 2 FLUX-generated horror scenes | 13–14 and their comparison preview | Project contribution dedicated under [CC0 only to the extent applicable rights exist](ARTWORK-LICENSE), without a promise of exclusivity or copyright protection |
| 10 downloaded photographs | 01–10 and their thumbnails | Their individual source licenses and attribution in [SOURCES.md](SOURCES.md); **not relicensed by the project** |

Configuration, tools and documentation use [MIT](LICENSE). The optional video is an **owner-supplied Grok animation of scene 13**, not a fifth independently created still wallpaper. **Created with Grok**; its provenance and links to the provider's output guidance and attribution requirements are in [SOURCES.md](SOURCES.md#optional-animated-wallpaper). No blanket MIT or CC0 license is asserted for the supplied animation itself. The qualified dedication of the underlying still is unchanged. Contact sheets are presentations of existing works, not additional wallpapers or waivers of the depicted works' rights. Installing the theme does not run generators or require their dependencies.

Required attribution, license links and the dedication of the four project-created works are also included in **`LICENSE`**, so they accompany the wallpapers even if a selective installer does not copy `SOURCES.md` or `ARTWORK-LICENSE`.
