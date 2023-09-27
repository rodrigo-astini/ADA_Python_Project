#Rodar o codigo abaixo no SQL para criar tabela cliente
CREATE TABLE cliente
    (
        id INT PRIMARY KEY IDENTITY(1,1),
        nome NVARCHAR(100) NOT NULL,
        cpf CHAR(14) NOT NULL,
        rg NVARCHAR(20) ,
        data_nascimento DATE ,
        cep CHAR(10) ,
        logradouro NVARCHAR(100) ,
        complemento NVARCHAR(100) ,
		bairro NVARCHAR(100) ,
		cidade NVARCHAR(100) ,
		estado CHAR(2) ,
        numero_residencia NVARCHAR(5) ,
        CONSTRAINT UQ_cpf UNIQUE (cpf)
    );
	set DATEFORMAT DMY