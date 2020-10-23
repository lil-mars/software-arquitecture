package org.example;
//ConcreteCommand
public class ComandoEncenderAlarma implements ICommando{
    Automovil auto;
    public ComandoEncenderAlarma(Automovil autoo){
        this.auto = autoo;
    }

    public void ejecutar(){
        //Invocando al metodo de Automvil
        auto.encenderAlarma();
    }
}
