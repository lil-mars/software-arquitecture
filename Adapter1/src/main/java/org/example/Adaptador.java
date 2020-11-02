package org.example;
//Adapter
public class Adaptador implements ITarget{
    //Creando la instancia de "CalcularArreglo"
    AdaptadoCalcularArreglo adaptadoCalcularArreglo = new AdaptadoCalcularArreglo();
    //realizando la adaptacion de una operacion
    @Override
    public int sumar(int numero1,int numero2){
        double resultado;
        //Aqui creamos el ARRAY que necesita el adaptado
        //Adapando los datos que se envian, Adaptado necesita un arreglo de Operandos
        int[] operandos = {numero1,numero2};

        //Realizando la operacion del adaptado
        resultado = adaptadoCalcularArreglo.suma(operandos);

        //Adaptando el resultado
        //El cliente espera un entero
        return (int) resultado;
    }
}
