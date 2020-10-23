package org.example;
//ConcreteCommand1: comando donde
public class ComandoApagarAlarma implements ICommando{
    Automovil auto;
    public ComandoApagarAlarma(Automovil autoo){
        this.auto = autoo;
    }

    public void ejecutar(){
        //Invocando al metodo de Automvil
        auto.apagarAlarma();
    }
}//end class
