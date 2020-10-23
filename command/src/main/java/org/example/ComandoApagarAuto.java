package org.example;
//ConcreteCommand
public class ComandoApagarAuto implements ICommando{
    Automovil auto;
    public ComandoApagarAuto(Automovil autoo){
        this.auto = autoo;
    }

    public void ejecutar(){
        //Invocando al metodo de Automvil
        auto.apagarAuto();
    }
}//end class
