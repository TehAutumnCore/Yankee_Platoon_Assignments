import { Link } from "react-router-dom"

const NavBar = () => {
    return(
        <ul style={{display:'flex',justifyContent:'space-around'}}>
            <li>
                <Link to='/'>Home</Link>
            </li>
            <li>
                <Link to='/about/'>About</Link>
            </li>
            <li>
                <Link to='/characters/'>Characters</Link>
            </li>
        </ul>
    );
};

export default NavBar