package org.example;

//ConcreteCommand
public class ComandoEncenderAuto implements ICommando{
    Automovil auto;
    public ComandoEncenderAuto(Automovil autoo){
        this.auto = autoo;
    }

    public void ejecutar(){
        //Invocando al metodo de Automvil
        auto.encenderAuto();
    }

}
