import {useEffect, useState} from "react";
import axios from 'axios';

const API_DOMAIN = 'http://localhost:8000'

function App() {
  const [promotions, setPromotion] = useState([]);

  const fetchData = () => {
    const config = {
      method: 'GET',
      url: API_DOMAIN + '/api/promotion/get',
    };

    axios(config).then((response) => {
      if (response.status === 200) {
        setPromotion(response.data);
      }
    })
  }
  useEffect(() => {
    fetchData();
  }, [])

  return (
    <div className="App">
      {promotions.map((promotion, index) => <p key={index}>{JSON.stringify(promotion)}</p>)}
    </div>
  );
}

export default App;
