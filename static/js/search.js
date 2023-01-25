new Autocomplete('#autocomplete', {

    search : input =>{
        console.log(input)
        const url = `/search/?search=${input}`
        return new Promise(resolve =>{
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                resolve(data.data)
            })
        })
    },
    onSubmit : result => {
        window.location.href = `/accounts/${result}`
    }
})
