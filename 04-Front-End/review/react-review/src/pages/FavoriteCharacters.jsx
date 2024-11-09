import { useOutletContext } from "react-router-dom"

const FavoriteCharacters = () => {
    const {isFavorite,addFavorite,rmFavorite} = useOutletContext
    return (
        <h2>Favorite Characters</h2>
        {
            FavoriteCharacters.map((character)=>())
        }
    )
}

export default FavoriteCharacters