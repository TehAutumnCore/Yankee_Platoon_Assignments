const CharactersPage = () => {
    const [characters,setCharacters] = useState([])
    useEffect(()=>{
        const getCharacters = async() => {
            let {data} = await axios.get(
                "https://thronesapi.com")//api
            };
            setCharacters(data)
        }
        getCharacters();
    },[]);

    return (
        <>
            <h2>Characters </h2>
            <p>
                list characters
            </p>
            <ul>
                {characters.map((character)=>(
                    <li>{characer.fullName}</li>
                ))}
            </ul>
        </>
    )
}