import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';
import Header from '../../components/header';

const DogecoinGraph = () => {
    const [observedImage, setObservedImage] = useState('');
    const [trendImage, setTrendImage] = useState('');
    const [seasonalImage, setSeasonalImage] = useState('');
    const [residualImage, setResidualImage] = useState('');
    const [data, setData] = useState([]);
    const [data2y, setData2y] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('http://0.0.0.0:8000/dogecoin');
            const result = await response.json();
            setObservedImage(result.observed);
            setTrendImage(result.trend);
            setSeasonalImage(result.seasonal);
            setResidualImage(result.residual);
            setData(result.data);
            setData2y(result.data_2y);  // Set 2-year data
        };

        fetchData();
    }, []);

    const chartData = {
        labels: Array.from({ length: data.length }, (_, i) => i),  // You can adjust this to use actual dates if available
        datasets: [
            {
                label: 'Dogecoin Price (5 Years)',
                data: data,
                borderColor: 'rgba(75, 192, 192, 1)',
                fill: false,
            },
        ],
    };

    const chartData2y = {
        labels: Array.from({ length: data2y.length }, (_, i) => i),  // You can adjust this to use actual dates if available
        datasets: [
            {
                label: 'Dogecoin Price (2 Years)',
                data: data2y,
                borderColor: 'rgba(153, 102, 255, 1)',
                fill: false,
            },
        ],
    };

    return (
        <>        <Header />
        <div>
            <h1>Dogecoin Price Decomposition (2 Years)</h1>
            {observedImage && <img src={`data:image/png;base64,${observedImage}`} alt="Observed" />}
            {trendImage && <img src={`data:image/png;base64,${trendImage}`} alt="Trend" />}
            {seasonalImage && <img src={`data:image/png;base64,${seasonalImage}`} alt="Seasonality" />}
            {residualImage && <img src={`data:image/png;base64,${residualImage}`} alt="Residual" />}
            
            <h1>Dogecoin Price (5 Years)</h1>
            <Line data={chartData} />

            <h1>Dogecoin Price (2 Years)</h1>
            <Line data={chartData2y} />
        </div></>
    );
};

export default DogecoinGraph;
