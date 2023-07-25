import { useState } from "react";
import Cookies from 'js-cookie';

export default function HomePage(){
    const [token, setToken] = useState(Cookies.get('jwt_token'))

    const handleLogin = async () => {

        const data = {
            username: 'Marti',
            password: 'timar201315',
        };
          
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        };


        try {
          const response = await fetch('http://127.0.0.1:8000/api/token/', options)
          const jsonData = await response.json()
          setToken(jsonData.access);
          Cookies.set('jwt_token', jsonData.access, { expires: 1, secure: true, sameSite: 'strict' });

        } catch (error) {
          console.error('Error fetching data:', error);
        }
    };

    const handleLogout = () => {
        const token = Cookies.get('jwt_token');
        console.log(token)
        const hola = async () => {
            try {
              const response = await fetch('http://127.0.0.1:8000/api/movies/all/', {
                method: 'GET',
                headers: {
                  'Authorization': `Bearer ${token}`,
                },
              });

              const jsonData = await response.json()
              console.log(jsonData)
    
            } catch (error) {
              console.error('Error fetching data:', error);
            }
        };

        hola()

        const me = async () => {
          try {
            const response = await fetch('http://127.0.0.1:8000/api/me', {
              method: 'GET',
              headers: {
                'Authorization': `Bearer ${token}`,
              },
            });

            const jsonData = await response.json()
            console.log(jsonData)
  
          } catch (error) {
            console.error('Error fetching data:', error);
          }
      };

      me()

    }

    const handleTokenRevision = () => {
      if(token == undefined || token == null){
        console.log('TOKEN INVALIDOOOO')
      }
    }

    const handleDeleteToken = () => {
      Cookies.remove('jwt_token');
      setToken(Cookies.get('jwt_token'))
    }

    return(
    <>
        <button onClick={handleLogin}>login</button>

        <button onClick={handleLogout}>logout</button>

        <button onClick={handleTokenRevision}>REVISION</button>

        <button onClick={handleDeleteToken}>DELETE</button>
    </>
    )
}