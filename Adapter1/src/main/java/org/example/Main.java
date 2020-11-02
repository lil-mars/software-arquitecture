package org.example;
//Client
public class Main
{
    public static void main( String[] args )
    {
        int resultado = 0;
        //Usando la Interfaz que el cliente conoce
        // En esta primera parte, el cliente conoce, que hay una clase que calcula la suma de
        // dos numeros
        ITarget targetCalcular = new Calcular();
        resultado = targetCalcular.sumar(4,3);
        System.out.println("La suma de dos numeros es: "+resultado);

        System.out.println(" --------------------------------------------------------------- ");
        System.out.println(" --------------------------------------------------------------- ");

        //Ahora, hay una clase que desea incorporar y esta tiene una interfaz diferente "CAdaptador"
        //Asignando "CAdaptador" a la instancia "targetCalcular"
        targetCalcular = new Adaptador();
        resultado = targetCalcular.sumar(7,8);
        System.out.println("El resultado de la suma de dos numeros es: "+resultado);
    }
}
