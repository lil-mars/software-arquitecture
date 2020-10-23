package org.example;
//1. Receiver - receptor: Es donde se indica que operacion se realizara

public class Automovil {
    // 2. Por cada uno de estos metodos se pueden o no crear los comandos
    //esto es de acuerdo a lo que se requiere
    public void encenderAuto(){
        System.out.println("Se ha encendido el auto");
    }
    public void apagarAuto(){
        System.out.println("Se ha apagado el auto");
    }
    public void encenderAlarma(){
        System.out.println("Alarma encendida");
    }
    public void apagarAlarma(){
        System.out.println("Alarma apagada");
    }


}//end class
