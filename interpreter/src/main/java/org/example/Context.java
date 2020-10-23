package org.example;

public class Context {
    private String expresion;
    private int valor;
    //recibe la expresion a interpretar
    public Context(String pExpresion){
        this.expresion = pExpresion;
        System.out.println("Se evaluara la expresion: "+ expresion);
    }

    public String getExpresion() { return expresion; }

    public void setExpresion(String expresion) { this.expresion = expresion; }

    public int getValor() { return valor; }

    public void setValor(int valor) {  this.valor = valor; }
}//end class

