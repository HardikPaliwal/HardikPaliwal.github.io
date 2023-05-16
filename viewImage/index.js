const imgId = window.location.search.split("?imageId=")[1];

const img = document.createElement('img');
img.setAttribute("src", `../images/${imgId}`)
img.setAttribute("id", "image")
document.getElementById("imageContainer").appendChild(img)
