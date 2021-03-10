import React, {useState} from 'react';
import {makeStyles} from '@material-ui/core/styles';
import Button from "@material-ui/core/Button";
import Paper from "@material-ui/core/Paper";
import {Typography} from "@material-ui/core";
import axios from 'axios';
import {API_DOMAIN} from "../App";

const useStyles = makeStyles((theme) => ({
    container: {
        backgroundColor: '#abcdef',
        margin: '10px 10px 20px 10px',
        padding: '10px',
        display: 'flex',
        flexDirection: 'column',
    },
    button: {
        marginTop: '10px',
        alignSelf: 'flex-end'
    }
}));

function PromotionItem(props) {
    const classes = useStyles();

    const {user} = props;

    const [promotion, setPromotion] = useState(props.promotion)
    const {id, title, min_seller, max_seller, start_date, end_date, participants} = promotion;

    const apply = () => {
        const config = {
            method: 'POST',
            url: API_DOMAIN + '/api/promotion/apply',
            headers: {'Content-Type': 'application/json'},
            data: {
                id: id,
                brand_id: user
            }
        };

        axios(config).then((response) => {
            if (response.status === 200) {
                setPromotion(response.data);
            }
        }).catch((e) => {alert(e.response.data)})
    }

    return (
        <Paper className={classes.container}>
            <Typography variant="h6">{title}</Typography>
            <Typography variant="subtitle2">프로모션 기간: {start_date} ~ {end_date}</Typography>
            <Typography variant="subtitle2">최소 인원 {min_seller}명 | 최대 인원 {max_seller}명</Typography>
            <Typography variant="subtitle2">참가 ({participants.length}명): {participants}</Typography>
            <Button variant="contained" size="large" className={classes.button} onClick={apply}>
                신청하기 ({participants.length}/{min_seller})
            </Button>
        </Paper>
    );
}

export default PromotionItem;
