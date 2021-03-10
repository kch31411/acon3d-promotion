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

    // TODO: 아래 상태 정보는 서버에서 보내주는 것이 좋을 듯.
    // TODO: 취소 되었음을 유저에게 알리기
    const status = (promotion) => {
        if (new Date() < new Date(start_date)) {
            if (participants.length < max_seller) {
                return "신청 가능"
            } else {
                return "인원 초과"
            }
        } else if (participants.length < min_seller) {
            return "인원 부족으로 취소됨"
        } else if (end_date && new Date() > new Date(end_date)) {
            return "마감됨"
        } else {
            return "진행중"
        }
    }

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
            <Typography variant="subtitle2" color='error'>{status(promotion)}</Typography>
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
