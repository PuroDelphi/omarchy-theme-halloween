#!/usr/bin/env python3
"""Original CC0 Halloween illustrations; standard library + rsvg-convert only.

Run: python tools/render-wallpapers.py
Options: --scene 11, --width 3840 --height 2160, --sources-only.
No network, external assets, fonts or changes to desktop configuration.
"""
from __future__ import annotations

import argparse
import html
import math
from pathlib import Path
import random
import shutil
import subprocess

W, H = 1920, 1080
BG = '#121016'
INK = '#0C0C13'
PLUM = '#4B2E53'
ORANGE = '#FF9A3C'
GOLD = '#FFD166'
CREAM = '#F5E9D3'
PURPLE = '#BB9AF7'
GREEN = '#B5D66F'
CYAN = '#7ED6C4'
SCENES = [
    ('11', 'campo-de-calabazas', 'La cosecha de medianoche'),
    ('12', 'mansion-del-cuervo', 'La mansión del cuervo'),
]


def tag(name, **attrs):
    attrs = ' '.join(f'{k.replace("_", "-")}="{html.escape(str(v), quote=True)}"' for k, v in attrs.items())
    return f'<{name} {attrs}/>'


def path(d, fill=INK, stroke=None, sw=1, **attrs):
    return tag('path', d=d, fill=fill, **({'stroke': stroke, 'stroke_width': sw} if stroke else {}), **attrs)


def rect(x, y, w, h, fill, **attrs):
    return tag('rect', x=x, y=y, width=w, height=h, fill=fill, **attrs)


def circle(x, y, r, fill, **attrs):
    return tag('circle', cx=x, cy=y, r=r, fill=fill, **attrs)


def ellipse(x, y, rx, ry, fill, **attrs):
    return tag('ellipse', cx=x, cy=y, rx=rx, ry=ry, fill=fill, **attrs)


def line(x1, y1, x2, y2, color, sw=1, **attrs):
    return tag('line', x1=x1, y1=y1, x2=x2, y2=y2, stroke=color, stroke_width=sw, **attrs)


def group(parts, transform='', **attrs):
    extra = ' '.join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<g transform="{transform}" {extra}>' + ''.join(parts) + '</g>'


def defs():
    return '''<defs>
    <linearGradient id="sky" x2="0.9" y2="1"><stop stop-color="#121016"/><stop offset=".56" stop-color="#1C1828"/><stop offset="1" stop-color="#3A263B"/></linearGradient>
    <linearGradient id="stone" x2="1" y2=".2"><stop stop-color="#201D2B"/><stop offset=".6" stop-color="#343044"/><stop offset="1" stop-color="#181723"/></linearGradient>
    <linearGradient id="pumpkin" x2="1" y2=".7"><stop stop-color="#9C4B2D"/><stop offset=".4" stop-color="#D47737"/><stop offset=".72" stop-color="#AC522E"/><stop offset="1" stop-color="#593027"/></linearGradient>
    <radialGradient id="halo"><stop stop-color="#FFD166" stop-opacity=".16"/><stop offset=".6" stop-color="#FF9A3C" stop-opacity=".035"/><stop offset="1" stop-color="#FF9A3C" stop-opacity="0"/></radialGradient>
    <radialGradient id="vignette"><stop offset=".4" stop-color="#090911" stop-opacity="0"/><stop offset="1" stop-color="#090911" stop-opacity=".55"/></radialGradient>
    <pattern id="hatch" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(32)"><path d="M0 0V14" stroke="#F5E9D3" stroke-width=".7" opacity=".04"/></pattern>
    </defs>'''


def sky(seed, moon_pos=(1450, 230), moon_r=105):
    rng = random.Random(seed)
    p = [rect(0, 0, W, H, 'url(#sky)')]
    for _ in range(105):
        x, y = rng.uniform(50, 1880), rng.uniform(45, 690)
        p.append(circle(round(x, 1), round(y, 1), rng.choice([.7, 1, 1.5]), CREAM, opacity=rng.uniform(.08, .35)))
    if moon_pos:
        x, y = moon_pos
        p += [circle(x, y, moon_r * 3, 'url(#halo)'), circle(x, y, moon_r, '#D5BE91')]
        for _ in range(24):
            a = rng.uniform(0, math.tau)
            r = rng.uniform(0, moon_r * .8)
            p.append(circle(x + math.cos(a)*r, y + math.sin(a)*r, rng.uniform(2, 12), '#9B8D81', opacity='.19'))
        p += [circle(x, y, moon_r + 12, 'none', stroke=GOLD, stroke_width='.7', opacity='.15')]
    # Engraved, horizontally drifting cirrus layers.
    for y, x in [(235, 90), (370, 380), (520, 25)]:
        p += [path(f'M{x} {y}q180 -24 340 0t360 0t360 0', 'none', '#66566F', 1, opacity='.13'),
              path(f'M{x+45} {y+8}q170 -18 330 0t340 0', 'none', '#66566F', 1, opacity='.1')]
    return p


def hills(seed=1, ground=780):
    rng = random.Random(seed)
    p = []
    for y, col, amp in [(ground-120, '#30263D', 100), (ground-45, '#211D2D', 60), (ground+35, '#171520', 50)]:
        ys = [int(y+rng.uniform(-amp, amp)) for _ in range(6)]
        d = f'M-100 {ys[0]}'
        for i in range(1, 6):
            d += f' Q{i*400-300} {ys[i-1]-65} {i*400-100} {ys[i]}'
        p.append(path(d+' L2000 1080H-100Z', col))
    return p


def bat(x, y, s=1, rot=0):
    return group([path('M-30 4Q-24 -15 -12 -10L-5 0L-3 -7L0 -3L3 -7L5 0L12 -10Q24 -15 30 4Q18 -3 16 10Q8 3 0 12Q-8 3 -16 10Q-18 -3 -30 4Z')], f'translate({x} {y}) rotate({rot}) scale({s})')


def tree(x, y, s=1, flip=1, color=INK):
    trunk = path('M-25 0Q-4 -130 -20 -245Q-33 -310 -16 -414L2 -432Q-8 -326 11 -248Q31 -120 31 0Z', color)
    branches = [
        'M-2 -241Q-76 -285 -126 -365L-159 -393M-83 -315L-77 -370M-117 -350L-177 -356',
        'M2 -301Q62 -339 90 -421L119 -447M66 -368L36 -407M88 -414L84 -457',
        'M15 -152Q87 -222 160 -240L189 -281M105 -223L113 -279M158 -239L205 -231',
        'M-2 -207Q-65 -207 -122 -248L-150 -248M-85 -225L-94 -267',
    ]
    p = [trunk]
    for d in branches:
        p.append(path(d, 'none', color, 13, stroke_linecap='round', stroke_linejoin='round'))
    p.append(path('M8 -38Q-9 -124 -2 -196M-9 -261Q-20 -320 -10 -373', 'none', '#4A3A4D', 2, opacity='.55'))
    return group(p, f'translate({x} {y}) scale({s*flip} {s})')


def pumpkin(x, y, s=1, face=False, tilt=0):
    p = [ellipse(0, 14, 66, 17, '#090911', opacity='.55'),
         path('M-4 -60Q-12 -86 5 -93L15 -89Q0 -80 5 -61Z', '#707445'),
         ellipse(-25, -23, 32, 41, 'url(#pumpkin)'), ellipse(25, -23, 32, 41, 'url(#pumpkin)'),
         ellipse(0, -24, 34, 45, 'url(#pumpkin)')]
    for z in [-30, -13, 13, 30]:
        p.append(path(f'M{z/2} -63Q{z*1.5} -24 {z*.7} 16', 'none', '#6B3429', 1.7, opacity='.65'))
    if face:
        p += [path('M-35 -23L-15 -39L-9 -18Z M10 -18L17 -39L37 -23Z', GOLD),
              path('M-33 -3L-17 1L-10 -5L-3 4L5 -4L14 0L30 -5L22 10L-18 12Z', GOLD)]
    else:
        p.append(path('M-40 -40Q-34 -53 -21 -55', 'none', '#F2B061', 2, opacity='.4'))
    return group(p, f'translate({x} {y}) rotate({tilt}) scale({s})')


def arch(x, y, w, h, fill, stroke='#66516B', sw=2):
    return path(f'M{x} {y+h}V{y+w/2}Q{x+w/2} {y-w/2} {x+w} {y+w/2}V{y+h}Z', fill, stroke, sw)


def window(x, y, w=45, h=95, glow=True):
    p = [arch(x, y, w, h, '#B4783B' if glow else '#11111B', '#514153', 3)]
    p += [line(x+w/2, y+8, x+w/2, y+h, '#29212B', 4), line(x+2, y+h*.6, x+w-2, y+h*.6, '#29212B', 4)]
    return ''.join(p)


def fence(x, y, n, step=28, h=100):
    p = [line(x, y-h*.35, x+n*step, y-h*.35, '#38303E', 4), line(x, y-h*.75, x+n*step, y-h*.75, '#38303E', 3)]
    for i in range(n+1):
        z = x+i*step
        p += [line(z, y, z, y-h, '#28232E', 5), path(f'M{z-6} {y-h+8}L{z} {y-h-8}L{z+6} {y-h+8}Z', '#3A303F')]
    return ''.join(p)


def grass(seed, y=1020, n=65):
    rng = random.Random(seed)
    p = []
    for _ in range(n):
        x = rng.uniform(-40, 1950)
        h = rng.uniform(14, 48)
        p.append(path(f'M{x:.1f} {y+30}q-8 {-h:.1f} -21 {-h-15:.1f}M{x:.1f} {y+30}q3 {-h:.1f} 16 {-h-12:.1f}', 'none', '#3D3141', 2, opacity='.5'))
    return p


def scene_11():
    p = sky(1, (1390, 215), 110) + hills(1, 720)
    for x, y, s in [(180, 739, .45), (400, 730, .6), (1750, 774, .8), (1870, 790, 1)]:
        p.append(tree(x, y, s, color='#211C2C'))
    p.append(path('M1130 750Q1230 840 1450 1080H1130Q1120 900 1070 770Z', '#39303B'))
    # Crooked little harvest barn, distant and subordinate.
    p += [path('M870 737V608L955 555L1040 610V752Z', '#191622'), path('M849 615L955 539L1060 615L1038 620L955 567L874 626Z', '#0D0D15'), rect(934, 669, 44, 78, '#0C0C13'), window(942, 598, 24, 39)]
    for y, count, size in [(798, 11, .32), (866, 9, .58), (955, 7, .96), (1080, 5, 1.5)]:
        for i in range(count):
            x = 140+i*(1780/count)+math.sin(i*9+y)*30
            if 1020 < x < 1440:
                continue
            p.append(pumpkin(x, y, size, face=(i+y)%3 == 0, tilt=math.sin(i)*8))
    # Foreground vines and harvest leaves.
    for x in [240, 750, 1590, 1880]:
        p.append(path(f'M{x-80} 1045q75 -100 160 -25q30 30 -8 37q-35 0 -14 -24', 'none', '#687147', 3, opacity='.7'))
        p.append(path(f'M{x} 1005q-30 -52 -63 -31q8 38 63 31Z', '#414D35'))
    p += [bat(1515, 215, .8, -15), bat(1570, 170, .5, 12)]
    return p + grass(1)


def scene_12():
    p = sky(2, (1350, 260), 140) + hills(2, 850)
    p += [path('M840 1040Q1000 840 1220 792L1280 810Q1050 920 1010 1080Z', '#3C303D')]
    # Stacked asymmetrical Gothic massing.
    p += [rect(1110, 490, 460, 360, 'url(#stone)'), rect(1020, 370, 140, 480, '#282330'),
          path('M990 388L1090 188L1190 388Z', '#11121C', '#544153', 2),
          path('M1080 502L1330 330L1604 502Z', '#15141F', '#544153', 2),
          rect(1460, 430, 125, 420, '#272331'), path('M1430 446L1520 285L1616 446Z', '#13131D', '#544153', 2)]
    for i in range(8):
        p.append(line(1125, 535+i*40, 1545, 535+i*40, '#5A475C', 1, opacity='.25'))
    for x in [1190, 1280, 1390, 1495]:
        for y in [540, 670]:
            p.append(window(x, y, 42, 83, glow=(x+y)%3 != 0))
    p += [window(1066, 435, 44, 100), window(1075, 618, 36, 83, False), window(1304, 402, 46, 65),
          arch(1305, 738, 88, 115, '#10111A', '#635061', 5), line(1349, 760, 1349, 852, '#443342', 2),
          rect(1290, 850, 120, 12, '#423446'), rect(1275, 862, 155, 12, '#302837'), rect(1255, 874, 195, 14, '#25202E')]
    # Chimneys, finials, weather vane and a raven.
    p += [rect(1410, 345, 28, 100, '#24202D'), rect(1403, 342, 44, 10, '#423142'),
          line(1090, 190, 1090, 145, '#80604E', 3), line(1070, 163, 1118, 163, '#80604E', 2),
          path('M1507 287Q1488 276 1499 265Q1509 251 1520 263L1534 265L1522 271L1529 286Z')]
    p += [fence(820, 935, 10, 27, 105), fence(1450, 935, 17, 27, 105), tree(1800, 1040, 1.75, -1), tree(60, 1020, 1.5)]
    p += [pumpkin(1218, 914, .72, True), pumpkin(1570, 948, .6), bat(1260, 235, .9, 8), bat(1660, 341, .65, -14)]
    return p + grass(2)


GENERATORS = [scene_11, scene_12]


def document(parts, title, width=W, height=H):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
            f'<title>{html.escape(title)}</title>'
            '<desc>Ilustración procedural original Halloween. CC0 1.0. Sin recursos externos. No es una captura de escritorio.</desc>'
            + ''.join(parts) + '</svg>')


def finish(parts, seed):
    # Deterministic fine stipple: no raster assets or expensive SVG filters.
    rng = random.Random(seed+400)
    parts += [rect(0, 0, W, H, 'url(#hatch)')]
    for _ in range(1600):
        parts.append(circle(round(rng.uniform(0, W), 1), round(rng.uniform(0, H), 1), rng.choice([.4, .6, .8]), '#F5E9D3', opacity='.035'))
    parts += [rect(0, 0, W, H, 'url(#vignette)')]
    return parts


def text(x, y, value, size=20, fill=CREAM, **attrs):
    props = ' '.join(f'{k.replace("_", "-")}="{html.escape(str(v), quote=True)}"' for k, v in attrs.items())
    return f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{size}" fill="{fill}" {props}>{html.escape(value)}</text>'


def inline_scene(content, x, y, width, height):
    # Nested SVG keeps every local definition scoped to its own drawing.
    # Rename IDs because SVG fragment lookup is document-wide in librsvg.
    prefix = f'p{int(x)}x{int(y)}-'
    ids = ['sky', 'stone', 'pumpkin', 'halo', 'vignette', 'hatch']
    for name in ids:
        content = content.replace(f'id="{name}"', f'id="{prefix}{name}"').replace(f'url(#{name})', f'url(#{prefix}{name})')
    inner = content[content.index('>')+1:content.rindex('</svg>')]
    return f'<svg x="{x}" y="{y}" width="{width}" height="{height}" viewBox="0 0 1920 1080">{inner}</svg>'


def make_previews(root, sources, renderer):
    directory = root / 'previews'
    directory.mkdir(parents=True, exist_ok=True)
    # Full-width illustrations preserve the detail of the two original scenes.
    parts = [rect(0, 0, 1920, 2440, BG), text(60, 80, 'HALLOWEEN / DOS ORIGINALES', 36, GOLD, letter_spacing=5),
             text(60, 128, 'Vista de arte · NO son capturas de escritorio · CC0 1.0', 22, '#B7A6BE')]
    for i, ((number, slug, title), source) in enumerate(zip(SCENES, sources)):
        y = 175+i*1120
        parts += [inline_scene(source, 40, y, 1840, 1035), rect(40, y+1035, 1840, 50, '#211B29'),
                  text(60, y+1068, f'{number}  /  {title}', 24, CREAM)]
    contact = directory / 'originals-contact-sheet.svg'
    contact.write_text(document(parts, 'Halloween — dos originales CC0', 1920, 2440), encoding='utf-8')
    render(renderer, contact, directory / 'originals-contact-sheet.png', 1920, 2440)
    # Editorial art + palette, explicitly distinct from a desktop screenshot.
    parts = [rect(0, 0, 1920, 1080, BG),
             text(78, 87, 'HALLOWEEN', 58, GOLD, letter_spacing=10),
             text(82, 137, 'DOS ILUSTRACIONES ORIGINALES / PALETA DEL TEMA', 21, CREAM, letter_spacing=3),
             text(82, 178, 'Vista artística · NO es una captura de escritorio', 20, '#B7A6BE')]
    for i, source in enumerate(sources):
        x = 40+i*940
        parts += [inline_scene(source, x, 250, 900, 506.25),
                  text(x+12, 801, f'{SCENES[i][0]} / {SCENES[i][2]}', 22, CREAM)]
    palette = [BG, CREAM, ORANGE, PLUM, GOLD, '#FF667A', GREEN, PURPLE, '#ED96C3', CYAN]
    for i, color in enumerate(palette):
        x = 80+i*177
        parts += [rect(x, 910, 146, 54, color, rx=3, stroke='#69516C', stroke_width=1), text(x, 996, color, 18, '#CABBCB')]
    parts += [text(80, 1045, 'DOS ORIGINALES CC0 1.0 · SVG EDITABLES · PNG 3840 × 2160', 18, '#B7A6BE', letter_spacing=2)]
    preview = directory / 'theme-art-preview.svg'
    preview.write_text(document(parts, 'Halloween — arte y paleta, no captura de escritorio'), encoding='utf-8')
    render(renderer, preview, root / 'preview.png', 1920, 1080)


def render(renderer, source, destination, width, height):
    subprocess.run([renderer, '--width', str(width), '--height', str(height), '--output', str(destination), str(source)], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--scene', choices=['all']+[s[0] for s in SCENES], default='all', help='Escena numerada; all también regenera las vistas previas')
    parser.add_argument('--width', type=int, default=3840)
    parser.add_argument('--height', type=int, default=2160)
    parser.add_argument('--sources-only', action='store_true', help='Escribir únicamente las dos fuentes SVG, sin rasterizar')
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parents[1], help='Raíz de salida; por defecto, raíz del repositorio')
    args = parser.parse_args()
    if args.width <= 0 or args.height <= 0:
        parser.error('Las dimensiones deben ser positivas')
    renderer = None if args.sources_only else shutil.which('rsvg-convert')
    if not args.sources_only and renderer is None:
        parser.error('Se necesita rsvg-convert (paquete librsvg); no se instala automáticamente')
    root = args.output_dir.resolve()
    (root / 'artwork').mkdir(parents=True, exist_ok=True)
    if not args.sources_only:
        (root / 'backgrounds').mkdir(parents=True, exist_ok=True)
    sources = []
    for i, ((number, slug, title), generator) in enumerate(zip(SCENES, GENERATORS)):
        if args.scene not in ('all', number):
            continue
        source = document([defs()]+finish(generator(), i), title)
        sources.append(source)
        destination = root / 'artwork' / f'{number}-{slug}.svg'
        destination.write_text(source, encoding='utf-8')
        if renderer:
            render(renderer, destination, root / 'backgrounds' / f'{number}-{slug}.png', args.width, args.height)
        print(f'{number} {title}', flush=True)
    if renderer and args.scene == 'all':
        make_previews(root, sources, renderer)


if __name__ == '__main__':
    main()
