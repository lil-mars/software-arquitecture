package org.example;
//Adaptado
//Esta es la clase con la que no se puede comunicar el Cliente
//El cliente no la puede usar directamente, ya que su interfaz es diferente

public class AdaptadoCalcularArreglo {
    public double suma(int[] pOperandos){
        double resultado=0;
        for(int n=0;n< pOperandos.length;n++){
            resultado += pOperandos[n];
        }
        return resultado;
    }
}
