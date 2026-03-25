/*create database G9;
use	G9;
create table tbl_cliente (
id_cliente int auto_increment primary key,
cpf_cliente varchar (20) not null,
nome_cliente varchar (100) not null,
telefone_cliente varchar (100) not null,
email_cliente varchar (100) not null,
data_nasc_cliente date not null,
endereco_cliente varchar (100) not null,
data_cadastro date not null,
status_cliente varchar (100) not null
);

insert into tbl_cliente
(cpf_cliente, nome_cliente, telefone_cliente, email_cliente, data_nasc_cliente, endereco_cliente, data_cadastro, status_cliente)
values
('111.111.111-11', 'Alisson', '(11)99999-9999', 'alisson_teste@gmail.com', '1999-02-22', 'Rua Itapecerica,220', '2026-03-25', 'Ativo'),
('222.222.222-22', 'Arthur', '(11)99999-9998', 'arthur_teste@gmail.com', '1999-02-25', 'Rua Taboão,220', '2026-03-25', 'Ativo'),
('333.333.333-33', 'Gabriel', '(11)99999-9997', 'gabriel_teste@gmail.com', '1999-02-19', 'Rua Embu,220', '2026-03-25', 'Ativo'),
('444.444.444-44', 'Giovanni', '(11)99999-9996', 'giovanni_teste@gmail.com', '1999-02-01', 'Rua Pinheiros,220', '2026-03-25', 'Ativo'),
('555.555.555-55', 'Samuel', '(11)99999-9995', 'samuel_teste@gmail.com', '1999-02-10', 'Rua São Paulo,220', '2026-03-25', 'Ativo');

delete from tbl_cliente where id_cliente between 6 and 10;*/
describe tbl_cliente;
select * from tbl_cliente;