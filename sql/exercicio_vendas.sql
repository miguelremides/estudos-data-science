CREATE TABLE Vendedores (
    id_vendedor INT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE Vendas (
    id_venda INT PRIMARY KEY,
    id_vendedor INT,
    valor_venda DECIMAL(10, 2),
    data_venda DATE,
    FOREIGN KEY (id_vendedor) REFERENCES Vendedores(id_vendedor)
);

-- DESAFIO: Escreva uma query que retorne o NOME do vendedor 
-- e a SOMA TOTAL de suas vendas, ordenado do maior para o menor.

SELECT 
    v.nome, 
    SUM(s.valor_venda) AS total_vendas
FROM Vendedores v
JOIN Vendas s ON v.id_vendedor = s.id_vendedor
GROUP BY v.nome
ORDER BY total_vendas DESC;
