const galleryBlocks = document.querySelectorAll(".GalleryBlock__ImageWrapper");
const modal = document.getElementById("modal");
console.log("🚀 ~ file: landet.js ~ line 3 ~ modal", modal)

let arr = [];
let obj = {};
let i = 0;

galleryBlocks.forEach((image) => {
    
    console.log(image.querySelector("img").getAttribute("src"));
    obj = {
        'id': i,
        'image': image.querySelector("img").getAttribute("src"),
        'caption': image.innerText
    }

    arr = [...arr, obj];
    i++;
    console.log(arr);

    image.addEventListener("click", (e) => {
        document.querySelector('body').style.overflow = "hidden";
        modal.classList.remove("Modal--Z");
        modal.classList.remove("Modal--Hidden");

        const imageHolder = document.getElementById("modal_image");

        
        let img = e.target.closest(".GalleryBlock__ImageWrapper").querySelector("img");
        
        const url = img.getAttribute("src");
        
        // console.log(e.target.getAttribute("src"))
        // if(url){
        //     console.log("jepp ", e.target.getAttribute("src"))
        //     // console.log(e.target.parentNode);
        //     // console.log(e.target.parentNode.querySelector("img"));
        //     console.log(e.target.closest(".GalleryBlock__ImageWrapper"));
        // } else {
        //     // let stuff = e.target.querySelector("img");
        //     console.log(e.target.closest(".GalleryBlock__ImageWrapper"));
        //     // console.log(e.target.parentNode.querySelector("img"));
        // }

        imageHolder.setAttribute("src", url);

        const caption = document.getElementById("modal_figcaption");
        caption.innerHTML = image.innerText;

        const modalOverlay = document.getElementById("modal");
        modalOverlay.addEventListener("click", () => {
            console.log("modalen klickades")
            // document.querySelector('body').style.overflow = "scroll";
            // modal.classList.add("Modal--Hidden");
        })    
        
        const closeButton = document.getElementById("close");
        closeButton.addEventListener("click", () => {
            document.querySelector('body').style.overflow = "scroll";
            modal.classList.add("Modal--Hidden");
            
            setTimeout(() => {
                modal.classList.add("Modal--Z");
            }, 600)

        })
    })
})


function test(){
    console.log("jo men den klickades")
}