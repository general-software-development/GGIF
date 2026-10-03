# GGIF Previews

<div id="static-gallery"></div>

<style>
#static-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 20px;
  padding: 30px 150px;
  box-sizing: border-box;
}

#static-gallery figure {
  margin: 0;
  min-width: 0;
  text-align: center;
}

#static-gallery img,
#static-gallery video {
  width: 100%;
  height: auto;
  max-height: 300px;
  object-fit: contain;
  display: block;
}

#static-gallery figcaption {
  margin-top: 6px;
  word-break: break-word;
}

#static-gallery figcaption a {
  text-decoration: underline;
}
</style>

<script>
(async () => {
  const gallery = document.getElementById("static-gallery");

  const manifestUrl = new URL(
    "../static/manifest.json",
    window.location.href
  );

  const files = await fetch(manifestUrl).then(r => r.json());

  const videoExtensions = /\.(mp4|webm|ogg|mov|m4v)$/i;

  for (const filename of files) {
    const url = new URL(
      "../static/" + filename,
      window.location.href
    );

    const figure = document.createElement("figure");

    let media;

    if (videoExtensions.test(filename)) {
      media = document.createElement("video");
      media.controls = true;
      media.preload = "metadata";
    } else {
      media = document.createElement("img");
      media.loading = "lazy";
      media.alt = filename;
    }

    media.src = url.href;

    const caption = document.createElement("figcaption");

    const link = document.createElement("a");
    link.href = url.href;
    link.textContent = filename.split("/").pop();
    link.target = "_blank";
    link.rel = "noopener";

    caption.appendChild(link);

    figure.appendChild(media);
    figure.appendChild(caption);

    gallery.appendChild(figure);
  }
})();
</script>
