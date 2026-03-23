public class Teste{
    public static int Soma(int a, int b){
        return a +b;
    }

    public static void mensagem(){
        System.out.println("Olá mundo");
    }

   //void main(){}
    public static void main(String[] args){
        //Fazendo um casting em java
        int x = 7;
        double y=10.7;

        int casting = (int)y;
        System.out.println(casting);

        int resultado=Soma(x, casting);
        System.out.println(resultado);

        mensagem();

        
    }
}