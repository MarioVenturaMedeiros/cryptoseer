import { AiOutlineLoading } from "react-icons/ai";
import styled, { keyframes } from "styled-components";

export const PageContainer = styled.div`
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  overflow: hidden;
`;

export const LeftContainer = styled.div`
  box-sizing: border-box;
  padding: 1%;
  width: 85%;
  text-align: center;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
`;

export const RightContainer = styled.div`
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: start;
  flex-wrap: wrap;
  width: 15%;
`;

export const Tabela = styled.table`
  margin: 20px 0;
  width: 90%;
  font-size: 1.1rem;

  thead {
    font-weight: 600;
  }

  td {
    padding: 10px 0;
    border: 1px solid #000;
  }
`;

export const Resumo = styled.div`
  width: 90%;
  border: 1px solid #000;
`;

export const ResumoItem = styled.div`
  width: 50%;
`;

const rotate = keyframes`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`;

export const LoadingIcon = styled(AiOutlineLoading)`
  width: 100%;
  animation: ${rotate} 1s linear infinite;
  font-size: 4rem;
`;

export const SucessMessage = styled.div`
  width: 70%;
  padding: 10px;
  text-align: center;
  background-color: #63f059;
  border-radius: 5px;
  color: #fff;
`;

export const ErrorMessage = styled.div`
  width: 70%;
  padding: 10px;
  text-align: center;
  background-color: #f05959;
  border-radius: 5px;
  color: #fff;
`;
