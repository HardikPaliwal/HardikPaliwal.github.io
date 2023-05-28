const imgId = window.location.search.split("?imageId=")[1];

const img = document.createElement('img');
img.setAttribute("src", `../images/raw/${imgId}`)
img.setAttribute("id", "image")
document.getElementById("imageContainer").appendChild(img)


async function fetchMetaData() {
    res = await fetch("../images/images_metadata.json")
    // waits until the request completes...
    return await res.json()
  }

  fetchMetaData().then(data => {
    let imgData = data[imgId]
    console.log(imgData)
    document.getElementById("prompt").innerText = imgData.Prompt
    document.getElementById("negativePrompt").innerText = imgData["Negative Prompt"]
    document.getElementById("model").innerText = imgData.Model
    document.getElementById("sampler").innerText = imgData.Sampler
    document.getElementById("seed").innerText = imgData.Seed
    document.getElementById("cfgScale").innerText = imgData["CFG scale"]
    document.getElementById("steps").innerText = imgData.Steps
    document.getElementById("date").innerText =new Date( imgData.Date * 1000).toLocaleString()
    document.getElementById("title").innerText =imgData.Title
  })



