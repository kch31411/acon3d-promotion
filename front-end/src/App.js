import React, {useEffect, useState} from "react";
import axios from 'axios';
import PromotionItem from "./components/PromotionItem";
import Typography from "@material-ui/core/Typography";
import {withStyles} from "@material-ui/styles";
import {InputBase} from "@material-ui/core";

export const API_DOMAIN = 'http://localhost:8000'

const BootstrapInput = withStyles((theme) => ({
    input: {
        border: '1px solid #cecece',
        borderRadius: 4,
        fontSize: "16px",
        padding: '10px',
        width: "100%",
        backgroundColor:"white"
    },
}))(InputBase);

function App() {
    const [promotions, setPromotion] = useState([]);
    const [user, setUser] = useState('');

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
            <div style={{display: 'flex'}}>
                <Typography variant="h4">신청인: </Typography>
                <BootstrapInput value={user}
                                onChange={(e) => setUser(e.target.value)} />
            </div>
            <Typography variant="subtitle1">A~J의 알파벳을 입력해주세요.</Typography>
            {promotions.map((promotion, index) => <PromotionItem key={index} promotion={promotion} user={user} />)}
        </div>
    );
}

export default App;
