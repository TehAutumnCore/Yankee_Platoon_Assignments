const sayHello = (evt) => {
    console.log("Hello")
}

const sayGoodByte = (evt) => {
    evt.stopPropagation()
    console.log("GoodBye!")
} //must spell out event in html file
//div onclick="SayHello(event)" id ="box-child" style=""></div>

const addImg = () => {
    let imgContainer = document.querySelector("#image-container")
    let img = document. createElement ('img' )
    img.src = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png"
    img.style.width = "25vmin"
    img.style.height = "25vmin" 
    imgContainer.appendChild(img)
    console. log ("image successfully created!") 

    const mouseOutFunction = (evt) => {
        evt.target.style.width = "25vmin"
        evt.target.style.height = "25vmin"
        evt.target.style.backgroundColor = 'transparent'
    }

    // add event listener to img
    img.addEventListener("mouseover",(evt) => {
        evt.target.style.width = "26vmin"
        evt.target.style.height = "26vmin"
        evt.target.style.backgroundColor = "yellow"
    })
    //add event listener to img
    img.addEventListener("mouseover", mouseOverFunc)
    img.addEventListener("mouseOut", mouseOutFunction)


    console.log("image successfully created!")

}

const formSubmit=(evt) => {
    evt.preventDefault() //to stop the page from refreshing and sending the form again
    // console.log("form submitted")
    // console.log(evt.target)
    const formData = new FormData(evt.target) //passing a form into the class FormData
    // console.log(formData)
    const formProps = Object.fromEntries(formData) //creates dictionary from formData
    // console.log(formProps)
    let p_tags = document.querySelector("p")
    p_tags[0].innertext += ' ' + formProps['first']
    p_tags[1].innertext += ' ' + formProps['last']
}

/*
<script src="./main.js" async defer></script>
</head>
<body>
<p>first name :< /p>
<p>last name :< /p>
<form onsubmit="formSubmit(event)">
    <input type="text" name='first' placeholder="first name?"/>
    <input type="text" name='last' placeholder="lastname name?"/>
    <input type="submit"/>
</form>
*/