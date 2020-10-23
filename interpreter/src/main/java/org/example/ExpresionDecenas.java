package org.example;

public class ExpresionDecenas extends Expression {
    @Override
    public String Unidad(){ return "X"; }
    @Override
    public String Cuatro(){ return "XL"; }
    @Override
    public String Cinco(){ return "L"; }
    @Override
    public String Nueve(){ return "XC"; }
    @Override
    public int Factor(){ return 10; }

}
