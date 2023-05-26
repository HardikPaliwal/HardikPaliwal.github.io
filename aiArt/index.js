async function fetchMetaData() {
    res = await fetch("../images/images_metadata.json")
    // waits until the request completes...
    return await res.json()
  }

  fetchMetaData().then(data => {

for (const [key, value] of Object.entries(data).reverse()) {
    const a = document.createElement("a")
    // <a href="../viewImage/viewImage.html?imageId=00018-3327410829.jpg">
    a.setAttribute("href", "../viewImage/viewImage.html?imageId=" + key )
    const img = document.createElement('img');
    img.setAttribute("src", `../images/${"THUMBNAIL-" + key}`)
    img.setAttribute("class", "galleryImage")
    img.setAttribute("loading", "lazy")
    a.appendChild(img)
    document.getElementById("mainGallery").appendChild(a)
}  })