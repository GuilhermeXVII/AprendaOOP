public class TestaMetodo{
    public static void main(String[] args){
        Oficina primeiroClienteGuilherme = new Oficina(); 
        primeiroClienteGuilherme.setRegistraCliente("Guiherme", "333.444.555-13");
        primeiroClienteGuilherme.setRegistraCarro("Fiat", 2013, "Uno Mille");

        //Eu posso instaciar sempre um novo objeto com o new, no caso o nosso cliente
        /**
         * Que sempre vai conter: nome, cpf, anocarro, modelo(marca)
         */
        Oficina segundoClienteCarla=new Oficina();
        segundoClienteCarla.setRegistraCliente("Carla", "222.111.000-xx");
        segundoClienteCarla.setRegistraCarro("Gol", 2003, "Gol modelo g3");
    }
}