package org.example;

public class Calcular implements ITarget {
    @Override
    public int sumar(int numero1, int numero2){
        return numero1+numero2;
    }
}
