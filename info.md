# FiraCode Nerd Font

- 2025-01 Actualizado a Nerd Font 3.3.0

> Fira Code: free monospaced font with programming ligatures

Mi pregunta: https://github.com/ryanoasis/nerd-fonts/discussions/1471

La regular tiene todo monospaced menos algunos íconos para que no sean tan
pequeños por lo que se hace necesario agregar un espacio extra para no
sobreponerlos con letras.

Se puede descargar la fuente ya parcheada de nerd fonts y usarla directamente o
bajarla desde el repo FiraCode y parchearla manualmente.

Últimamente, y ha funcionado muy bien, simplemente usar la de NerdFonts como
base.

> Es necesario copiar la fuente bold también.

## Usando la fuente de NerdFonts:

1. Descargamos y extraemos la fuente FiraCode ya modificada (usar medium y
   bold): https://www.nerdfonts.com/font-downloads

2. Modificamos los glifos ss03 y ss05 aquí:
   https://mutsuntsai.github.io/fontfreeze/ Opcional: Font family suffix: FIX

3. Agregamos el prompt:

Abrir la fuente FiraCode con FontForge y **con la misma sesión** abrir la otra
fuente. Ahí se puede copiar sin problemas el glifo.

El cohete está en seguisym (Windows 7 font) seguisym -> SegoeUISymbol u1F680
128640

> Son miles de glifos asíque usar menú "Ver" -> "ir a" Origen: `U+1F680`
> Destino: `U+F135`

La posición u1f680 es usado por emojis y eso puede hacer que no se respete la
versión de esta fuente sino otra específica de emojis, por ello usamos uf135.

En esta iteración no se ha ajustado la _width_ de la fuente a 1200.

4. Ajustar metadata de las fuentes.

Cuidado con los campos como BoldItalic, debería ser Bold Italic para KDE.

El XUID debería ser único. Al menos copiando el de la versión que funcionaba se
arregló.

> Ojo que fontforge a veces se queda como un proceso en segundo plano al 100%,
> luego de cerrar ejecutar por si acaso: killall -9 fontforge

Ajustar nombres si queremos (Los nombres son relevantes. Ver parcheado manual).

---

## Parcheado manual:

1. Descargar FiraCode

https://github.com/tonsky/FiraCode/releases

2. Extraer fuentes bold y medium ttf (No regular, es muy delgada).

3. Descargar font-patcher

```command
wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FontPatcher.zip
```

4. Parchear las fuentes con el patcher:

```command
fontforge -script font-patcher original/FiraCode-Medium.ttf --complete
fontforge -script font-patcher original/FiraCode-Bold.ttf --complete
```

5. Modificar con FontFreezer

https://mutsuntsai.github.io/fontfreeze/ Features: ss03 y ss05 Font family
suffix: FIX

Opciones default: target feature for activation calt

6. Agregar cohete de prompt:

Abrir la fuente FiraCode con FontForge y **con la misma sesión** abrir la otra
fuente. Ahí se puede copiar sin problemas el glifo.

El cohete está en seguisym (Windows 7 font) seguisym -> SegoeUISymbol u1F680
128640

Usar Ver -> "ir a" (go to) origen: U+1F680 destino: F135

La posición u1f680 es usado por emojis y eso puede hacer que no se respete la
versión de esta fuente sino otra específica de emojis, por ello usamos f135.

Definir ancho a 1200?

7. Ajustar nombres antes de exportar

En base a los nombres se agrupan. Asíque deben ser coherentes.

- Regular (medium)

> FiraCodeNerdFontFIX-Regular FiraCode Nerd Font FIX FiraCode Nerd Font FIX
> Regular Regular
>
> Nombres TTF, ID único FiraCodeNerdFontFIX Nerd Font Regular Estilo preferido
> Regular

test:

> FiraCodeNerdFontFIX-Mono FiraCode Nerd Font FIX Mono FiraCode Nerd Font FIX
> Regular Mono Regular
>
> Nombres TTF, ID único FiraCode Nerd Font FIX Mono Familia OTF preferida
> FiraCode Nerd Font FIX Estilos OTF preferidos Regular

FiraCodeNerdFontFIX-Mono.ttf FiraCodeNerdFontFIX-Bold-Mono.ttf

- Bold

> FiraCodeNerdFontFIX-Bold FiraCode Nerd Font FIX FiraCode Nerd Font FIX Bold
> Bold
>
> Nombres TTF, ID único FiraCodeNerdFontFIX Nerd Font Bold

8. Exportar

Archivo -> Generar fuente FiraCodeNerdFontFIX-Regular.ttf
FiraCodeNerdFontFIX-Bold.ttf
