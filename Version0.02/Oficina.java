//Version 0.0.2

//Vamos iniciar o nosso código nessa versão
//Aqui temos a nossca class Oficina, ela sera o nosso código fonte
//Mas o que é código fonte?
//Código fonte é aonde vai ficar todas as informações e comportamentos do nosso programa
public class Oficina{

    //Aqui temos os atributos da nossa oficina:
    String nome;
    String cpf;
    String carro;
    int anoCarro;
    String modelo;

    //Agora vamos criar uma classe chamada TestaCliente.java

    /**Agora vamos lidar com métodos, mas o que é método?
    Métodos são ações que a gente pode incorpora na nossa classe Oficina(No caso a principal)
    Agora vamos criar um método que vai se chamar setRegistraCliente
    set vem de settar algo, alguma coisa sendo nome numero ou qualquer outra coisa
    Os set serão muito importantes na orientação a objetos!

    /**e a gente usar o this.nome e this.cpf ele vai retornar null quando a gente chamar
        na classe TestaMetodo.java
        Por conta que é parametro que o usuário vai entra*/
    public void setRegistraCliente(String nome, String cpf){
        System.out.println("Cliente:" + nome);
        System.out.println("Número de CPF:" + cpf);
    }

    public void setRegistraCarro(String carro, int anoCarro, String modelo){
        System.out.println("Marca do carro: " + carro);
        System.out.println("Ano do carro:   " + anoCarro);
        System.out.println("Modelo(Marca):  " + modelo);
    }

    //Agora vamos nos aprofundar mais um pouco nos métodos

}