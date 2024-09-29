import React, { useState } from "react";
import { Botao } from "../../components/button/style";
import Header from "../../components/header";
import axios from 'axios';
import {
  ErrorMessage,
  LeftContainer,
  LoadingIcon,
  PageContainer,
  RightContainer,
  SucessMessage,
  Tabela,
} from "./style";

function Homepage() {
  const [isLoading, setIsLoading] = useState(false);
  const [isTableLoading, setIsTableLoading] = useState(false);
  const [isRetreinado, setIsRetreinado] = useState(false);
  const [error, setError] = useState(null);
  const [tableData, setTableData] = useState(null);

  function handleGetTable() {
    
    setIsTableLoading(true);
  
    axios.get('http://0.0.0.0:8000/predict')
      .then(response => {
        // Handle the successful response
        console.log('Data:', response.data);
        setTableData(response.data);
      })
      .catch(error => {
        // Handle any errors
        console.error('Error fetching data:', error);
      })
      .finally(() => {
        setIsTableLoading(false);
      });
  }
    

  function handleRetreinar() {
    setIsLoading(true);
    axios.get('http://0.0.0.0:8000/retraining')
    .then(response => {
      // Handle the successful response
      console.log('Data:', response.data);
      setError(response.data);
      setIsRetreinado(true);
    })
    .catch(error => {
      // Handle any errors
      console.error('Error fetching data:', error);
    })
    .finally(() => {
      setIsLoading(false);
    });
  }

  function formatDate(dateString) {
    const date = new Date(dateString);
    const day = String(date.getDate()).padStart(2, "0");
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const year = date.getFullYear();

    return `${day}/${month}/${year}`;
  }


  return (
    <PageContainer>
      <Header />
      <LeftContainer>
        <Botao onClick={() => handleGetTable()}>Prever próximos 10 dias</Botao>
        {isTableLoading ? <LoadingIcon /> : null}
        {!tableData ? null :         <Tabela>
          <thead>
            <tr>
              <td>Data</td>
              <td>Preço</td>
            </tr>
          </thead>
          <tbody>
            {tableData?.predicted_values.map((item, index) => (
              <tr key={index + 1}>
                <td>{formatDate(item.ds)}</td>
                <td>{item.yhat}</td>
              </tr>
            ))}
          </tbody>
        </Tabela>}
        {!tableData ? null :         <Tabela>
          <tr style={{ backgroundColor: "#24ABE3", color: "#fff" }}>
            <td>Venda</td>
            <td>
              {formatDate(
                tableData?.predicted_values.find(
                  (item) => item.yhat === tableData?.highest_value
                ).ds
              )}
            </td>
            <td>{tableData?.highest_value}</td>
          </tr>
          <tr style={{ backgroundColor: "#0B8C38", color: "#fff" }}>
            <td>Compra</td>
            <td>
              {formatDate(
                tableData?.predicted_values.find(
                  (item) => item.yhat === tableData?.lowest_value
                ).ds
              )}
            </td>
            <td>{tableData?.lowest_value}</td>
          </tr>
        </Tabela>}
      </LeftContainer>
      <RightContainer>
        <Botao onClick={() => handleRetreinar()}>Retreinar</Botao>
        {isLoading ? <LoadingIcon /> : null}
        {!isLoading && error  && isRetreinado ? (
          <SucessMessage>IA retreinada!</SucessMessage>
        ) : null}
        {!isLoading && !error && isRetreinado ? <ErrorMessage>Deu ruim.</ErrorMessage> : null}
      </RightContainer>
    </PageContainer>
  );
}

export default Homepage;
