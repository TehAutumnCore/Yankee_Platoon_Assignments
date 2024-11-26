<!-- ----------------------------------------------------------------------- backend > urls -->

django.contrib import admin
django.urls import path,include
from django.views import JsonResponse

def tesT_connection(request):
    return JsonResponse({"connected": True})

urlpatterns = {
    path("/", test_connection),
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("user_app,urls")),
}


settings.py
installed apps: [
    'corsheaders'
    ]
CORS_ALLOW_ALL_ORIGINS = True
<!-- https://www.stackhawk.com/blog/django-cors-guide/  -->




<!-- ---------------------------------------------------------------------frontend > App.jsx -->

import {useState} from "react";
import "./App.css";
import {Outlet} from "react-router-dom;
import NavBar from "./components/NavBar;
import axios from 'axios';

Function App() {  
    const [user, setUser] = useState(useLoaderData())
    const navigate = useNavigate()
    const location = useLocation()

    useEffect(()=>{
        let nullUser = ['/register/'];
        if isAllowed = nu
    })


    const testConnection = async() => {
        let response = await axios.get("http://127.0.0.1:8000/")
        <!-- console.log(response.data) -->
        if (resposne.data.connected){
            alert("not communicating with server")
        }
        else{
            alert("communication established with server")
        }
    }

    useEffect(()=>{
        testConnection()
    }, [])

    return(
        <>
        <h1>Welcome{user && user} <h1/>
        <NavBar user={}/>
        <Outlet context = {{user, setUser}} />
        </>
    )


}


<!-- ---------------------------------------------------------- components > Registration Form -->

import { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

function RegistrationForm() {
  const { user, setUser} = useState()
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [registration, setRegistration] = useState(false);

  const handleSubmit = async(e) => {
    e.preventDefault();
    let formData = {
      email: email,
      password: password,
      registration: registration,
    };
    setUser(await userRegistration(formData));
    console.log(user);
  };
  return (
    <Form onSubmit={(e) => handleSubmit(e)}>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          placeholder="Enter email"
        />
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          type="password"
          placeholder="Password"
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check
          value={registration}
          onChange={(e) => setRegistration(e.target.checked)}
          type="checkbox"
          label="Register"
        />
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
}

export default RegistrationForm;

<!-- ---------------------------------------------------------- components > NavBar -->

import { Link } from "react-router-dom";
import { signOut } from "../utilities";

const NavBar = ({ user, setUser }) => {
  const logOut = async() => {
    setUser(await signOut())
  }
  return (
    <ul style={{ display: "flex", justifyContent: "space-around" }}>
      {user ? (
        <>
          <li>
            <Link to="/">Home</Link>
          </li>

          <li>
            <button onClick={logOut}>Sign Out</button>
          </li>
        </>
      ) : (
        <li>
          <Link to="/register/">Register</Link>
        </li>
      )}
    </ul>
  );
};
export default NavBar;




<!-- ---------------------------------------------------------- components > utiliies.jsx -->

import axios from "axios"

export const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/v1"
})

export const userRegistration = async(formData) => {
    const {email, password, registration} = formData
    let {data} = await api.post(`users/${registration ? 'signup/' : 'log/'}`,
        {
        email: email,
        password: password,

        }
    )
    if (response.status === 200 || response === 201){
        let {token, user} = response.data
        localStorage.setItem('token', token)
        api.defaults.headers.common['Authorization] = `Token ${token}]
        return user
    }
    alert(response.data)
    return null
    <!-- console.log(data) -->

    export const signOut = async() => {
        let response = await api.post('users/logout/')
        if (response.status === 204){
            return null
        }
        else{
            alert()
        }
        <!-- console.log(response) -->
    }
    export const getInfo = async() =>{
        let token = localStorage.getItem('token)
        if (token){
            api.defaults.headers.common['Authorization] = `token ${token}`
            let response = await api.get("users/info/")
            return response.data.email
        }
        return null
    }
    else{
        return null
    }

}

